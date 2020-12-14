
#import classes
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
import format_object as FO
try:
    from requests_html import HTMLSession
except Exception:
    pass

def main():

    # Basic print information to tell the user about the program
    print("Welcome to a stock Screener")
    print("""This program will allow you to: 
          1. To read financial information from a text file 
          2. Get financial information from a stock or 
          """)

    #this variable allows the user to control the program
    first_test = True

    while first_test:
        start = input("Please enter 1 to read a file,type 'quit' to quit the program, or type 2 to screen a stock:")
        #takes the user to the read file part of the program
        if start == "1":
            FO.read_files()

        #allows the user to terminate the program completely
        elif start.lower().strip() =="quit":
            print("Thank you for using this program:")
            first_test = False

        #will take the user to the stock screener
        else:
            test = True
            while test:
                round_2 = str(input("do you wish to continue screening stocks? Y= Yes, N = No:"))
                if round_2.upper().strip() == "Y":
                    FO.format_ticker()
                elif round_2.upper().strip() == "N":
                    print("Stock Screener program Terminated!!!!!!")
                    test = False
main()
