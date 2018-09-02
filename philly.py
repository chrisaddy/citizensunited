from scraper import phetch_philly
import pandas as pd

### urls are in kind of inconsistent formats
### easy enough to just list them for now

year_urls = [
    'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2007%20YTD/Explorer.Transactions.2007ytd.txt',
    'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2008%20YTD/Explorer.Transactions.2008ytd.txt',
    'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2009%20YTD/Explorer.Transactions.2009.YTD.txt',
    'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2010%20YTD/Explorer.Transactions.2010%20.txt',
    'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2011%20YTD/Explorer.Transactions.2011.txt',
    'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2012%20YTD/Explorer.Transactions.2012.YTD.txt',
    'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2013%20YTD/Explorer.Transactions.2013.YTD.txt',
    'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2014%20YTD/Explorer.Transactions.2014.YTD.txt',
    'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2015%20YTD/Explorer.Transactions.2015.YTD.txt',
    'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2016%20YTD/Explorer.Transactions.2016.YTD.txt',
    'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2017%20YTD/Explorer.Transactions.2017.YTD.txt',
    'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2018%20YTD/Explorer.Transactions.txt'
    ]

transactions = phetch_philly(year_urls[0])

for url in year_urls[1:]:
    transactions.append(phetch_philly(url))

print(transactions.info())

### TODO put it in a database
