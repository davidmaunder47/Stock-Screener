
#import Classes
import yahoo_fin.stock_info as yf
import requests
import pandas as pd
import ftplib
import io
import re
import json
import Ratio_method
import Income_Statement as IS
import os
import Income_Path as IP
import Balance_path as BP
import shares_year as sy


def format_object(ticker):
    # The following function will pass in our ticker
    # and format the dataframe files from Panda and from our API
    try:
        # the following will format the ticker enter above into a more readable dataframe format form our pandas import
        bs_stock_1 = yf.get_balance_sheet(ticker)
        # format original columns into these easy to read columns
        bs_stock_1.columns = ["2020", "2019", "2018", "2017"]
        bs_stock_1.index.name = "Account"

        # formatting for the income statement portion
        is_stock_1 = yf.get_income_statement(ticker)
        is_stock_1.columns = ["2020", "2019", "2018", "2017"]
        is_stock_1.index.name = "Account"

        # Calling the function to format shares from a dictionary to get a float
        # We also want the daily stock and market cap
        shares_outstanding = sy.shares(ticker)
        daily_share_price = yf.get_live_price(ticker)
        market_cap = shares_outstanding * daily_share_price

        # this calls the year function
        year = sy.year_call()
        stock_attributes = {"Income Statement": is_stock_1, "Balance Sheet": bs_stock_1,
                            "total Shares": shares_outstanding, "Daily Shares": daily_share_price,
                            "market_cap": market_cap, "year": year, "ticker": ticker,
                            "daily_share_price": daily_share_price}
        control(stock_attributes)

    except:
        # if they did not enter a ticker
        # this will be a pseudo recursive approach and take us back to the main page
        print("you did not enter a ticker with a correct symbol,you will be taken back to the ticker login section")
        format_ticker()


def control(stock_attributes):
    # the point of this function is to decide which income or
    # balance statement function to call when the ticker is formatted
    control = True
    while control:
        print("")
        print("Please pick a financial Statement")
        print("Option '1' for the income statement")
        print("Option '2' for the balance sheet information")
        # this allows the user to get balance sheet of income statement information
        option = input("Please enter a number or type 'Q' to quit:").lower().strip()
        if option.lower().strip() == "q":
            print("you have chosen to quit using this stock snd or you have chosen to quit this program")
            control = False
        elif option.lower().strip() == "1":
            IP.income_statment_path(stock_attributes)
        elif option.lower().strip() == "2":
            BP.balance_statement_path(stock_attributes)


def format_ticker():
    # this function allows a user to pick a stock or get a random stock

    # These the sets are formed by importing the tickers from Yahoo API
    dow_set = set(yf.tickers_dow())
    snp_set = set(yf.tickers_sp500())

    # Combine both sets to create a random set of all companies in the S&P 500 and the dow jones
    sp_dow = dow_set.union(snp_set)

    test = True
    print("Please type 'quit' to exit the program at any time")
    print("Please type 'random' to get a random stock to analyze")
    while test:
        input_1 = str(input("Please enter a ticker of your choosing, with no quotation marks:"))
        # allows the user to quit
        if input_1.upper().strip() == "QUIT":
            print("you have opted to quit the program, goodbye!")
            test = False
        # this allows the user get a random stock from the dop and SP set
        elif input_1.upper().strip() == "RANDOM":
            # pops a string from the set
            a = sp_dow.pop()
            print(a)
            # this ticker calls the format object function which is the main function
            format_object(a)
            test = False
        # will allow the function to run again if the user enters a string longer than 8 elements
        # no stock will no 8 strings long
        elif len(input_1) < 8:
            print(input_1)
            # this ticker calls the format object function which is the main function
            format_object(input_1)
            test = False


def read_files():
    # This function is called main Its main purpose is to check if a user has created a file already for a certain stock
    try:
        file = input("Enter file name:")
        file_open = open(file, "r")
        control = True
        while control:
            # file_open.read()
            # The second part of this function is to check
            # if the a certain word of financial ratio is in a file that has been made already
            check = input("check to see if a financial ratio is in the word document Y/N: ")
            if check.lower().strip() == "y":
                lookup = input("Type in word to see if its in the file:")
                count = 0

                for lines in file_open:
                    for word in lines.split(" "):
                        if lookup.lower() in word.lower():
                            count += 1
                            break

                if count < 1:
                    print(lookup, "is not in file")
                else:
                    print(lookup, "is in the file")
            elif check.lower().strip() == "n":
                control = False
        file_open.close()

    # this except is made to make sure the file does not exist
    # or it prevents the program from crashing if the user enters a wrong name for a file
    except:
        print("file does not exist")
