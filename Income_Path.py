import Income_Statement as IS
import os


def income_statment_path(stock_info):
    # gets the dictionary input and converts them into individual variables so we can pass it
    income_statement = stock_info["Income Statement"]
    market_cap = stock_info["market_cap"]
    year = str(stock_info["year"])
    live_price = stock_info["daily_share_price"]
    ticker = stock_info["ticker"]

    string = ticker + ".txt"

    file_control = True
    while file_control:
        open_file = True
        file_input = input("Enter 'w' or 'a' to write or append a file or 'n' to do nothing:")
        if file_input.lower().strip() == "w":
            file = open(string, "w")
            file_control = False
        elif file_input.lower().strip() == "a":
            if os.path.exists(string):
                file = open(string, "a")
                file_control = False
            else:
                print("File does not exist!")
        elif file_input.lower().strip() == "n":
            open_file = False
            file_control = False
    account_list = ["Income Statement", "Net Income", "PE Ratio", "revenue",
                    "income/revenue", "interest/expense", "price/expense",
                    "price/revenue", "four year income growth rate",
                    "four year revenue growth rate", "current year financial", "Live price"]

    # This function is used to print out a menu for the consumer
    count = 1
    for i in account_list:
        if count == 10:
            print("get " + i + ":" " price")
        else:
            print("get " + i + ": " + str(count))
        count += 1

    income_stock_object = IS.IncomeStatement(income_statement,market_cap,year,ticker)
    try:
        control = True
        while control:
            option = input("Please enter a number or type 'quit' to quit:")
            if option.lower().strip() == "quit":
                control = False
            elif option.lower().strip() == "1":
                a = income_stock_object.print_income_statement()
                print(a)

            elif option.lower().strip() == "2":
                a = income_stock_object.get_income()
                print(a)

            elif option.lower().strip() == "3":
                a = income_stock_object.get_price_earnings()
                print(a)

            elif option.lower().strip() == "4":
                a = income_stock_object.get_revenue()
                print(a)

            elif option.lower().strip() == "5":
                a = income_stock_object.get_income_revenue()
                print(a)

            elif option.lower().strip() == "6":
                a = income_stock_object.get_interest_expense_NI()
                print(a)

            elif option.lower().strip() == "7":
                a = income_stock_object.get_price_to_sale()
                print(a)

            elif option.lower().strip() == "8":
                a = income_stock_object.four_year_income_growth_rate()
                print(a)

            elif option.lower().strip() == "9":
                a = income_stock_object.four_year_revenue_growth_rate()
                print(a)

            elif option.lower().strip() == "10":
                a = income_stock_object.income_statement_of_year()
                print(a)

            elif option.lower().strip() == "price":
                print(live_price)
            if open_file == True:
                file.write(str(a) + "\n")
    except:
        print("There is no function for this company, you will be taken back to the Statement Selection screen")
    finally:
        if open_file == True:
            file.close()
