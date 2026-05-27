import time

from rich.console import Console
from rich.panel import Panel
from rich.align import Align

from domain_grant_efficiency.main import calculate_optimizations_flexible

console = Console()

SPLASH = r"""
██████╗   ██████╗  ███╗   ███╗  █████╗  ██╗ ███╗   ██╗
██╔══██╗ ██╔═══██╗ ████╗ ████║ ██╔══██╗ ██║ ████╗  ██║
██║  ██║ ██║   ██║ ██╔████╔██║ ███████║ ██║ ██╔██╗ ██║
██║  ██║ ██║   ██║ ██║╚██╔╝██║ ██╔══██║ ██║ ██║╚██╗██║
██████╔╝ ╚██████╔╝ ██║ ╚═╝ ██║ ██║  ██║ ██║ ██║ ╚████║
╚═════╝   ╚═════╝  ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═══╝

███████╗ ███████╗ ███████╗ ██╗  ██████╗ ██╗ ███████╗ ███╗   ██╗  ██████╗ ██╗   ██╗
██╔════╝ ██╔════╝ ██╔════╝ ██║ ██╔════╝ ██║ ██╔════╝ ████╗  ██║ ██╔════╝ ╚██╗ ██╔╝
█████╗   █████╗   █████╗   ██║ ██║      ██║ █████╗   ██╔██╗ ██║ ██║       ╚████╔╝ 
██╔══╝   ██╔══╝   ██╔══╝   ██║ ██║      ██║ ██╔══╝   ██║╚██╗██║ ██║        ╚██╔╝  
███████╗ ██║      ██║      ██║ ╚██████╗ ██║ ███████╗ ██║ ╚████║ ╚██████╗    ██║   
╚══════╝ ╚═╝      ╚═╝      ╚═╝  ╚═════╝ ╚═╝ ╚══════╝ ╚═╝  ╚═══╝  ╚═════╝    ╚═╝   

 ██████╗  █████╗  ██╗      ██████╗ ██╗   ██╗ ██╗       █████╗  ████████╗  ██████╗  ██████╗ 
██╔════╝ ██╔══██╗ ██║     ██╔════╝ ██║   ██║ ██║      ██╔══██╗ ╚══██╔══╝ ██╔═══██╗ ██╔══██╗
██║      ███████║ ██║     ██║      ██║   ██║ ██║      ███████║    ██║    ██║   ██║ ██████╔╝
██║      ██╔══██║ ██║     ██║      ██║   ██║ ██║      ██╔══██║    ██║    ██║   ██║ ██╔══██╗
╚██████╗ ██║  ██║ ███████╗╚██████╗ ╚██████╔╝ ███████╗ ██║  ██║    ██║    ╚██████╔╝ ██║  ██║
 ╚═════╝ ╚═╝  ╚═╝ ╚══════╝ ╚═════╝  ╚═════╝  ╚══════╝ ╚═╝  ╚═╝    ╚═╝     ╚═════╝  ╚═╝  ╚═╝
"""

def show_splash():
    panel = Panel(
        Align.center(SPLASH),
        border_style="bright_cyan",
        padding=(1, 2),
    )

    console.print()
    console.print(panel)
    time.sleep(0.5)
    console.print()
    time.sleep(0.5)

def typewriter(text, delay):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)

def loading_dots(text, delay):
    dots = [".", "..", "..."]
    for item in dots:
        print(f"\r{text} {item:<3}", end="", flush=True)
        # item:<3 makes every dot item 3 spaces wide
        time.sleep(delay)

def show_welcome():
    loading_dots("Loading the advanced graphing calculator")
    time.sleep(1)
    typewriter("Use this calculator to maximize efficient use of $10 domain grants!", 0.03)
    time.sleep(1)
    console.print("[dim italic]Enter the following values to begin your calculations[/dim italic]")
    time.sleep(0.5)

def horizontal_bar_chart(data, width, label_width):
    optimizations_flexible = calculate_optimizations_flexible()
    max_value = max(data.values())

    for key, value in data.items():
        percent_of_max = value / max_value
        bar_length = round(percent_of_max * width)
        bar = "█" * bar_length
        
    
