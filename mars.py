#!/usr/bin/env python3
"""
MARS - AI-Powered Red Team Automation
Created by J0J0M0J0
For Authorized Security Testing Only
"""

import sys
import os
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.markdown import Markdown

console = Console()

ICON = """
              #####                    ****                     #####   
              #######                 ******                   ######             
          ####   ##########           ******             ##########  ###          
         #####           #######       ****        ########         #####        
         #####                #####             #####               #####        
           #####################  #   #####     # ######################         
                              ###   #########   ###                            
                       #######    ############      ######                       
                     ##########   #############    #########                     
                   ###########    #############    ###########                   
                 ######       ##  ############# ##         ######                 
               #####        #####  ###########  ####         #####               
             ****#        *******#  #########   #******         #****             
           ****         **+++***     ######      ***+++***        ****           
         ***          *++++*+  ***  *+++++++*  *** ++++++**          ***         
       **           *+++++    *+++  ++++++++   +++*    ++++++*          **       
                  +++++       +=+    +=====+    +=+      +++++*                  
                ++++         +=+     +=====+     +=+        ++++*                
              ++==          +=+      +=====+      +=+          ==++              
            ++=            ===       =----=        ===            ==+            
                           ==        =----=         ==              =++         
                          ==         =----=          ==                          
                         ==          =-::-=           ==                         
                         =            =::=             =                         
                        =             =::=              =                        
                       -              =..=               -                       
                      :               :.:                 :                       
                                      :::                                       
                                      :::                                        
                                      ---                                        
                                      |||

       .   .
     .'     '.
    /   o     \\
   |     o     |
    \\    _    /
     '.     .'
       '...'
"""

BANNER = """
███╗   ███╗ █████╗ ██████╗ ███████╗
████╗ ████║██╔══██╗██╔══██╗██╔════╝
██╔████╔██║███████║██████╔╝███████╗
██║╚██╔╝██║██╔══██║██╔══██╗╚════██║
██║ ╚═╝ ██║██║  ██║██║  ██║███████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
"""

def show_legal_warning():
    """Display legal warning and get user consent."""
    warning = """
⚠️  LEGAL WARNING ⚠️

MARS is for AUTHORIZED SECURITY TESTING ONLY.

This AI-powered tool can perform automated penetration testing.
Unauthorized use against systems you do not own or have explicit 
permission to test is ILLEGAL and UNETHICAL.

By using MARS, you agree that:
• You have WRITTEN AUTHORIZATION to test the target systems
• You will use MARS ONLY on systems you own or have permission to test
• You accept FULL RESPONSIBILITY for your actions
• You understand AI actions are logged and auditable

Type 'I AGREE' to continue (or 'exit' to quit):
"""
    console.print(Panel(warning, border_style="bold red", title="[bold red]⚠️  LEGAL DISCLAIMER[/bold red]"))
    response = input().strip()
    
    if response != "I AGREE":
        console.print("[bold red]Exiting. You must agree to the terms to use MARS.[/bold red]")
        sys.exit(0)

def display_banner():
    """Display MARS banner."""
    # Mars Red Theme: #FF4500 (OrangeRed) to #8B0000 (DarkRed)
    console.print(f"[bold #FF4500]{ICON}[/bold #FF4500]", justify="center")
    console.print(f"[bold #8B0000]{BANNER}[/bold #8B0000]", justify="center")
    console.print("\n[bold white on #8B0000] AI-POWERED RED TEAM AUTOMATION [/bold white on #8B0000]", justify="center")
    console.print("\n[bold white]made by J0J0M0J0[/bold white]", justify="center")
    console.print("[dim]Think Like a Hacker. Attack Like an AI.[/dim]\n", justify="center")

def show_main_menu():
    """Display the main interactive menu."""
    menu = """
[bold red]♂️ MARS - Main Menu[/bold red]

[cyan][1][/cyan] 🔍 [white]Reconnaissance[/white]
    └── AI-powered target analysis and OSINT

[cyan][2][/cyan] 🎯 [white]Vulnerability Scan[/white]
    └── Intelligent vulnerability discovery

[cyan][3][/cyan] 💀 [white]Exploit Generation[/white]
    └── AI-generated custom payloads

[cyan][4][/cyan] 🎭 [white]MITRE ATT&CK Emulation[/white]
    └── Simulate APT groups (Lazarus, APT29, etc.)

[cyan][5][/cyan] 💬 [white]AI Chat Mode[/white]
    └── Natural language red teaming

[cyan][6][/cyan] 📊 [white]Generate Report[/white]
    └── AI-written penetration test reports

[cyan][7][/cyan] ⚙️  [white]Settings[/white]
    └── Configure AI models and preferences

[bold red][99][/bold red] 💥 [white]Self-Destruct[/white]
    └── Emergency cleanup and exit

[cyan][0][/cyan] 🚪 [white]Exit[/white]
"""
    console.print(Panel(menu, border_style="red"))

def ai_chat_mode():
    """Interactive AI chat mode for natural language red teaming."""
    from core.ai_engine import AIEngine
    
    console.print("\n[bold red]💬 MARS AI Chat Mode[/bold red]")
    console.print("[dim]Type 'exit' to return to main menu[/dim]\n")
    
    ai = AIEngine()
    
    if not ai.is_configured():
        console.print("[yellow]⚠️  No AI model configured. Setting up...[/yellow]")
        ai.setup_interactive()
    
    console.print(f"[green]✓ Using AI Model: {ai.get_model_name()}[/green]\n")
    
    while True:
        try:
            user_input = Prompt.ask("[bold cyan]You[/bold cyan]")
            
            if user_input.lower() in ['exit', 'quit', 'back']:
                break
            
            if not user_input.strip():
                continue
            
            # Get AI response
            console.print("\n[dim]🤖 MARS is thinking...[/dim]")
            response = ai.chat(user_input)
            
            console.print(f"\n[bold red]MARS[/bold red]: {response}\n")
            
        except KeyboardInterrupt:
            break
    
    console.print("\n[yellow]Exiting chat mode...[/yellow]\n")

def reconnaissance_mode():
    """AI-powered reconnaissance mode."""
    from modules.osint.ai_recon import AIRecon
    
    console.print("\n[bold red]🔍 AI Reconnaissance Mode[/bold red]\n")
    
    target = Prompt.ask("[cyan]Enter target domain/IP[/cyan]")
    
    if not target:
        console.print("[red]No target specified[/red]")
        return
    
    console.print(f"\n[yellow]🤖 Initiating AI reconnaissance on: {target}[/yellow]\n")
    
    recon = AIRecon()
    results = recon.analyze(target)
    
    if results:
        console.print("\n[bold green]✓ Reconnaissance Complete[/bold green]\n")
        console.print(Panel(str(results), title="AI Analysis", border_style="green"))

def vuln_scan_mode():
    """AI-powered vulnerability scanning."""
    from modules.osint.vuln_scanner import VulnScanner
    
    console.print("\n[bold red]🎯 AI Vulnerability Scanner[/bold red]\n")
    
    target = Prompt.ask("[cyan]Enter target URL/IP[/cyan]")
    
    if not target:
        console.print("[red]No target specified[/red]")
        return
    
    console.print(f"\n[yellow]🤖 Scanning for vulnerabilities: {target}[/yellow]\n")
    
    scanner = VulnScanner()
    results = scanner.scan(target)
    
    if results:
        console.print("\n[bold green]✓ Scan Complete[/bold green]\n")
        for vuln in results:
            console.print(f"  • {vuln}")

def exploit_gen_mode():
    """AI-powered exploit generation."""
    from modules.exploit.payload_gen import PayloadGenerator
    
    console.print("\n[bold red]💀 AI Exploit Generator[/bold red]\n")
    console.print("[yellow]⚠️  For authorized testing only![/yellow]\n")
    
    table = Table(title="Available Payload Types")
    table.add_column("#", style="cyan")
    table.add_column("Type", style="white")
    table.add_column("Description", style="dim")
    
    table.add_row("1", "Reverse Shell", "Multi-language reverse shell payloads")
    table.add_row("2", "Web Shell", "PHP/ASP/JSP web shells")
    table.add_row("3", "SQL Injection", "SQLi payload generator")
    table.add_row("4", "XSS Payloads", "Cross-site scripting payloads")
    table.add_row("5", "Custom", "AI-generated custom payload")
    
    console.print(table)
    
    choice = Prompt.ask("\n[cyan]Select payload type[/cyan]", choices=["1", "2", "3", "4", "5"])
    
    gen = PayloadGenerator()
    payload = gen.generate(int(choice))
    
    if payload:
        console.print(Panel(payload, title="Generated Payload", border_style="red"))

def mitre_mode():
    """MITRE ATT&CK emulation mode."""
    from modules.mitre.attck_mapper import ATTCKMapper
    
    console.print("\n[bold red]🎭 MITRE ATT&CK Emulation[/bold red]\n")
    
    table = Table(title="Available Adversary Profiles")
    table.add_column("#", style="cyan")
    table.add_column("APT Group", style="white")
    table.add_column("Origin", style="yellow")
    table.add_column("Specialty", style="dim")
    
    table.add_row("1", "APT29 (Cozy Bear)", "Russia", "Espionage, Government targets")
    table.add_row("2", "Lazarus Group", "North Korea", "Financial, Cryptocurrency")
    table.add_row("3", "APT41", "China", "Espionage, Gaming industry")
    table.add_row("4", "FIN7", "Russia", "Financial, POS systems")
    table.add_row("5", "Custom Profile", "—", "Create your own TTPs")
    
    console.print(table)
    
    choice = Prompt.ask("\n[cyan]Select adversary profile[/cyan]", choices=["1", "2", "3", "4", "5"])
    target = Prompt.ask("[cyan]Enter target[/cyan]")
    
    mapper = ATTCKMapper()
    console.print(f"\n[yellow]🎭 Emulating {mapper.get_apt_name(int(choice))}...[/yellow]\n")
    
    results = mapper.emulate(int(choice), target)
    
    if results:
        for phase in results:
            console.print(f"  {phase}")

def report_mode():
    """Generate AI-written penetration test report."""
    from modules.reporting.ai_report import AIReportGenerator
    
    console.print("\n[bold red]📊 AI Report Generator[/bold red]\n")
    
    table = Table(title="Report Formats")
    table.add_column("#", style="cyan")
    table.add_column("Format", style="white")
    table.add_column("Description", style="dim")
    
    table.add_row("1", "JSON", "Machine-readable structured data")
    table.add_row("2", "HTML", "Professional web-based report")
    table.add_row("3", "Markdown", "GitHub-friendly documentation")
    table.add_row("4", "PDF", "Executive summary (coming soon)")
    
    console.print(table)
    
    choice = Prompt.ask("\n[cyan]Select format[/cyan]", choices=["1", "2", "3", "4"])
    
    gen = AIReportGenerator()
    report = gen.generate(int(choice))
    
    if report:
        console.print(f"\n[green]✓ Report saved to: {report}[/green]")

def settings_mode():
    """Configure MARS settings."""
    from core.ai_engine import AIEngine
    
    console.print("\n[bold red]⚙️  MARS Settings[/bold red]\n")
    
    table = Table(title="Configuration Options")
    table.add_column("#", style="cyan")
    table.add_column("Setting", style="white")
    table.add_column("Current Value", style="green")
    
    ai = AIEngine()
    
    table.add_row("1", "AI Model", ai.get_model_name() or "Not configured")
    table.add_row("2", "API Key", "••••••••" if ai.has_api_key() else "Not set")
    table.add_row("3", "Local Model", ai.get_local_model() or "None")
    table.add_row("4", "Stealth Mode", "Enabled" if ai.config.get("stealth_mode") else "Disabled")
    table.add_row("5", "Logging", "Enabled" if ai.config.get("logging") else "Disabled")
    
    console.print(table)
    
    choice = Prompt.ask("\n[cyan]Select setting to change[/cyan]", choices=["1", "2", "3", "4", "5", "back"])
    
    if choice == "1":
        ai.setup_interactive()
    elif choice == "2":
        api_key = Prompt.ask("[cyan]Enter API Key[/cyan]", password=True)
        ai.set_api_key(api_key)
        console.print("[green]✓ API Key saved[/green]")
    elif choice == "4":
        state = ai.toggle_stealth()
        console.print(f"[green]✓ Stealth Mode {'Enabled' if state else 'Disabled'}[/green]")
    elif choice == "5":
        state = ai.toggle_logging()
        console.print(f"[green]✓ Logging {'Enabled' if state else 'Disabled'}[/green]")
    elif choice == "back":
        return

def main():
    # Initialize Stealth Shield
    try:
        from core.stealth import StealthShield
        shield = StealthShield()
        if not shield.activate():
            console.print("[bold red]⚠️  ALERT: Debugger Detected! Initiating evasion protocols...[/bold red]")
            # In a real scenario, we might exit here
    except ImportError:
        pass

    parser = argparse.ArgumentParser(description="MARS - AI-Powered Red Team Automation")
    parser.add_argument("--target", "-t", help="Target domain/IP")
    parser.add_argument("--mode", "-m", choices=["recon", "vuln", "exploit", "mitre", "chat", "report"],
                       help="Operation mode")
    parser.add_argument("--ai-model", choices=["gpt-4", "claude", "ollama"], help="AI model to use")
    parser.add_argument("--no-warning", action="store_true", help="Skip legal warning")
    parser.add_argument("--apt", help="APT group to emulate")
    parser.add_argument("--output", "-o", help="Output file path")
    
    args = parser.parse_args()
    
    # Display banner
    display_banner()
    
    # Legal warning
    if not args.no_warning:
        show_legal_warning()
    
    try:
        # Command-line mode
        if args.mode:
            if args.mode == "chat":
                ai_chat_mode()
            elif args.mode == "recon":
                if not args.target:
                    console.print("[red]Error: --target required for recon mode[/red]")
                    sys.exit(1)
                from modules.osint.ai_recon import AIRecon
                recon = AIRecon()
                recon.analyze(args.target)
            elif args.mode == "vuln":
                if not args.target:
                    console.print("[red]Error: --target required for vuln mode[/red]")
                    sys.exit(1)
                from modules.osint.vuln_scanner import VulnScanner
                scanner = VulnScanner()
                scanner.scan(args.target)
            elif args.mode == "report":
                report_mode()
            elif args.mode == "mitre":
                if not args.apt or not args.target:
                    console.print("[red]Error: --apt and --target required for mitre mode[/red]")
                    sys.exit(1)
                mitre_mode() # Note: mitre_mode currently implements interactive selection, needs refactor for CLI args support if strictly following args
                # For now let's just enter interactive mitre mode 
            return
        
        # Interactive mode
        while True:
            show_main_menu()
            
            choice = Prompt.ask("[cyan]Select option[/cyan]", choices=["0", "1", "2", "3", "4", "5", "6", "7", "99"])
            
            if choice == "0":
                console.print("\n[red]Goodbye! Stay ethical. 🔴[/red]\n")
                break
            elif choice == "1":
                reconnaissance_mode()
            elif choice == "2":
                vuln_scan_mode()
            elif choice == "3":
                exploit_gen_mode()
            elif choice == "4":
                mitre_mode()
            elif choice == "5":
                ai_chat_mode()
            elif choice == "6":
                report_mode()
            elif choice == "7":
                settings_mode()
            elif choice == "99":
                if Confirm.ask("[bold red]ARE YOU SURE? This will delete all logs and config![/bold red]"):
                    shield.emergency_cleanup()

    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user.[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]💥 CRITICAL ERROR: {str(e)}[/bold red]")
        console.print("[dim]MARS has encountered an anomaly but remains operational.[/dim]")
        # Log error to encrypted log (simulated)

