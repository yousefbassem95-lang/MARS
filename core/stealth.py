"""
MARS Stealth Shield - Anti-Analysis & Self-Protection
"""

import sys
import os
import time
import psutil
import platform
import random
from rich.console import Console

console = Console()

class StealthShield:
    """Proactive defense mechanisms for MARS."""
    
    def __init__(self):
        self.paranoid_mode = False
    
    def activate(self):
        """Activate stealth checks."""
        if self._check_debugger():
            return False
        
        if self._check_virtualization():
            # In paranoid mode, we might exit. For now, just warn/log.
            pass
            
        self._obfuscate_process()
        return True

    def _check_debugger(self):
        """Check for active debuggers."""
        # Method 1: sys.gettrace
        if sys.gettrace() is not None:
            return True
            
        # Method 2: Parent process check (basic)
        try:
            parent = psutil.Process(os.getppid())
            suspicious_parents = ['gdb', 'ida', 'radare2', 'strace', 'ltrace']
            if any(p in parent.name().lower() for p in suspicious_parents):
                return True
        except:
            pass
            
        return False

    def _check_virtualization(self):
        """Check for virtualization/sandbox artifacts."""
        # Basic check - looking for common VM MAC addresses or files
        # (Simplified for Python portability)
        try:
            if platform.system() == "Linux":
                with open('/proc/cpuinfo', 'r') as f:
                    if 'hypervisor' in f.read().lower():
                        return True
        except:
            pass
        return False

    def _obfuscate_process(self):
        """Attempt to disguise the process name."""
        try:
            # Simple process renaming if setproctitle is installed
            try:
                import setproctitle
                # Fake common daemon names
                fake_names = ['systemd-journald', 'kworker/u4:0', 'apache2', 'nginx']
                setproctitle.setproctitle(random.choice(fake_names))
            except ImportError:
                pass
        except:
            pass

    def emergency_cleanup(self):
        """Perform emergency cleanup of logs and artifacts."""
        console.print("[bold red]\n💥 INITIATING EMERGENCY DESTRUCT SEQUENCE 💥[/bold red]")
        
        paths_to_nuke = [
            "logs/",
            "config/ai_config.json",
            "__pycache__/",
            "generated_payloads/"
        ]
        
        for path in paths_to_nuke:
            if os.path.exists(path):
                try:
                    if os.path.isdir(path):
                        import shutil
                        shutil.rmtree(path)
                    else:
                        os.remove(path)
                    console.print(f"[dim]Nuked {path}[/dim]")
                except:
                    pass
        
        console.print("[bold red]Cleanup Complete. MARS Ghost Protocol Active.[/bold red]")
        sys.exit(0)

    def secure_input(self, prompt_text):
        """Securely get input ensuring it's not logged elsewhere if possible."""
        from rich.prompt import Prompt
        return Prompt.ask(prompt_text, password=True)
