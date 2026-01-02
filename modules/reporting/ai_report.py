"""
AI-Powered Report Generator
"""

import os
import json
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

class AIReportGenerator:
    """Generate professional penetration test reports with AI."""
    
    def __init__(self):
        self.reports_dir = Path(__file__).parent.parent.parent / "logs"
        self.reports_dir.mkdir(exist_ok=True)
        self.findings = []
    
    def add_finding(self, finding):
        """Add a finding to the report."""
        self.findings.append(finding)
    
    def generate(self, format_type, findings=None):
        """Generate report in specified format."""
        
        if findings:
            self.findings = findings
        
        if not self.findings:
            console.print("[yellow]No findings to report. Using demo data.[/yellow]")
            self.findings = self._get_demo_findings()
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            
            task = progress.add_task("[cyan]🤖 AI generating report...", total=None)
            
            if format_type == 1:  # JSON
                report_path = self._generate_json(timestamp)
            elif format_type == 2:  # HTML
                report_path = self._generate_html(timestamp)
            elif format_type == 3:  # Markdown
                report_path = self._generate_markdown(timestamp)
            elif format_type == 4:  # PDF
                report_path = self._generate_pdf(timestamp)
            else:
                report_path = None
            
            progress.update(task, completed=True)
        
        return report_path
    
    def _get_demo_findings(self):
        """Get demo findings for testing."""
        return [
            {
                "title": "SQL Injection Vulnerability",
                "severity": "CRITICAL",
                "cvss": 9.8,
                "location": "/api/v1/users",
                "description": "The application is vulnerable to SQL injection attacks via the 'id' parameter.",
                "impact": "An attacker could extract, modify, or delete data from the database.",
                "remediation": "Use parameterized queries or prepared statements."
            },
            {
                "title": "Missing Security Headers",
                "severity": "MEDIUM",
                "cvss": 5.3,
                "location": "All responses",
                "description": "Several security headers are missing including HSTS, CSP, and X-Frame-Options.",
                "impact": "Users may be vulnerable to clickjacking and man-in-the-middle attacks.",
                "remediation": "Implement proper security headers on all responses."
            },
            {
                "title": "Outdated Software",
                "severity": "HIGH",
                "cvss": 7.5,
                "location": "Web server",
                "description": "Apache 2.4.41 is running which has known vulnerabilities.",
                "impact": "Server may be vulnerable to known exploits.",
                "remediation": "Update Apache to the latest version."
            }
        ]
    
    def _generate_json(self, timestamp):
        """Generate JSON report."""
        
        report = {
            "report_type": "Penetration Test Report",
            "generated": datetime.now().isoformat(),
            "generated_by": "MARS AI",
            "author": "J0J0M0J0",
            "findings": self.findings,
            "summary": {
                "total_findings": len(self.findings),
                "critical": len([f for f in self.findings if f.get("severity") == "CRITICAL"]),
                "high": len([f for f in self.findings if f.get("severity") == "HIGH"]),
                "medium": len([f for f in self.findings if f.get("severity") == "MEDIUM"]),
                "low": len([f for f in self.findings if f.get("severity") == "LOW"])
            }
        }
        
        report_path = self.reports_dir / f"mars_report_{timestamp}.json"
        
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        return str(report_path)
    
    def _generate_markdown(self, timestamp):
        """Generate Markdown report."""
        
        from core.ai_engine import AIEngine
        ai = AIEngine()
        
        # Generate executive summary with AI
        findings_json = json.dumps(self.findings, indent=2)
        exec_summary = ai.write_report(findings_json, "executive_summary")
        
        report = f"""# 🔴 MARS Penetration Test Report

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Author:** J0J0M0J0  
**Tool:** MARS AI Red Team Framework

---

## Executive Summary

{exec_summary}

---

## Summary of Findings

| Severity | Count |
|----------|-------|
| 🔴 Critical | {len([f for f in self.findings if f.get("severity") == "CRITICAL"])} |
| 🟠 High | {len([f for f in self.findings if f.get("severity") == "HIGH"])} |
| 🟡 Medium | {len([f for f in self.findings if f.get("severity") == "MEDIUM"])} |
| 🔵 Low | {len([f for f in self.findings if f.get("severity") == "LOW"])} |
| **Total** | **{len(self.findings)}** |

---

## Detailed Findings

"""
        
        for i, finding in enumerate(self.findings, 1):
            severity_icon = {
                "CRITICAL": "🔴",
                "HIGH": "🟠",
                "MEDIUM": "🟡",
                "LOW": "🔵"
            }.get(finding.get("severity", "INFO"), "⚪")
            
            report += f"""### {i}. {finding.get('title', 'Finding')}

**Severity:** {severity_icon} {finding.get('severity', 'N/A')}  
**CVSS Score:** {finding.get('cvss', 'N/A')}  
**Location:** `{finding.get('location', 'N/A')}`

**Description:**  
{finding.get('description', 'No description provided.')}

**Impact:**  
{finding.get('impact', 'No impact assessment provided.')}

**Remediation:**  
{finding.get('remediation', 'No remediation provided.')}

---

"""
        
        report += f"""
## Conclusion

This penetration test was conducted using MARS AI-powered automation.
All testing was performed with proper authorization.

---

**Report Generated by MARS**  
**made by J0J0M0J0**  
*AI-Powered Red Team Automation*
"""
        
        report_path = self.reports_dir / f"mars_report_{timestamp}.md"
        
        with open(report_path, 'w') as f:
            f.write(report)
        
        return str(report_path)
    
    def _generate_html(self, timestamp):
        """Generate HTML report."""
        
        report_path = self.reports_dir / f"mars_report_{timestamp}.html"
        
        findings_html = ""
        for i, finding in enumerate(self.findings, 1):
            severity_color = {
                "CRITICAL": "#dc3545",
                "HIGH": "#fd7e14",
                "MEDIUM": "#ffc107",
                "LOW": "#17a2b8"
            }.get(finding.get("severity", "INFO"), "#6c757d")
            
            findings_html += f"""
            <div class="finding">
                <h3>{i}. {finding.get('title', 'Finding')}</h3>
                <span class="severity" style="background-color: {severity_color};">
                    {finding.get('severity', 'N/A')} (CVSS: {finding.get('cvss', 'N/A')})
                </span>
                <p><strong>Location:</strong> <code>{finding.get('location', 'N/A')}</code></p>
                <p><strong>Description:</strong> {finding.get('description', 'N/A')}</p>
                <p><strong>Impact:</strong> {finding.get('impact', 'N/A')}</p>
                <p><strong>Remediation:</strong> {finding.get('remediation', 'N/A')}</p>
            </div>
            """
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MARS Penetration Test Report</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #eee;
            min-height: 100vh;
        }}
        .header {{
            text-align: center;
            padding: 40px;
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            color: #ff4757;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }}
        .summary-card {{
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }}
        .finding {{
            background: rgba(255,255,255,0.05);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            border-left: 4px solid #ff4757;
        }}
        .severity {{
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            color: white;
            font-weight: bold;
        }}
        code {{
            background: rgba(255,255,255,0.1);
            padding: 2px 8px;
            border-radius: 4px;
        }}
        .footer {{
            text-align: center;
            padding: 20px;
            margin-top: 40px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🔴 MARS Penetration Test Report</h1>
        <p>Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p>Author: J0J0M0J0 | Tool: MARS AI</p>
    </div>
    
    <div class="summary">
        <div class="summary-card" style="border-bottom: 3px solid #dc3545;">
            <h2>{len([f for f in self.findings if f.get("severity") == "CRITICAL"])}</h2>
            <p>Critical</p>
        </div>
        <div class="summary-card" style="border-bottom: 3px solid #fd7e14;">
            <h2>{len([f for f in self.findings if f.get("severity") == "HIGH"])}</h2>
            <p>High</p>
        </div>
        <div class="summary-card" style="border-bottom: 3px solid #ffc107;">
            <h2>{len([f for f in self.findings if f.get("severity") == "MEDIUM"])}</h2>
            <p>Medium</p>
        </div>
        <div class="summary-card" style="border-bottom: 3px solid #17a2b8;">
            <h2>{len([f for f in self.findings if f.get("severity") == "LOW"])}</h2>
            <p>Low</p>
        </div>
    </div>
    
    <h2>Detailed Findings</h2>
    {findings_html}
    
    <div class="footer">
        <p>Report Generated by MARS AI Red Team Framework</p>
        <p>made by J0J0M0J0</p>
    </div>
</body>
</html>"""
        
        with open(report_path, 'w') as f:
            f.write(html)
        
        return str(report_path)
    
    def _generate_pdf(self, timestamp):
        """Generate PDF report (placeholder)."""
        console.print("[yellow]PDF generation requires additional dependencies.[/yellow]")
        console.print("[dim]Install with: pip install reportlab[/dim]")
        console.print("[green]Generating Markdown instead...[/green]")
        
        return self._generate_markdown(timestamp)
