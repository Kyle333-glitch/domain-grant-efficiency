from rich.console import Console
from rich.panel import Table

from domain_grant_efficiency.ui import show_splash, show_welcome

console = Console()

def main():
    show_splash()
    show_welcome()

    while True:
        cost_first_year = input("The cost of your domain for the first year: ")
        num_first_year = input("The number of domains you will be buying at the first year cost: ")
        cost_recurring_year = input("The renewal cost of your domain (years after the first): ")
        num_recurring_year = input("The number of domains you will be buying at the renewal cost: ")

        table = Table(title="Your choices", border_style="bright_cyan")
        table.add_column("Value", style="bold")
        table.add_column("Input", style="green")

        table.add_row("First year cost", f"${cost_first_year}")
        table.add_row("Number of first year domains", f"${num_first_year}")
        table.add_row("Renewal year cost", f"${cost_recurring_year}")
        table.add_row("Number of renewal year domains", f"${num_recurring_year}")

        console.print(table)

        print()

        confirm_choices = input("Confirm these choices? Enter y to continue or anything else to change your selections: ")
        if confirm_choices.lower() == "y":
            break


    