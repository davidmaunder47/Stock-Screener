import yahoo_fin.stock_info as yf
class IncomeStatement:

    #This income statement class will take the dictionary objects and pass them as attributes
    def __init__(self, income_statement, market_cap, year, ticker):
        self.income_statement = income_statement
        self.market_cap = market_cap
        self.year = year
        self.ticker = ticker

    """These methods will take a dataframe and find a position in a column 
    the position in the column will return a value which we can find in the row"""

    #this method just returns the income statement
    def print_income_statement(self):
        return self.income_statement

    #this income statement of the year you want
    def income_statement_of_year(self):
        return self.income_statement[self.year]

    #Returns the income of the year to pass other functions
    def return_income(self):
        a = self.income_statement.index.get_loc("netIncome")
        d = self.income_statement[self.year][a]
        return d

    #returns just the net income
    def get_income(self):
        d = self.return_income()
        string = "{} {}: Net Income Amount: {:.2f}"
        return string.format(self.ticker, self.year, d)

    #gives just the revenue to pass for other methods
    def return_revenue(self):
        b = self.income_statement.index.get_loc("totalRevenue")
        d = self.income_statement[self.year][b]
        return d

    #prints out the revenue of the year when called
    def get_revenue(self):
        d = self.return_revenue()
        string = "{} {}: Total Gross Revenue: {:.2f}"
        return string.format(self.ticker, self.year, d)

    #the Market cap divides by total income fo the company
    #its used to justify value
    def get_price_earnings(self):
        d = self.return_income()
        e = self.market_cap/d
        string = "{} {}: Price Earnings Amount: {:.2f}"
        return string.format(self.ticker, self.year, e)

    #Shows income over revenue
    #show profit margin
    def get_income_revenue(self):
        b = self.return_income()
        d = self.return_revenue()
        string = "{} {}: Income/Revenue: {:.2f}%"
        return string.format(self.ticker, self.year, (b / d) * 100)

    #interest over expense shows a potential inability to pay back debt
    def get_interest_expense_NI(self):
        b = self.return_income()
        c = self.income_statement.index.get_loc("interestExpense")
        d = self.income_statement[self.year][c]
        string = "{} {}: Interest/Net Income: {:.2f}"
        e = ((d*-1)/b)*100
        return string.format(self.ticker, self.year, e)

    #Market cap of the stock by revenue shows value of a company
    def get_price_to_sale(self):
        b = self.return_revenue()
        string = "{} {}: Price/Sale: {:.2f}"
        return string.format(self.ticker, self.year, self.market_cap/b)

    #Takes whatever year the user wants and gets a growth function 2017 for the income account
    def four_year_income_growth_rate(self):
        a = self.return_income()
        b = self.income_statement.index.get_loc("netIncome")
        c = self.income_statement["2017"][b]
        d = ((a-c)/c)*100
        string = "{} {}: Average income growth rate from 2017: {:.2f}"
        return string.format(self.ticker, self.year, d)

    # Takes whatever year the user wants and gets a growth function 2017 for the revenue account
    def four_year_revenue_growth_rate(self):
        a = self.return_revenue()
        b = self.income_statement.index.get_loc("totalRevenue")
        c = self.income_statement["2017"][b]
        d = ((a-c)/c)*100
        string = "{} {}: Average revenue growth rate from 2017: {:.2f}"
        return string.format(self.ticker, self.year, d)
