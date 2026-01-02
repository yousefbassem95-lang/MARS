"""
AI-Powered Reconnaissance Module
"""

import socket
import subprocess
import json
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

class AIRecon:
    """AI-powered reconnaissance and target analysis."""
    
    def __init__(self):
        self.results = {}
    
    def analyze(self, target):
        """Perform comprehensive AI-powered reconnaissance."""
        console.print(f"\n[bold cyan]🔍 AI Reconnaissance: {target}[/bold cyan]\n")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            
            # DNS Resolution
            task = progress.add_task("[cyan]Resolving DNS...", total=None)
            dns_info = self._resolve_dns(target)
            progress.update(task, completed=True)
            
            # Port Scan (common ports)
            task = progress.add_task("[cyan]Scanning ports...", total=None)
            ports = self._quick_port_scan(target)
            progress.update(task, completed=True)
            
            # Technology Detection
            task = progress.add_task("[cyan]Detecting technologies...", total=None)
            tech = self._detect_tech(target)
            progress.update(task, completed=True)
            
            # Subdomain Enumeration
            task = progress.add_task("[cyan]Enumerating subdomains...", total=None)
            subdomains = self._enum_subdomains(target)
            progress.update(task, completed=True)
        
        # Compile results
        self.results = {
            "target": target,
            "dns": dns_info,
            "open_ports": ports,
            "technologies": tech,
            "subdomains": subdomains
        }
        
        # Display results
        self._display_results()
        
        # AI Analysis
        console.print("\n[bold yellow]🤖 AI Analysis:[/bold yellow]\n")
        from core.ai_engine import AIEngine
        ai = AIEngine()
        analysis = ai.analyze_target(json.dumps(self.results))
        console.print(analysis)
        
        return self.results
    
    def _resolve_dns(self, target):
        """Resolve DNS for target."""
        try:
            # Remove protocol if present
            host = target.replace("https://", "").replace("http://", "").split("/")[0]
            
            ip = socket.gethostbyname(host)
            return {"hostname": host, "ip": ip}
        except:
            return {"hostname": target, "ip": "Unable to resolve"}
    
    def _quick_port_scan(self, target):
        """Quick scan of common ports."""
        common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 
                       993, 995, 1433, 3306, 3389, 5432, 8080, 8443]
        open_ports = []
        
        host = target.replace("https://", "").replace("http://", "").split("/")[0]
        
        try:
            ip = socket.gethostbyname(host)
        except:
            return []
        
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    service = self._get_service_name(port)
                    open_ports.append({"port": port, "service": service})
                sock.close()
            except:
                pass
        
        return open_ports
    
    def _get_service_name(self, port):
        """Get service name for common ports."""
        services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 
            53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
            1433: "MSSQL", 3306: "MySQL", 3389: "RDP", 
            5432: "PostgreSQL", 8080: "HTTP-Alt", 8443: "HTTPS-Alt"
        }
        return services.get(port, "Unknown")
    
    def _detect_tech(self, target):
        """Detect web technologies."""
        tech = []
        
        try:
            import requests
            
            url = target if target.startswith("http") else f"http://{target}"
            
            response = requests.get(url, timeout=5, verify=False, 
                                   allow_redirects=True,
                                   headers={"User-Agent": "Mozilla/5.0"})
            
            headers = response.headers
            
            # Server detection
            if 'Server' in headers:
                tech.append(f"Server: {headers['Server']}")
            
            # X-Powered-By
            if 'X-Powered-By' in headers:
                tech.append(f"Powered by: {headers['X-Powered-By']}")
            
            # Check for common frameworks in HTML
            content = response.text.lower()
            
            if 'wordpress' in content or 'wp-content' in content:
                tech.append("CMS: WordPress")
            elif 'drupal' in content:
                tech.append("CMS: Drupal")
            elif 'joomla' in content:
                tech.append("CMS: Joomla")
            
            if 'react' in content:
                tech.append("Frontend: React")
            elif 'vue' in content:
                tech.append("Frontend: Vue.js")
            elif 'angular' in content:
                tech.append("Frontend: Angular")
            
            if 'jquery' in content:
                tech.append("Library: jQuery")
            
            # Security headers check
            security_headers = ['X-Frame-Options', 'X-XSS-Protection', 
                              'Content-Security-Policy', 'Strict-Transport-Security']
            missing_headers = [h for h in security_headers if h not in headers]
            
            if missing_headers:
                tech.append(f"⚠️ Missing security headers: {', '.join(missing_headers)}")
            
        except:
            tech.append("Unable to detect (connection failed)")
        
        return tech if tech else ["No technologies detected"]
    
    def _enum_subdomains(self, target):
        """Enumerate subdomains using common prefixes."""
        subdomains = []
        
        # Extract base domain
        host = target.replace("https://", "").replace("http://", "").split("/")[0]
        
        # Common subdomain prefixes
        prefixes = ['www', 'mail', 'ftp', 'admin', 'api', 'dev', 'staging',
                   'test', 'beta', 'portal', 'vpn', 'remote', 'app', 'blog',
                   'shop', 'store', 'cdn', 'static', 'assets', 'img']
        
        for prefix in prefixes:
            subdomain = f"{prefix}.{host}"
            try:
                socket.gethostbyname(subdomain)
                subdomains.append(subdomain)
            except:
                pass
        
        return subdomains if subdomains else ["No subdomains found"]
    
    def _display_results(self):
        """Display reconnaissance results in a table."""
        console.print("\n[bold green]═══════════════════════════════════════[/bold green]")
        console.print("[bold green]       RECONNAISSANCE RESULTS[/bold green]")
        console.print("[bold green]═══════════════════════════════════════[/bold green]\n")
        
        # DNS Info
        console.print(f"[cyan]Target:[/cyan] {self.results['target']}")
        console.print(f"[cyan]IP:[/cyan] {self.results['dns'].get('ip', 'N/A')}\n")
        
        # Open Ports
        if self.results['open_ports']:
            table = Table(title="Open Ports")
            table.add_column("Port", style="cyan")
            table.add_column("Service", style="green")
            
            for port_info in self.results['open_ports']:
                table.add_row(str(port_info['port']), port_info['service'])
            
            console.print(table)
        else:
            console.print("[yellow]No open ports detected[/yellow]")
        
        # Technologies
        console.print("\n[bold]Detected Technologies:[/bold]")
        for tech in self.results['technologies']:
            console.print(f"  • {tech}")
        
        # Subdomains
        if self.results['subdomains'] and self.results['subdomains'] != ["No subdomains found"]:
            console.print("\n[bold]Discovered Subdomains:[/bold]")
            for sub in self.results['subdomains']:
                console.print(f"  • {sub}")
