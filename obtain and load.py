import datetime
import requests
import bs4
class obtain_and_load():
    def __init__(self, cur):
         self.cur = cur
    def obtain_parse_wiki_snp500(self):
        ## get time 
        now = datetime.datetime.utcnow()
        ## get HTML for the to 
        response = requests.get(
        "http://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        )
        soup = bs4.BeautifulSoup(response.text)
        symbolslist = soup.select('table')[0].select('tr')[1:]
        symbols = []
        for i, symbol in enumerate(symbolslist):
            tds = symbol.select('td')
            symbols.append(
                (
                    tds[0].select('a')[0].text, # Ticker ’stock’,
                    tds[1].select('a')[0].text, # Name
                        tds[3].text, # Sector ’USD’, now, now
                    )
                )
        return symbols