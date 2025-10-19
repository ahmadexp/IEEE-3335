"""IEEE-3335 Tools package."""

import shutil
from rich.console import Console

# Single shared console instance
terminal_width = shutil.get_terminal_size().columns
console = Console(width=max(terminal_width, 100))