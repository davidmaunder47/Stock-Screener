import Ratio_method
import os


def balance_statement_path(stock_info):

    #gets the dictionary input and converts them into individual variables so we can pass it
    balancesheet_statement = stock_info["Balance Sheet"]
    market_cap = stock_info["market_cap"]
    year = str(stock_info["year"])
    ticker = stock_info["ticker"]
    live_price = stock_info["daily_share_price"]
    string = ticker + ".txt"

    account_list = ["Balance Sheet All Years", "Cash to Total Debt", "Assets to Total Debt", "current Ratio",
                    "Cash/Current Liabilities", "Equity/Liabilities", "Cash/Short Term Debt",
                    "liquid assets/short term debt", "price to book", "current year debt FS", "live price"]

    #This function is used to print out a menu for the consumer
    count = 1
    for i in account_list:
        if count == 10:
            print("get " + i +":" " price")
        else:
            print("get " + i + ": "+ str(count))
        count +=1

    #this function allows a user to write append or not read a file
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
        elif file_input.lower().strip() == "n":
            open_file = False
            file_control = False

    #this try statement allows the user to call the individual functions from our Income Statement Class
    try:
        control = True
        while control:
            option = input("Please enter a number or type 'q' to quit:")
            if option.lower().strip() == "q":
                control = False
            elif option.lower().strip() == "1":
                a = Ratio_method.get_debt_fs(balancesheet_statement)
                print(a)
            elif option.lower().strip() == "2":
                a = Ratio_method.cash_debt(balancesheet_statement, year, ticker)
                print(a)
            elif option.lower().strip() == "3":
                a = Ratio_method.asset_debt(balancesheet_statement, year, ticker)
                print(a)
            elif option.lower().strip() == "4":
                a = Ratio_method.currentasset_current_liabilities(balancesheet_statement, year, ticker)
                print(a)
            elif option.lower().strip() == "5":
                a = Ratio_method.cash_current_liabilities(balancesheet_statement, year, ticker)
                print(a)
            elif option.lower().strip() == "6":
                a = Ratio_method.equity_debt(balancesheet_statement, year, ticker)
                print(a)
            elif option.lower().strip() == "7":
                a = Ratio_method.cash_current_debt(balancesheet_statement, year, ticker)
                print(a)
            elif option.lower().strip() == "8":
                a = Ratio_method.short_assets_current_debt(balancesheet_statement, year, ticker)
                print(a)
            elif option.lower().strip() == "9":
                a = Ratio_method.current_price_to_book(balancesheet_statement, year, ticker, market_cap)
                print(a)
            elif option.lower().strip() == "10":
                a = Ratio_method.get_current_FS(balancesheet_statement, year)
                print(a)
            elif option.lower().strip() == "price":
                print(ticker, "Live Price is:", live_price)
            if open_file:
                file.write(str(a) + "\n")

    except:
        print("this function does not exist for this company, please try another company")
    #this will close the file if the user opens it
    finally:
        if open_file:
            file.close()