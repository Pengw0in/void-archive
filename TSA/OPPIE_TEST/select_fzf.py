import subprocess
from typing import Optional, List

def select_result(results: List[str], prompt: str = "Select video:") -> Optional[str]:
    if not results:
        return None

    try:
        fzf = subprocess.run(
            ["fzf", "--prompt", f"{prompt}"],
            input = "\n".join(results),
            capture_output= True,
            text= True
        )
        return fzf.stdout.strip() if fzf.returncode == 0 else None
    except FileNotFoundError:
        print("Error: fzf is not installed or not found in PATH.")
        return None
