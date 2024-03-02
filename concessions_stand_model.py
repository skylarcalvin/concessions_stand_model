'''
This module models a typical booster club consessions stand, and provides some basic cost and profit analysis.
It is assumed that rent, labor_cost, and utilities are all covered by the school and therefore are zero.

First The expenses and income sources are predefined.
'''

# Initial parameter values.

## Expenses ##
# Product expenses per serving.
soda_fountain_cost = 0.40
soda_bottle_cost = 0.60
water_cost = 0.25
juice_cost = 0.5
body_armor_cost = .8
hotdog_cost = 0.30
bun_cost = 0.10
candy_cost = 0.50
chip_cost = 0.25
popcorn_kernel_cost = 0.08
oil_cost = 0.10
salt_cost = 0.06
pickle_cost = 0.30
nacho_chips_cost = 0.75
nacho_cheese_cost = 0.30
pizza_slice_cost = 1
jalepeno_cost = 0.08
condiments_cost = 0.08

# Business_Expenses:
labor_rate = 20

## Income ##
# Price per serving.
soda_fountain_price = 3
soda_bottle_price = 3
water_price = 2
juice_price = 2
body_armor_price = 3
hotdog_price = 2
candy_price = 1
chip_price = 1
popcorn_price = 3
pickle_price = 1
nacho_price = 2
pizza_slice_price = 2

# Quantities

# Number of servings per event.
soda_fountain_servings = 100
soda_bottles = 60
waters = 60
juices = 10
body_armors = 50
hotdogs = 50
candies = 30
chips = 20
popcorns = 120
pickles = 12
nachos = 30
pizza_slices = 50

# Hours open.
hours_open = 3

# Function to display menu.
def display_menu():
    '''
    Function displays the menu with the current parameter values.
    '''

    # Print out the menu.
    print(
        f'''
Expenses:

Product cost:
1. Cost of a fountain drink per serving: {soda_fountain_cost}
2. Cost of a soda bottle:                {soda_bottle_cost}
3. Cost of a water:                      {water_cost}
4. Cost of a juice:                      {juice_cost}
5. Cost of a body armor:                 {body_armor_cost}
6. Cost of a hotdog:                     {hotdog_cost}
7. Cost of a bun:                        {bun_cost}
8. Cost of a candy:                      {candy_cost}
9. Cost of a bag of chips:               {chip_cost}
10. Cost of a batch of popcorn kernels:  {popcorn_kernel_cost}
11. Cost of a batch of popcorn oil:      {oil_cost}
12. Cost of a batch of salt:             {salt_cost}
13. Cost of a pickle:                    {pickle_cost}
14. Cost of a batch of nacho chips:      {nacho_chips_cost}
15. Cost of a batch of nacho cheese:     {nacho_cheese_cost}
16. Cost of a pizza slice:               {pizza_slice_cost}
17. Cost of a serving of japenos:        {jalepeno_cost}
18. Cost of a serving of condiments      {condiments_cost}

Business_Expenses:
19. Hourly cost of labor:                {labor_rate}

Income:
20. Price of a fountain drink:           {soda_fountain_price}
21. Price of a soda bottle:              {soda_bottle_price}
22. Price of a water:                    {water_price}
32. Price of a juice:                    {juice_price}
24. Price of a body armor:               {body_armor_price}
25. Price of a hotdog:                   {hotdog_price}
26. Price of a candy:                    {candy_price}
27. Price of a bag of chips:             {chip_price}
28. Price of a bag of popcorn:           {popcorn_price}
29. Price of a pickle:                   {pickle_price}
30. Price of a nacho:                    {nacho_price}
31. Price of a slice of pizza:           {pizza_slice_price}

Estimated Sales Volume:
32. Fountain drinks sold:                {soda_fountain_servings}
33. Soda bottles sold:                   {soda_bottles}
34. Water bottles sold:                  {waters}
35. Juices sold:                         {juices}
36. Body armors sold:                    {body_armors}
37. Hotdogs sold:                        {hotdogs}
38. Candies sold:                        {candies}
39. Bags of popcorn sold:                {popcorns}
40. Pickles sold:                        {pickles}
41. Nachos sold:                         {nachos}
42. Pizza slices sold:                   {pizza_slices}

Other Factors:
43. Hours open:                          {hours_open}

Analysis:
44. Profit/Loss Calculation
45. "What If" analysis with 10% variance
46. Find Break-Even

Enter Selection (0 to Exit):
        '''
    )

# Function to update the values.
def update_values(selection):
    '''
    Function updates the values based on user input.
    '''

    # Import the global variables into the function's scope.
    global soda_fountain_cost, \
        soda_bottle_cost, \
        water_cost, \
        juice_cost, \
        body_armor_cost, \
        hotdog_cost, \
        bun_cost, \
        candy_cost, \
        chip_cost, \
        popcorn_kernel_cost, \
        oil_cost, \
        salt_cost, \
        pickle_cost, \
        nacho_chips_cost, \
        nacho_cheese_cost, \
        pizza_slice_cost, \
        jalepeno_cost, \
        condiments_cost, \
        labor_rate, \
        soda_fountain_price, \
        soda_bottle_price, \
        water_price, \
        juice_price, \
        body_armor_price, \
        hotdog_price, \
        candy_price, \
        chip_price, \
        popcorn_price, \
        pickle_price, \
        nacho_price, \
        pizza_slice_price, \
        soda_fountain_servings, \
        soda_bottles, \
        waters, \
        juices, \
        body_armors, \
        hotdogs, \
        candies, \
        chips, \
        popcorns, \
        pickles, \
        nachos, \
        pizza_slices, \
        hours_open

    # If the selection equals 1.
    if selection == 1:

        # Save the user input value for serving cost.
        soda_fountain_cost = float(input('Enter Fountain Drink Cost: '))

    # If the selection equals 2.
    elif selection == 2:

        # Save the user input value for labor rate.
        soda_bottle_cost = float(input('Enter Soda Bottle Cost: '))

    # If the selection equals 3.
    elif selection == 3:

        # Save the user input value for monthly shop rental.
        water_cost = float(input('Enter Water Bottle Cost: '))

    # If the selection equals 4.
    elif selection == 4:
        
        # Save the user input value for monthly utilities.
        juice_cost = float(input('Enter Juice Cost: '))

    # If the selection equals 5.
    elif selection == 5:

        # Save the user input value for monthly advertising.
        body_armor_cost = float(input('Enter Body Amror Cost: '))

    # If the Selection equals 6.
    elif selection == 6:

        # Save the user input value for the selling price.
        hotdog_cost = float(input('Enter Hotdog Cost: '))

    # If the selection equals 7.
    elif selection == 7:

        # Save the user input value for servings per month.
        bun_cost = float(input('Enter Hotdog Bun Cost: '))

    # If the selection equals 8.
    elif selection == 8:

        # Save the user input value for servings per month.
        candy_cost = float(input('Enter Candy Cost: '))

    # If the selection equals 9.
    elif selection == 9:

        # Save the user input value for servings per month.
        chip_cost = float(input('Enter Chip Cost: '))

    # If the selection equals 10.
    elif selection == 10:

        # Save the user input value for servings per month.
        popcorn_kernel_cost = float(input('Enter Popcorn Kernel Cost : '))

    # If the selection equals 11.
    elif selection == 11:

        # Save the user input value for servings per month.
        oil_cost = float(input('Enter Popcorn Oil Cost: '))

    # If the selection equals 12.
    elif selection == 12:

        # Save the user input value for servings per month.
        salt_cost = float(input('Enter Popcorn Salt Cost: '))

    # If the selection equals 13.
    elif selection == 13:

        # Save the user input value for servings per month.
        pickle_cost = float(input('Enter Pickle Cost: '))

    # If the selection equals 14.
    elif selection == 14:

        # Save the user input value for servings per month.
        nacho_chips_cost = float(input('Enter Nacho Chip Cost: '))

    # If the selection equals 15.
    elif selection == 15:

        # Save the user input value for servings per month.
        nacho_cheese_cost = float(input('Enter Nacho Cheese Cost: '))

    # If the selection equals 16.
    elif selection == 16:

        # Save the user input value for servings per month.
        pizza_slice_cost = float(input('Enter Pizza Slice Cost: '))

    # If the selection equals 17.
    elif selection == 17:

        # Save the user input value for servings per month.
        jalepeno_cost = float(input('Enter Jalepeno Cost: '))

    # If the selection equals 18.
    elif selection == 18:

        # Save the user input value for servings per month.
        condiments_cost = float(input('Enter Condiments Cost: '))

    # If the selection equals 19.
    elif selection == 19:

        # Save the user input value for servings per month.
        labor_rate = float(input('Enter Labor Rate: '))

    # If the selection equals 20.
    elif selection == 20:

        # Save the user input value for servings per month.
        soda_fountain_price = int(input('Enter Fountain Drink Price: '))

    # If the selection equals 21.
    elif selection == 21:

        # Save the user input value for servings per month.
        soda_bottle_price = float(input('Enter Soda Bottle Price: '))

    # If the selection equals 22.
    elif selection == 22:

        # Save the user input value for servings per month.
        water_price = float(input('Enter Water Bottle Price: '))

    # If the selection equals 23.
    elif selection == 23:

        # Save the user input value for servings per month.
        juice_price = float(input('Enter Juice Price: '))

    # If the selection equals 24.
    elif selection == 24:

        # Save the user input value for servings per month.
        body_armor_price = float(input('Enter Body Armor Price:' ))

    # If the selection equals 25.
    elif selection == 25:

        # Save the user input value for servings per month.
        candy_price = float(input('Enter Candy Price: '))

    # If the selection equals 26.
    elif selection == 26:

        # Save the user input value for servings per month.
        chip_price = float(input('Enter Chip Price: '))

    # If the selection equals 27.
    elif selection == 27:

        # Save the user input value for servings per month.
        popcorn_price = float(input('Enter Bag of Popcorn Price:'))

    # If the selection equals 28.
    elif selection == 28:

        # Save the user input value for servings per month.
        pickle_price = float(input('Enter Pickle Price: '))

    # If the selection equals 29.
    elif selection == 29:

        # Save the user input value for servings per month.
        nacho_price = float(input('Enter Nacho Price: '))

    # If the selection equals 30.
    elif selection == 30:

        # Save the user input value for servings per month.
        pizza_slice_price = float(input('Enter Pizza Slice Price: '))

    # If the selection equals 31.
    elif selection == 31:

        # Save the user input value for servings per month.
        soda_fountain_servings = int(input('Enter Expected Number of Fountain Drinks Sold: '))

    # If the selection equals 32.
    elif selection == 32:

        # Save the user input value for servings per month.
        soda_bottles = int(input('Enter Expected Number of Soda Bottles Sold: '))

    # If the selection equals 33.
    elif selection == 33:

        # Save the user input value for servings per month.
        waters = int(input('Enter Expected Number of Water Bottles Sold: '))

    # If the selection equals 34.
    elif selection == 34:

        # Save the user input value for servings per month.
        juices = int(input('Enter Expected Number of Juices Sold: '))

    # If the selection equals 35.
    elif selection == 35:

        # Save the user input value for servings per month.
        body_armors = int(input('Enter Expected Number of Body Armors Sold: '))

    # If the selection equals 36.
    elif selection == 36:

        # Save the user input value for servings per month.
        hotdogs = int(input('Enter Expected Number of Hotdogs Sold: '))

    # If the selection equals 37.
    elif selection == 37:

        # Save the user input value for servings per month.
        candies = int(input('Enter Expected Number of Candies Sold: '))

    # If the selection equals 38.
    elif selection == 38:

        # Save the user input value for servings per month.
        chips = int(input('Enter Expected Number of Bags of Chips Sold: '))

    # If the selection equals 39.
    elif selection == 39:

        # Save the user input value for servings per month.
        popcorns = int(input('Enter Expected Number of Bags of Popcorn Sold: '))

    # If the selection equals 40.
    elif selection == 40:

        # Save the user input value for servings per month.
        pickles = int(input('Enter Expected Number of Pickles Sold: '))

    # If the selection equals 41.
    elif selection == 41:

        # Save the user input value for servings per month.
        nachos = int(input('Enter Expected Number of Nachos Sold: '))

    # If the selection equals 42.
    elif selection == 42:

        # Save the user input value for servings per month.
        pizza_slices = int(input('Enter Expected Number of Pizza Slices Sold: '))

    # If the selection equals 43.
    elif selection == 43:

        # Save the user input value for servings per month.
        hours_open = int(input('Enter Number of Hours Open: '))

# Function to calculate expenses.
def calculate_expenses(costs, quantities):
    '''
    Function calculates the expenses.
    '''

    fountain_drink = costs[0] * quantities[0]
    soda_bottle = costs[1] * quantities[1]
    water = costs[2] * quantities[2]
    juice = costs[3] * quantities[3]
    body_armor = costs[4] * quantities[4]
    hotdog = (costs[5] + costs[6]) * quantities[5]
    candy = costs[7] * quantities[6]
    chip = costs[8] * quantities[7]
    popcorn = (costs[9] + costs[10] + costs[11]) * quantities[8]
    pickle = costs[12] * quantities[9]
    nacho = (costs[13] + costs[14]) * quantities[10]
    pizza_slice = costs[15] * quantities[11]
    jalepenos = costs[16]
    condiments = costs[17]
    labor = costs[18] * quantities[12]

    total_expenses = fountain_drink + \
                        soda_bottle + \
                        water + \
                        juice + \
                        body_armor + \
                        hotdog + \
                        candy + \
                        chip + \
                        popcorn + \
                        pickle + \
                        nacho + \
                        pizza_slice + \
                        jalepenos + \
                        condiments + \
                        labor

    # Return the total expenses.
    return total_expenses

# Function to calculate income.
def calculate_income(prices, quantities):
    '''
    Function calculates income.
    '''
    
    fountain_drink = prices[0] * quantities[0]
    soda_bottle = prices[1] * quantities[1]
    water = prices[2] * quantities[2]
    juice = prices[3] * quantities[3]
    body_armor = prices[4] * quantities[4]
    hotdog = prices[5] * quantities[5]
    candy = prices[6] * quantities[6]
    chip = prices[7] * quantities[7]
    popcorn = prices[8] * quantities[8]
    pickle = prices[9] * quantities[9]
    nacho = prices[10] * quantities[10]
    pizza_slice = prices[11] * quantities[11]

    # Total income equals selling price times the servings per month.
    total_income = fountain_drink + \
                        soda_bottle + \
                        water + \
                        juice + \
                        body_armor + \
                        hotdog + \
                        candy + \
                        chip + \
                        popcorn + \
                        pickle + \
                        nacho + \
                        pizza_slice

    return total_income

# Function to calculate profit / loss.
def calculate_profit_loss(income, expenses):
    '''
    Function calculates profit and loss.
    '''

    # Calculate the profit loss value
    profit_or_loss = income - expenses

    #return the result.
    return profit_or_loss

# Function to calculate Percent differential for task three.
def calculate_differential(income, expenses, transaction_type):
    '''
    Function calculates the percent differential.
    '''

    # Define a list of percents.
    percents = [
        -0.10, 
        -0.08,
        -0.06,
        -0.04,
        -0.02, 
         0.00, 
         0.02, 
         0.04, 
         0.06, 
         0.08, 
         0.10
    ]

    # Loop through the percents.
    for p in percents:

        # If transaction type equals expenses.
        if transaction_type == 'expenses':

            # Calculate the new expenses value.
            new_expenses = expenses + (expenses * p)

            # Calculate the new profit loss value.
            profit_loss = income - new_expenses

            # Format and pring the outcome.
            print(f'Percent: {int(p * 100)} Expenses: {round(new_expenses, 2)} Profit/Loss: {round(profit_loss, 2)}')

        # If transaction type equals income.
        elif transaction_type == 'income':

            # Calculate the new income value.
            new_income = income + (income * p)

            # Calculate the new profit loss value.
            profit_loss = new_income - expenses

            # Format and print the outcome.
            print(f'Percent: {int(p * 100)} Income: {round(new_income, 2)} Profit/Loss: {round(profit_loss, 2)}')

# Function to handle the what if analysis.
def what_if_analysis(income, expenses):
    '''
    Function calculates and prints variance of expenses and income 
        from -10% to 10%.
    '''

    print()
    print('Varying the Expenses From -10% to +10%:')
    
    # Expense Percent Differential
    calculate_differential(income, expenses, 'expenses')

    print()
    print('Varying the Income From -10% to +10%:')

    # Income Percent Differential
    calculate_differential(income, expenses, 'income')
    print()

# Function to find the break even point.
def calculate_break_even(income, expenses, selling_price):
    '''
    Function detects the "Break-even" point, where the sign of Profit/Loss changes.
    '''
    
    # Save the selling price and initial profit loss value.
    price  = selling_price
    profit_loss = calculate_profit_loss(income, expenses)

    # Check whether profit loss is positive.
    if profit_loss >= 0:

        # Loop decreases the selling price until profit loss becomes negative.
        while profit_loss >= 0:

            # Decrease the price by 10 cents per iteration.
            price -= 0.1

            # Then calculate a new income.
            new_income = calculate_income(price)

            # Lastly get a profit loss with the new income value.
            profit_loss = calculate_profit_loss(new_income, expenses)

    # If the profit loss is negative...
    elif profit_loss < 0:

        # Loop increaes the selling price until profit loss becomes positive.
        while profit_loss < 0:

            # Increase the price by 10 cents per iteration.
            price += 0.1

            # Then calculate a new income.
            new_income = calculate_income(price)

            #Lastly get a lrofit loss with the new income.
            profit_loss = calculate_profit_loss(new_income, expenses)

    # Finally print te result.
    print(f'Break-Even occurs when a selling price of: {round(price, 2)}')

# Main Program.
def main():
    '''
    Main program function.
    '''


    while True:
        '''
        While loop diplays current values of the parameters.
        It then takes input, and performs functionality accordingly.
        '''
        
        # Category Lists
        prices = [
            soda_fountain_price,
            soda_bottle_price,
            water_price,
            juice_price,
            body_armor_price,
            hotdog_price,
            candy_price,
            chip_price,
            popcorn_price,
            pickle_price,
            nacho_price,
            pizza_slice_price,
        ]

        costs = [
            soda_fountain_cost,
            soda_bottle_cost,
            water_cost,
            juice_cost,
            body_armor_cost,
            hotdog_cost,
            bun_cost,
            candy_cost,
            chip_cost,
            popcorn_kernel_cost,
            oil_cost,
            salt_cost,
            pickle_cost,
            nacho_chips_cost,
            nacho_cheese_cost,
            pizza_slice_cost,
            jalepeno_cost,
            condiments_cost,
            labor_rate
        ]

        quantities = [
            soda_fountain_servings,
            soda_bottles,
            waters,
            juices,
            body_armors,
            hotdogs,
            candies,
            chips,
            popcorns,
            pickles,
            nachos,
            pizza_slices,
            hours_open
        ]



        # Run the Menu function.
        display_menu()
        
        # Save the user entered value as a variable.
        selected_value = input('Please enter an integer between 0 and 45: ')

        # Test if the user input is an integer.
        if selected_value.isdigit():

            selected_value = int(selected_value)

        # If it isn't...
        else:

            # Tell the user that they made an invalid selection.
            print('Invalid Selection. Please enter an integer value between 0 and 45...')
            continue

        # Calculate income and expenses.
        income = calculate_income(prices, quantities)

        expenses = calculate_expenses(costs, quantities)

        # If the input is 0 exit the program.
        if selected_value == 0:

            # Stop the loop.
            break
        
        # Update the various values if the selection is 1 through 7.
        elif 1 <= selected_value <= 43:
            
            # Run the update values function with the  enetered value.
            update_values(selected_value)

        # If the selection is 8, calulate the profit loss.
        elif selected_value == 44:

            # Call the profit/loss function and then calculate the profit loss per serving.
            profit_loss = calculate_profit_loss(income, expenses)

            # If the profit/loss it positive.
            if profit_loss >= 0:
                
                # Print out the message with positive.
                print(f'The concessions stand will have a profit of {round(profit_loss, 2)}.')

            else:
                
                # Print out the message with negative.
                print(f'The concenssions will have a loss of {profit_loss}.')

        # If the selection is 9, perform the what if analysis.
        elif selected_value == 45:

            # Call the what-if analysis function.
            what_if_analysis(income, expenses)

        # If the selection is 10, find the break-even point.
        elif selected_value == 46:
            
            # Call the break even function.e
            calculate_break_even(income, expenses, prices)

# Tell the interpreter to run this block first.
if __name__ == "__main__":

    main()
