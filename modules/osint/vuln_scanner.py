"""
Vulnerability Scanner Module
"""

import socket
import ssl
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

class VulnScanner:
    """Vulnerability scanner with AI-powered analysis."""
    
    def __init__(self):
        self.vulnerabilities = []
    
    def scan(self, target):
        """Perform vulnerability scan on target."""
        console.print(f"\n[bold cyan]🎯 Vulnerability Scan: {target}[/bold cyan]\n")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            
            # SSL/TLS Check
            task = progress.add_task("[cyan]Checking SSL/TLS...", total=None)
            ssl_vulns = self._check_ssl(target)
            self.vulnerabilities.extend(ssl_vulns)
            progress.update(task, completed=True)
            
            # Security Headers
            task = progress.add_task("[cyan]Analyzing security headers...", total=None)
            header_vulns = self._check_headers(target)
            self.vulnerabilities.extend(header_vulns)
            progress.update(task, completed=True)
            
            # Common Vulnerabilities
            task = progress.add_task("[cyan]Testing common vulnerabilities...", total=None)
            common_vulns = self._check_common_vulns(target)
            self.vulnerabilities.extend(common_vulns)
            progress.update(task, completed=True)
        
        # Display results
        self._display_results()
        
        # AI Analysis
        if self.vulnerabilities:
            console.print("\n[bold yellow]🤖 AI Recommendations:[/bold yellow]\n")
            from core.ai_engine import AIEngine
            ai = AIEngine()
            
            vuln_summary = "\n".join([f"- {v}" for v in self.vulnerabilities])
            prompt = f"Analyze these vulnerabilities and provide exploitation guidance:\n{vuln_summary}"
            
            analysis = ai.chat(prompt)
            console.print(analysis)
        
        return self.vulnerabilities
    
    def _check_ssl(self, target):
        """Check SSL/TLS configuration."""
        vulns = []
        
        host = target.replace("https://", "").replace("http://", "").split("/")[0]
        
        try:
            context = ssl.create_default_context()
            with socket.create_connection((host, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    cert = ssock.getpeercert()
                    version = ssock.version()
                    
                    # Check TLS version
                    if version in ['TLSv1', 'TLSv1.1']:
                        vulns.append(f"[HIGH] Outdated TLS version: {version}")
                    
                    # Check certificate expiry
                    import datetime
                    not_after = cert.get('notAfter')
                    if not_after:
                        # Parse date (format: 'May 26 12:00:00 2024 GMT')
                        try:
                            expiry = datetime.datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
                            if expiry < datetime.datetime.now():
                                vulns.append("[CRITICAL] SSL certificate expired!")
                            elif (expiry - datetime.datetime.now()).days < 30:
                                vulns.append("[MEDIUM] SSL certificate expires soon")
                        except:
                            pass
        except ssl.SSLError as e:
            vulns.append(f"[HIGH] SSL Error: {str(e)}")
        except:
            pass
        
        return vulns
    
    def _check_headers(self, target):
        """Check security headers."""
        vulns = []
        
        try:
            import requests
            
            url = target if target.startswith("http") else f"https://{target}"
            
            response = requests.get(url, timeout=5, verify=False,
                                   headers={"User-Agent": "Mozilla/5.0"})
            
            headers = response.headers
            
            # Critical security headers
            security_headers = {
                'Strict-Transport-Security': '[HIGH] Missing HSTS header',
                'X-Content-Type-Options': '[MEDIUM] Missing X-Content-Type-Options',
                'X-Frame-Options': '[MEDIUM] Missing X-Frame-Options (Clickjacking)',
                'X-XSS-Protection': '[LOW] Missing X-XSS-Protection',
                'Content-Security-Policy': '[MEDIUM] Missing Content-Security-Policy'
            }
            
            for header, vuln in security_headers.items():
                if header not in headers:
                    vulns.append(vuln)
            
            # Check for server version disclosure
            if 'Server' in headers:
                server = headers['Server']
                if any(v in server.lower() for v in ['apache', 'nginx', 'iis']):
                    if any(char.isdigit() for char in server):
                        vulns.append(f"[LOW] Server version disclosure: {server}")
            
            # Check for sensitive info in headers
            if 'X-Powered-By' in headers:
                vulns.append(f"[LOW] Technology disclosure: {headers['X-Powered-By']}")
                
        except:
            vulns.append("[INFO] Unable to check headers (connection failed)")
        
        return vulns
    
    def _check_common_vulns(self, target):
        """Check for common web vulnerabilities."""
        vulns = []
        
        try:
            import requests
            
            url = target if target.startswith("http") else f"https://{target}"
            
            # Check for directory listing
            common_dirs = ['/admin/', '/backup/', '/.git/', '/.env', '/config/', 
                          '/phpinfo.php', '/server-status', '/wp-admin/']
            
            for path in common_dirs:
                try:
                    test_url = url.rstrip('/') + path
                    response = requests.get(test_url, timeout=3, verify=False,
                                           headers={"User-Agent": "Mozilla/5.0"})
                    
                    if response.status_code == 200:
                        if '.git' in path:
                            vulns.append(f"[CRITICAL] Git repository exposed: {path}")
                        elif '.env' in path:
                            vulns.append(f"[CRITICAL] Environment file exposed: {path}")
                        elif 'phpinfo' in path:
                            vulns.append(f"[HIGH] PHP info exposed: {path}")
                        elif response.status_code != 404:
                            vulns.append(f"[MEDIUM] Sensitive path accessible: {path}")
                except:
                    pass
            
            # Check robots.txt for interesting paths
            try:
                robots = requests.get(f"{url}/robots.txt", timeout=3, verify=False)
                if robots.status_code == 200:
                    content = robots.text.lower()
                    if 'admin' in content or 'backup' in content or 'secret' in content:
                        vulns.append("[INFO] robots.txt reveals sensitive paths")
            except:
                pass
                
        except:
            pass
        
        return vulns
    
    def _display_results(self):
        """Display scan results."""
        console.print("\n[bold green]═══════════════════════════════════════[/bold green]")
        console.print("[bold green]       VULNERABILITY SCAN RESULTS[/bold green]")
        console.print("[bold green]═══════════════════════════════════════[/bold green]\n")
        
        if not self.vulnerabilities:
            console.print("[green]✓ No vulnerabilities detected[/green]")
            return
        
        table = Table(title="Discovered Vulnerabilities")
        table.add_column("Severity", style="bold")
        table.add_column("Description", style="white")
        
        for vuln in self.vulnerabilities:
            if "[CRITICAL]" in vuln:
                severity = "[red]CRITICAL[/red]"
            elif "[HIGH]" in vuln:
                severity = "[orange1]HIGH[/orange1]"
            elif "[MEDIUM]" in vuln:
                severity = "[yellow]MEDIUM[/yellow]"
            elif "[LOW]" in vuln:
                severity = "[blue]LOW[/blue]"
            else:
                severity = "[dim]INFO[/dim]"
            
            desc = vuln.replace("[CRITICAL]", "").replace("[HIGH]", "").replace("[MEDIUM]", "").replace("[LOW]", "").replace("[INFO]", "").strip()
            table.add_row(severity, desc)
        
        console.print(table)
        console.print(f"\n[bold]Total: {len(self.vulnerabilities)} issues found[/bold]")
