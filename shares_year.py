import yahoo_fin.stock_info as yf


def year_call():
    #This function converts a string and makes sure its between 2017 and 2020
    #the function will go from a string to an int to make sure its between 2017 and 2020
    #then back to a string to pass it into our class
    test = True
    while test:
        try:
            year = int(input("Please enter a year from 2020- 2017:"))
            while year > 2020 or year < 2017:
                year = int(input("Please enter a year from 2020- 2017:"))
            test = True
        #this will run if the int is entered as a string
        except ValueError or TypeError:
            print("Please enter a number:")
            continue
        else:
            return year
            test = True


def shares(ticker):
    #This function calls a method from the yahoo api it converts into a dictionary
    test = yf.get_stats(ticker)
    test = test.set_index("Attribute")

    #converts a dataframe into an API
    dictionary = {}
    count = -1
    for i in test.index:
        count += 1
        for j in range(len(test["Value"])):
            if j == count:
                # print(test["Value"][j],i)
                dictionary[i] = test["Value"][j]

    string = dictionary["Shares Outstanding 5"]

    #the following takes a string and
    #converts it from a string into a int based on the string

    if string[-1] == "B":
        string = string.replace("B", "")
        shares_rounded = float(string)*1000000000

    elif string[-1] == "M":
        string = string.replace("M", "")
        shares_rounded = float(string) * 1000000
    else:
        shares_rounded = float(string)

    return shares_rounded
