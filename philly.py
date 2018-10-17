from scraper import phetch_philly

# urls are in kind of inconsistent formats
# easy enough to just list them for now

year_urls = {
    '2007': 'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2007%20YTD/Explorer.Transactions.2007ytd.txt',
    '2008': 'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2008%20YTD/Explorer.Transactions.2008ytd.txt',
    '2009': 'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2009%20YTD/Explorer.Transactions.2009.YTD.txt',
    # '2010': 'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2010%20YTD/Explorer.Transactions.2010%20.txt',
    '2011': 'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2011%20YTD/Explorer.Transactions.2011.txt',
    '2012': 'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2012%20YTD/Explorer.Transactions.2012.YTD.txt',
    '2013': 'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2013%20YTD/Explorer.Transactions.2013.YTD.txt',
    '2014': 'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2014%20YTD/Explorer.Transactions.2014.YTD.txt',
    '2015': 'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2015%20YTD/Explorer.Transactions.2015.YTD.txt',
    '2016': 'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2016%20YTD/Explorer.Transactions.2016.YTD.txt',
    '2017': 'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2017%20YTD/Explorer.Transactions.2017.YTD.txt',
    '2018': 'ftp://ftp.phila-records.com/Year-to-Date%20Transaction%20Files/2018%20YTD/Explorer.Transactions.txt'
    }
for year, url in year_urls.items():
    try:
        print(f'Getting data for {year}')
        transactions = phetch_philly(url)
        transactions.to_csv(f'philly_transactions{year}.csv')
    except:
        continue
