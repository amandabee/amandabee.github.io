#!/usr/bin/env python

### This is rough, but works. I wanted a spreadsheet of MLB Salaries for a 
### basic lesson on means and medians and how wildly extravagant salaries 
### distort the mean. So I scraped the data from Newsday's salary database.

#import scraperwiki
import urllib2
from bs4 import BeautifulSoup
import csv

def get_soup(url):
    #soup = BeautifulSoup(scraperwiki.scrape(url))
    soup = BeautifulSoup(urllib2.urlopen(url))
    return soup


def get_salaries(soup, linewriter):
    table = soup.find("table", {"id":"sdb-results"})
    
    for row in table.findAll('tr'):
      cells = row.find_all("td")
      try:
        data = {
            'player' : cells[0].get_text().strip(),
            'team' : cells[1].get_text().strip(), 
            'position' : cells[2].get_text().strip(), 
            'state' : cells[3].get_text().strip(), 
            'league' : cells[4].get_text().strip(),
            'division' : cells[5].get_text().strip(),
            '2013_salary' : cells[6].get_text().strip('$,').strip(),
            'age' : cells[7].get_text().strip()
        }
        #scraperwiki.sqlite.save(unique_keys=['player'],data=data)
        linewriter.writerow(data)
        print "Saved " + data['player']
      except Exception,e: 
        print str(e)


base_url = "http://data.newsday.com/long-island/data/baseball/mlb-salaries-2013/?currentRecord="

print range(1, 854, 50)

  
with open('/home/amanda/Desktop/mlb_salaries_alt.csv', 'a+') as csvfile:
    fieldorder = ['player' , 'team' , 'position' , 'state' ,
                    'league', 'division', '2013_salary', 'age']
    linewriter = csv.DictWriter(csvfile, fieldorder, delimiter='|',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        
    for record in range(1, 854, 50):
        print "starting..."
        url = base_url + str(record);
        soup = get_soup(url)
        get_salaries(soup, linewriter)
        print url;


