# portfolio.py
 
import csv
import urllib
from collections import defaultdict
 
def get_portfolio(filename):
    ''' read in the CSV file of stock trades
          build a dictionary of lists of tuples of the form
          { symbol : [(shares, purchase px), (shares, purchase px), ...], ... }
          { 'CSCO':  [(150, 19.05), (175, 19.56), ...], ... }
    '''
    portfolio = defaultdict(list)
    with open(filename) as f:
        for symbol, shares, price in csv.reader(f):
            portfolio[symbol].append( (int(shares), float(price)) )
    return portfolio

quote_url_template = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sl1d1t1c1ohgv&e=.csv'
def get_quote(*symbols):
    url = quote_url_template % ','.join(symbols)
    u = urllib.urlopen(url)
    quotes = {}
    for symbol, price, _, _, _, _, _, _, _ in csv.reader(u):
        try:
            quotes[symbol] = float(price)
        except ValueError:
            pass
    return quotes

def get_positions(portfolio):
    return {ticker: sum([shares for shares, _ in portfolio[ticker]])for ticker in portfolio}

def get_market_value(portfolio):
    quotes = get_quote(*portfolio)
    for position in get_positions(portfolio):
        return {ticker: sum([shares * quotes[ticker] for shares, _ in portfolio[ticker]])for ticker in portfolio}

def get_profits(portfolio):
    quotes = get_quote(*portfolio)
    for position in get_positions(portfolio):
        return[sum([shares * (quotes[ticker] - price) for shares, price in portfolio[ticker]])for ticker in portfolio]

if __name__ == '__main__':
    filename = 'notes/stocks.txt'
    portfolio = get_portfolio(filename)
    print get_quote(*portfolio)
    positions = get_positions(portfolio)
    market_values =  get_market_value(portfolio)
    profits = get_profits(portfolio)
    heading_template = '%20s %20s %21s %21s'
    row_template = u'%20s %20s %20s\N{small dollar sign} %20s\N{small dollar sign}'
    header = 'Ticker', 'Shares', 'Market Value', 'Profit'
    print heading_template % header
    print heading_template % tuple(['-' * len(h) for h in header])
    i = 0
    for ticker in portfolio:
        print heading_template % (ticker, positions[ticker], market_values[ticker], profits[i])
        i += 1
    print u"Total Profits for Portfolio is %20s\N{small dollar sign}" % sum(profits)
    
    
    
