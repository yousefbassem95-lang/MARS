"""
MITRE ATT&CK Framework Mapper and Emulator
"""

import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree

console = Console()

class ATTCKMapper:
    """MITRE ATT&CK framework integration for adversary emulation."""
    
    def __init__(self):
        self.apt_profiles = {
            1: {
                "name": "APT29 (Cozy Bear)",
                "origin": "Russia",
                "description": "Russian state-sponsored group focused on espionage",
                "techniques": [
                    {"id": "T1566.001", "name": "Spearphishing Attachment", "phase": "Initial Access"},
                    {"id": "T1059.001", "name": "PowerShell", "phase": "Execution"},
                    {"id": "T1547.001", "name": "Registry Run Keys", "phase": "Persistence"},
                    {"id": "T1027", "name": "Obfuscated Files", "phase": "Defense Evasion"},
                    {"id": "T1003.001", "name": "LSASS Memory", "phase": "Credential Access"},
                    {"id": "T1021.002", "name": "SMB/Windows Admin Shares", "phase": "Lateral Movement"},
                    {"id": "T1560.001", "name": "Archive via Utility", "phase": "Collection"},
                    {"id": "T1041", "name": "Exfiltration Over C2", "phase": "Exfiltration"}
                ]
            },
            2: {
                "name": "Lazarus Group",
                "origin": "North Korea",
                "description": "North Korean state-sponsored group targeting financial institutions",
                "techniques": [
                    {"id": "T1566.001", "name": "Spearphishing Attachment", "phase": "Initial Access"},
                    {"id": "T1204.002", "name": "Malicious File", "phase": "Execution"},
                    {"id": "T1543.003", "name": "Windows Service", "phase": "Persistence"},
                    {"id": "T1140", "name": "Deobfuscate/Decode", "phase": "Defense Evasion"},
                    {"id": "T1552.001", "name": "Credentials In Files", "phase": "Credential Access"},
                    {"id": "T1570", "name": "Lateral Tool Transfer", "phase": "Lateral Movement"},
                    {"id": "T1005", "name": "Data from Local System", "phase": "Collection"},
                    {"id": "T1567.002", "name": "Exfiltration to Cloud Storage", "phase": "Exfiltration"}
                ]
            },
            3: {
                "name": "APT41",
                "origin": "China",
                "description": "Chinese state-sponsored group with dual espionage and financial motives",
                "techniques": [
                    {"id": "T1190", "name": "Exploit Public-Facing Application", "phase": "Initial Access"},
                    {"id": "T1059.003", "name": "Windows Command Shell", "phase": "Execution"},
                    {"id": "T1505.003", "name": "Web Shell", "phase": "Persistence"},
                    {"id": "T1036.005", "name": "Match Legitimate Name", "phase": "Defense Evasion"},
                    {"id": "T1003.001", "name": "LSASS Memory", "phase": "Credential Access"},
                    {"id": "T1021.001", "name": "Remote Desktop Protocol", "phase": "Lateral Movement"},
                    {"id": "T1213", "name": "Data from Information Repositories", "phase": "Collection"},
                    {"id": "T1048.003", "name": "Exfiltration Over Unencrypted Protocol", "phase": "Exfiltration"}
                ]
            },
            4: {
                "name": "FIN7",
                "origin": "Russia",
                "description": "Financially motivated group targeting retail and hospitality",
                "techniques": [
                    {"id": "T1566.001", "name": "Spearphishing Attachment", "phase": "Initial Access"},
                    {"id": "T1059.005", "name": "Visual Basic", "phase": "Execution"},
                    {"id": "T1053.005", "name": "Scheduled Task", "phase": "Persistence"},
                    {"id": "T1055.001", "name": "DLL Injection", "phase": "Defense Evasion"},
                    {"id": "T1056.001", "name": "Keylogging", "phase": "Credential Access"},
                    {"id": "T1021.001", "name": "Remote Desktop Protocol", "phase": "Lateral Movement"},
                    {"id": "T1125", "name": "Video Capture", "phase": "Collection"},
                    {"id": "T1041", "name": "Exfiltration Over C2", "phase": "Exfiltration"}
                ]
            },
            5: {
                "name": "Custom Profile",
                "origin": "Custom",
                "description": "User-defined adversary profile",
                "techniques": []
            }
        }
    
    def get_apt_name(self, choice):
        """Get APT name by choice number."""
        return self.apt_profiles.get(choice, {}).get("name", "Unknown")
    
    def emulate(self, apt_choice, target):
        """Emulate APT group techniques."""
        
        apt = self.apt_profiles.get(apt_choice)
        
        if not apt:
            console.print("[red]Invalid APT selection[/red]")
            return None
        
        if apt_choice == 5:
            return self._custom_emulation(target)
        
        console.print(f"\n[bold red]🎭 Emulating: {apt['name']}[/bold red]")
        console.print(f"[dim]Origin: {apt['origin']}[/dim]")
        console.print(f"[dim]{apt['description']}[/dim]\n")
        
        # Display attack phases
        tree = Tree(f"[bold red]🎯 Attack Campaign: {target}[/bold red]")
        
        phases = {}
        for tech in apt['techniques']:
            phase = tech['phase']
            if phase not in phases:
                phases[phase] = tree.add(f"[bold yellow]{phase}[/bold yellow]")
            
            phases[phase].add(f"[green]{tech['id']}[/green] - {tech['name']}")
        
        console.print(tree)
        
        # Detailed execution plan
        results = self._generate_execution_plan(apt, target)
        
        return results
    
    def _generate_execution_plan(self, apt, target):
        """Generate detailed execution plan using AI."""
        
        console.print("\n[bold yellow]🤖 AI-Generated Execution Plan:[/bold yellow]\n")
        
        from core.ai_engine import AIEngine
        ai = AIEngine()
        
        techniques_str = "\n".join([
            f"- {t['id']}: {t['name']} ({t['phase']})" 
            for t in apt['techniques']
        ])
        
        prompt = f"""You are emulating {apt['name']} APT group against target: {target}

Their known techniques:
{techniques_str}

Generate a detailed attack plan that:
1. Describes each phase of the attack
2. Provides specific commands/tools for each technique
3. Explains how to chain techniques together
4. Includes detection evasion strategies
5. Maps to real-world scenarios

Be specific and actionable. This is for authorized red team exercises."""
        
        response = ai.chat(prompt)
        console.print(response)
        
        # Return execution summary
        return [
            f"✓ Phase: {t['phase']} - {t['id']}: {t['name']}"
            for t in apt['techniques']
        ]
    
    def _custom_emulation(self, target):
        """Custom adversary emulation with user-defined TTPs."""
        
        from rich.prompt import Prompt
        
        console.print("\n[bold cyan]Custom Adversary Profile[/bold cyan]\n")
        
        # Select techniques
        console.print("[dim]Available ATT&CK Tactics:[/dim]")
        tactics = [
            "Initial Access", "Execution", "Persistence", "Privilege Escalation",
            "Defense Evasion", "Credential Access", "Discovery", "Lateral Movement",
            "Collection", "Exfiltration", "Impact"
        ]
        
        for i, tactic in enumerate(tactics, 1):
            console.print(f"  [{i}] {tactic}")
        
        console.print("\n[dim]Enter technique IDs (e.g., T1566.001) separated by commas:[/dim]")
        techniques = Prompt.ask("[cyan]Techniques[/cyan]")
        
        if not techniques:
            console.print("[yellow]No techniques specified[/yellow]")
            return None
        
        # Generate AI-powered emulation
        from core.ai_engine import AIEngine
        ai = AIEngine()
        
        prompt = f"""Create a custom adversary emulation plan for target: {target}

The adversary uses these MITRE ATT&CK techniques: {techniques}

Provide:
1. Attack narrative explaining the adversary's goals
2. Step-by-step execution plan for each technique
3. Specific tools and commands
4. Detection opportunities for blue team
5. Recommended mitigations

Make it realistic and actionable for purple team exercises."""
        
        console.print("\n[dim]🤖 Generating custom attack plan...[/dim]\n")
        
        response = ai.chat(prompt)
        console.print(response)
        
        return [f"Custom emulation for techniques: {techniques}"]
    
    def get_technique_details(self, technique_id):
        """Get details for a specific ATT&CK technique."""
        
        from core.ai_engine import AIEngine
        ai = AIEngine()
        
        prompt = f"""Provide detailed information about MITRE ATT&CK technique {technique_id}:

Include:
1. Full name and description
2. Procedure examples (real-world APT usage)
3. Detection methods
4. Mitigation strategies
5. Example attack commands/scripts

Be comprehensive and technical."""
        
        return ai.chat(prompt)
    
    def generate_detection_rules(self, techniques):
        """Generate detection rules for specified techniques."""
        
        from core.ai_engine import AIEngine
        ai = AIEngine()
        
        prompt = f"""Generate detection rules for these MITRE ATT&CK techniques:
{techniques}

Provide:
1. Sigma rules
2. YARA rules (if applicable)
3. Splunk queries
4. Windows Event IDs to monitor
5. Key indicators of compromise (IOCs)

Make rules specific and actionable for SOC analysts."""
        
        return ai.chat(prompt)
