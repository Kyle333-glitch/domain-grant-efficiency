from rich.console import Console
from rich.table import Table
from InquirerPy import inquirer

from domain_grant_efficiency.ui import show_splash, show_welcome, loading_dots, typewriter
from domain_grant_efficiency.calculator import nearest_ten_round_up, nearest_ten, find_deviation


console = Console()

def confirm_choices(cost_first_year, num_first_year, cost_recurring_year, num_recurring_year):
    table = Table(title="Your choices", border_style="bright_cyan")

    table.add_column("Value", style="bold")
    table.add_column("Input", style="green")

    table.add_row("First year cost", f"${cost_first_year}")
    table.add_row("Number of first year domains", f"${num_first_year}")
    table.add_row("Renewal year cost", f"${cost_recurring_year}")
    table.add_row("Number of renewal year domains", f"${num_recurring_year}")

    console.print(table)


    confirm_choice = inquirer.select(
            message="Confirm these choices?",
            choices=[
                {"name": "Yes, these are correct", "value": True},
                {"name": "No, I want to change my selections", "value": False}
            ],
            pointer=">",
        ).execute()

    if confirm_choice:
        console.print("[green]Choices confirmed![/green]")
        return True
    
    return False

def change_choices(cost_first_year, num_first_year, cost_recurring_year, num_recurring_year):
    choices = [cost_first_year, num_first_year, cost_recurring_year, num_recurring_year]

    edit_which = inquirer.checkbox(
            message="Which of these would you like to change?",
            choices=[
                "First year cost",
                "Number of first year domains",
                "Renewal year cost",
                "Number of renewal year domains",
            ],
            pointer=">",
        ).execute()

    if not edit_which:
        console.print("[red]Choice changing canceled.[/red]")

    if "First year cost" in edit_which:
        cost_first_year = input("The cost of your domain for the first year: ")
    if "Number of first year domains" in edit_which:
        num_first_year = input("The number of domains you will be buying at the first year cost: ")
    if "Renewal year cost" in edit_which:
        cost_recurring_year = input("The renewal cost of your domain (for years after the first): ")
    if "Number of renewal year domains" in edit_which:
        num_recurring_year = input("The number of domains you will be buying at the renewal cost: ")

    return choices

def get_essential_info():
    cost_first_year = input("The cost of your domain for the first year: ")
    num_first_year = input("The number of domains you will be buying at the first year cost: ")
    cost_recurring_year = input("The renewal cost of your domain (for years after the first): ")
    num_recurring_year = input("The number of domains you will be buying at the renewal cost: ")

    while True:
        choice_confirmation = confirm_choices(cost_first_year, num_first_year, cost_recurring_year, num_recurring_year)
        if choice_confirmation:
            break
        else:
            change_choices(cost_first_year, num_first_year, cost_recurring_year, num_recurring_year)
    
    return [cost_first_year, num_first_year, cost_recurring_year, num_recurring_year]

def calculate_optimizations_no_flexibility():
    loading_dots("Maximizing efficiency and optimizing")
    no_spend_money_required = nearest_ten_round_up(total_cost)
    console.print(f"If you don't want to spend any of your own money, you'll need ${no_spend_money_required / 10} $10 grants or ${no_spend_money_required} dollars")
    min_excess_money_required = nearest_ten(total_cost)
    console.print(f"If you just want to minimize excess, we reccomend ${min_excess_money_required / 10} $10 grants or ${min_excess_money_required} dollars")
    deviation = find_deviation(total_cost)
    if deviation > 0:
        console.print(f"You would end up with ${deviation} left over.")
    elif deviation < 0:
        console.print(f"You would end up spending ${deviation} of your own money.")
    else:
        console.print("You would end up with the perfect amount to pay for your domains.")

def main():
    show_splash()
    show_welcome()

    essential_info = get_essential_info()

    cost_first_year = essential_info[0]
    num_first_year = essential_info[1]
    cost_recurring_year = essential_info[2]
    num_recurring_year = essential_info[3]

    console.print("[green]Initial config complete![\green]")

    loading_dots("Calculating total cost")
    total_cost = cost_first_year * num_first_year + cost_recurring_year + num_recurring_year
    typewriter(f"Total cost is: ${total_cost}")

    flexible = inquirer.select(
            message=f"Are you sure that you will have exactly ${num_first_year} first-year domains and exactly ${num_recurring_year} domains?",
            choices=[
                {"name": "Yes, I am sure.", "value": False},
                {"name": "No, I'm planning on around those numbers, but I'm flexible.", "value": True}
            ],
            pointer=">",
        ).execute()

    if not flexible:
        calculate_optimizations_no_flexibility()
    else:
        console.print(f"Assuming you will have exactly ${num_first_year} first-year domains and exactly ${num_recurring_year} domains:")
        calculate_optimizations_no_flexibility()
        console.print("To see how you can optimize:")



    





        

        




    