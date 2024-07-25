# PROGRAM REQUIREMENTS

# FIXME Revise the coin procesor and add a function for establish the correct number with refund is processed

# TODO Revise all fuctions and optimize. 1 Fuctión 1 Task

import os
from re import match
from coffee_data import *



print("\n")

def user_input_coffee_select_validator():
    """
    Prompts the user for an input of 'espresso', 'latte', 'cappuccino', 'report', or 'off' and returns the corresponding string based on the response.

    Returns:
        str: The input provided by the user, which can be 'espresso', 'latte', 'cappuccino', 'report', or 'off'.

    Example:
        >>> user_input_coffee_select_validator()
        What would you like? (espresso/latte/cappuccino): espresso
        'espresso'

        >>> user_input_coffee_select_validator()
        What would you like? (espresso/latte/cappuccino): latte
        'latte'

    Notes:
        - The function will continue to prompt for input until the user provides a valid response ('espresso', 'latte', 'cappuccino', 'report', or 'off').
        - The input is case insensitive, so 'ESPRESSO', 'LATTE', 'CAPPUCCINO', 'REPORT', and 'OFF' are also valid inputs.
        - Any other input will prompt the user to try again until a valid response is provided.
        - The options 'report' and 'off' are hidden from normal users and are only available to maintenance staff.
    """
    
    while True:
        print("\n")
        
        text = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

        if text in ["espresso", "latte", "cappuccino", "report", "off"]:
            print(f"Selected {text}")
            print("\n")
            return text
        else:
            print("\n")
            print("Please, select correctly.")

           
def user_input_coin_select_validator(text_input: str):
    """
    Prompts the user to insert coins and validates the input. The function will return the amount entered as an integer.

    Args:
        text_input (str): The message to display to the user when requesting input.

    Returns:
        int: The amount of coins inserted by the user. Returns 0 if the user does not input any value.

    Example:
        >>> user_input_coin_select_validator("Please insert coins: ")
        Please insert coins: 100
        100

        >>> user_input_coin_select_validator("Please insert coins: ")
        Please insert coins: 
        0

    Notes:
        - The function will continue to prompt for input until the user provides a valid response (an integer between 0 and 9999).
        - If the input is an empty string, the function will return 0.
        - The input is expected to be a string that can be converted to an integer.
    """
    
    while True:
        print("\n")
        print("Please insert coins.")
        
        text = input(text_input).strip()

        if text == "":
            return 0
        
        elif match(r"^[0-9]{1,4}$", text):
            text = int(text)
            return text

        else:
            print("\n")
            print("Invalid input. Please insert a valid amount (0-9999).")


def user_input_yn(text_input: str):
    """
    Prompts the user for a yes or no input and returns a boolean value based on the response.

    Args:
        text_input (str): The message to display to the user when requesting input.

    Returns:
        bool: True if the user inputs 'y' or 'yes', False if the user inputs 'n' or 'no'.

    Example:
        >>> user_input_yn("Do you want to continue? (y/n): ")
        Do you want to continue? (y/n): y
        True

        >>> user_input_yn("Do you want to continue? (y/n): ")
        Do you want to continue? (y/n): no
        False

    Notes:
        - The function will continue to prompt for input until the user provides a valid response ('y', 'yes', 'n', or 'no').
        - The input is case insensitive, so 'Y', 'YES', 'N', and 'NO' are all valid inputs.
        - Any other input will prompt the user to try again until a valid response is provided.
    """
    
    while True:
        text = input(text_input).lower()
        
        if text in ["n", "no"]:
            return False
            
        elif text in ["y", "yes"]:
            return True

        else:
            print("Please, only 'y' or 'n'.")

            
def coin_processor(coffee: str, menu: dict, cash_register: dict):
    """
    Processes the coins inserted by the user for a coffee purchase and updates the cash register.

    Args:
        coffee (str): The type of coffee selected by the user.
        menu (dict): A dictionary containing the menu items and their prices.
        cash_register (dict): A dictionary representing the current state of the cash register with counts of each coin type.

    Returns:
        tuple: A tuple containing:
            - bool: True if the payment is successful, False otherwise.
            - float: The total amount of money inserted by the user.
            - float: The refund amount to be given back to the user if any.
            - dict: The updated cash register with the new counts of each coin type.

    Example:
        >>> menu = {'espresso': {'cost': 1.5}, 'latte': {'cost': 2.5}, 'cappuccino': {'cost': 3.0}}
        >>> cash_register = {'quarters': 50, 'dimes': 50, 'nickles': 50, 'pennies': 50}
        >>> coin_processor('espresso', menu, cash_register)
        how many quarters? ($0.25) : 4
        how many dimes? ($0.10) : 0
        how many nickles? ($0.05) : 0
        how many pennies? ($0.01) : 0
        (True, 1.0, 0.25, {'quarters': 54, 'dimes': 50, 'nickles': 50, 'pennies': 50})

    Notes:
        - The function will prompt the user to input the number of each type of coin they are inserting.
        - If the total amount of inserted coins is less than the cost of the selected coffee, the user will be refunded.
        - If the total amount of inserted coins is equal to or greater than the cost of the selected coffee, the cash register will be updated, and any excess amount will be refunded to the user.
    """
    
    quarters=  user_input_coin_select_validator("how many quarters? ($0.25) : ")
    dimes = user_input_coin_select_validator("how many dimes? ($0.10) : ")
    nickles =user_input_coin_select_validator("how many nickles? ($0.05) : ")
    pennies = user_input_coin_select_validator("how many pennies? ($0.01) : ")
    
    total_coin = round((
                (quarters*0.25) + 
                (dimes*0.1)      + 
                (nickles*0.05)  + 
                (pennies*0.01)), 
                2
    )
    
    if total_coin < menu[coffee]["cost"]:
       
        print("\n")
        print("Sorry that's not enough money. Money refunded.")
        
        print(f"""
        Refundend 
    {quarters} x Quarters
    {dimes} x Dimes
    {nickles} x Nickles
    {pennies} x Pennies
        """)
        
        print("\n")
        
        return False
    
    elif total_coin >= menu[coffee]["cost"]:
        refund = round(total_coin - menu[coffee]["cost"], 2)
        cash_register["quarters"] += quarters
        cash_register["dimes"] += dimes
        cash_register["nickles"] += nickles
        cash_register["pennies"] += pennies
    
        return True, total_coin, refund, cash_register

def report(resources: dict, cash_register: dict):
    
    """
    Prints a report of the current resources and total cash in the cash register.

    Args:
        resources (dict): A dictionary containing the current amount of each resource (e.g., water, milk, coffee).
        cash_register (dict): A dictionary representing the current state of the cash register with counts of each coin type.

    Example:
        >>> resources = {'water': 500, 'milk': 300, 'coffee': 200}
        >>> cash_register = {'quarters': 50, 'dimes': 50, 'nickles': 50, 'pennies': 50}
        >>> report(resources, cash_register)
        water: 500 ml
        milk: 300 ml
        coffee: 200 ml
        money: $20.50

    Notes:
        - The function calculates the total cash in the register based on the counts of each type of coin.
        - The report includes the amount of each resource in milliliters and the total cash in dollars.
    """
    
    for key, value in resources.items():
        print(f"{key.capitalize()}: {value}ml")
    
    total_cash = (
        (cash_register["quarters"]*0.25) + 
        (cash_register["dimes"]*0.1) + 
        (cash_register["nickles"]*0.05) + 
        (cash_register["pennies"]*0.01)
    )

    print(f"money:  ${total_cash:.2f}")
    
def make_coffee(coffee: str, resources: dict):
    """
    Prepares a coffee beverage if sufficient resources are available and updates the resources. 

    Args:
        coffee (str): The type of coffee to make (e.g., 'espresso', 'latte', 'cappuccino').
        resources (dict): A dictionary representing the current available resources (e.g., 'water', 'milk', 'coffee').
        cash_register (dict): A dictionary representing the current state of the cash register with counts of each coin type.

    Returns:
        tuple: A tuple containing two elements:
            - A dictionary representing the updated resources after making the coffee.
            - The cash register dictionary, unchanged.

    Example:
        >>> resources = {'water': 500, 'milk': 300, 'coffee': 200}
        >>> cash_register = {'quarters': 10, 'dimes': 10, 'nickles': 10, 'pennies': 10}
        >>> make_coffee('latte', resources, cash_register)
        ({'water': 400, 'milk': 200, 'coffee': 200}, {'quarters': 10, 'dimes': 10, 'nickles': 10, 'pennies': 10})

    Notes:
        - The function checks if there are enough resources to make the selected coffee.
        - If any resource is insufficient, an error message is printed and the coffee is not made.
        - The function updates the resource quantities based on the ingredients required for the selected coffee.
        - The cash register is returned unchanged.
    """
    
    if MENU[coffee]:
        
        for key, value in MENU[coffee]["ingredients"].items():

            if resources[key] < MENU[coffee]["ingredients"][key]:
                print(f"Sorry there is not enough {key}")
                
                
            elif resources[key] >= MENU[coffee]["ingredients"][key]:
                resources[key] -= MENU[coffee]["ingredients"][key]
                
        return resources, cash_register

def check_resources(coffee: str, resources: dict) -> bool:
    """
    Checks if there are sufficient resources available to make the selected coffee.

    Args:
        coffee (str): The type of coffee to check (e.g., 'espresso', 'latte', 'cappuccino').
        resources (dict): A dictionary representing the current available resources (e.g., 'water', 'milk', 'coffee').

    Returns:
        bool: True if there are enough resources to make the selected coffee, False otherwise.

    Example:
        >>> resources = {'water': 500, 'milk': 300, 'coffee': 200}
        >>> check_resources('latte', resources)
        True

        >>> resources = {'water': 200, 'milk': 300, 'coffee': 200}
        >>> check_resources('latte', resources)
        False

    Notes:
        - The function checks if all required ingredients for the selected coffee are available in the required quantities.
        - If any resource is insufficient, an error message is printed and the function returns False.
        - If all resources are sufficient, the function returns True.
    """
    
    if MENU[coffee]:
        for key, value in MENU[coffee]["ingredients"].items():
            if resources[key] < MENU[coffee]["ingredients"][key]:
                print(f"Sorry there is not enough {key}")
                return False
                
# def refund():
#     print("")

# def check_user_cash():
#     print("")

# def total_resources():
#     print("")

while True:
    
    #os.system('cls')
    
    text = user_input_coffee_select_validator()
    
    if text in ["espresso", "latte", "cappuccino"]:
        
        if check_resources(text, resources) == False:
            break
        
        elif check_resources(text, resources) != False:
            
            if user_input_yn(f"The price of selection is ${MENU[text]["cost"]}, do you agree?: ") == True:
        
                coins = coin_processor(text, MENU, cash_register)
                
                if coins == False:
                    continue
                
                elif coins[0] == True:
                    cash_register == coins[3]
                    make_coffee(text, resources)
                    print(f"Total amount is {coins[1]}")
                    print(f"Your refund is {coins[2]}")
                
        
            
    
    elif  text == "report":
        report(resources, cash_register)
        print("\n")
        text = user_input_yn("Go to user mode? ")
        if text == False:
            break
    
    elif text == "off":
        print("\n")
        print("Maintenance mode: Shutting down the system")
        break
    
    
        













