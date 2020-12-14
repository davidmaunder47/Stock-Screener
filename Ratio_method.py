import yahoo_fin.stock_info as yf

#This package is a list of functions that yield financial information
#Each function will find a position of the value and year in the dataframe

#return balance sheet information for four years


def get_debt_fs(object):
    return object

#Gets cash over debt of the company
#Used to asses ability pay back debt


def cash_debt(object, year, ticker_name):
    a = object.index.get_loc("totalLiab")
    b = object.index.get_loc("cash")
    c = object[year][b]
    d = object[year][a]
    string = "{} {}:\nCash/Debt Ratio: {:.2f}"
    return string.format(ticker_name, year, c/d)

#shows asset to the debt for the company
#ability to pay back the debt


def asset_debt(object, year, ticker_name):
    a = object.index.get_loc("totalLiab")
    b = object.index.get_loc("totalAssets")
    c = object[year][b]
    d = object[year][a]
    string = "{} {}:\nAsset/Debt Ratio: {:.2f}"
    return string.format(ticker_name, year, c / d)

#shows current asset to total current debt for the company
#ability to pay back the debt on a short term basis


def currentasset_current_liabilities(object, year, ticker_name):
    a = object.index.get_loc("totalCurrentLiabilities")
    b = object.index.get_loc("totalCurrentAssets")
    c = object[year][b]
    d = object[year][a]
    string = "{} {}:\nCurrent Asset/Current Liabilities Ratio: {:.2f}"
    return string.format(ticker_name, year, c / d)

#shows cash to current debt for the company
#ability to pay back the debt in the short term


def cash_current_liabilities(object, year, ticker_name):
    a = object.index.get_loc("totalCurrentLiabilities")
    b = object.index.get_loc("cash")
    c = object[year][b]
    d = object[year][a]
    string = "{} {}:\nCash/Current Liability Ratio: {:.2f}"
    return string.format(ticker_name, year, c / d)


def equity_debt(object, year, ticker_name):
    # Shows how the company is leveraged
    a = object.index.get_loc("totalLiab")
    b = object.index.get_loc("totalStockholderEquity")
    c = object[year][b]
    d = object[year][a]
    string = "{} {}:\nDebt/Equity Ratio: {:.2f}"
    return string.format(ticker_name, year, c / d)


def cash_current_debt(object, year, ticker_name):
    # Shows a company to pay back there debt in the short term
    a = object.index.get_loc("shortLongTermDebt")
    b = object.index.get_loc("cash")
    c = object[year][b]
    d = object[year][a]
    string = "{} {}:\nCash/Current Debt Ratio: {:.2f}"
    return string.format(ticker_name, year, c/d)


def short_assets_current_debt(object, year, ticker_name):
    # Shows a company to pay back there debt in the short term
    a = object.index.get_loc("shortLongTermDebt")
    b = object.index.get_loc("cash")
    c = object.index.get_loc("shortTermInvestments")
    d = object.index.get_loc("accountsPayable")
    e = object[year][a]
    f = object[year][b]
    g = object[year][c]
    h = object[year][d]
    i = e+h
    j = f+g
    string = "{} {}:\nLiquid Assets/Current Liabilities Ratio: {:.2f}"
    return string.format(ticker_name, year, i/j)


def current_price_to_book(object, year, ticker_name, market_cap):
    # current price to book shows value in a company
    b = object.index.get_loc("totalStockholderEquity")
    c = object[year][b]
    e = market_cap/(c)
    string = "{} {}:\n Price to Book Ratio: {:.2f}"
    return string.format(ticker_name, year, e)


def get_current_FS(object, year):
    # get price for company
    a = object[year]
    return a
