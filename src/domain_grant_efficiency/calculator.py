


#ooh splash screen?
#do the typewriter effect
#print("Welcome to domain effeciency counter: Calculate how many $10 domain grants you should buy for maximum (efficient) money use.")
#cost_first_year = input("Enter how much it will cost in total for the first year, including all taxes & fees, like the ICANN registration fee:")
#make sure valid input
# if cost first year and recurring are both higher than that of spaceship, recocmend spaceship to them or porkbun or someone cheap
# guide to domain buying for bang for buck or cheapest?
import math


def nearest_ten(number):
    return round(number / 10) * 10

def nearest_ten_round_up(number):
    return math.ceil(number / 10) * 10
    # example: number = 67; math.ceil(67/10) * 10 --> math.ceil(6.7) * 10 --> 7 * 10 --> 70

def find_deviation(cost_first_year, num_first_year, cost_recurring_year, num_recurring_year):
    total_cost = cost_first_year * num_first_year + cost_recurring_year * num_recurring_year
    grant_money = nearest_ten(total_cost)
    return grant_money - total_cost
    # examples:
    # Get $20 from grants, need $18; 20 - 18 = +2 ($2 left over / overage)
    # Get $20 from grants, need $22; 20 - 22 = -2 ($2 short)
    # Get $20 from grants, need $20; 20 - 20 = 0 (perfect!)

# no $N short w/ this
def left_over(cost_first_year, num_first_year, cost_recurring_year, num_recurring_year):
    total_cost = cost_first_year * num_first_year + cost_recurring_year * num_recurring_year
    grant_money_required = nearest_ten_round_up(total_cost)
    return grant_money_required - total_cost # this is the overage



#maybe graph this
# green for efficient, yellow for mid, red for very inefficient (ex: 1 cent short)