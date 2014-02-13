""" 
To scrape facility addresses from http://www.bop.gov/locations/list.jsp I started trying to scrape this w/Beautiful Soup, but it turns out this is all in JSON
 """
import urllib2
import json
import csv

url = "http://www.bop.gov/PublicInfo/execute/locations?todo=query&output=json"
json_string = urllib2.urlopen(url).read()
## Load the string of JSON into a dict
jsondata = json.loads(json_string)
## Review the keys of the dict
## or just use http://jsbeautifier.org/ to see what it looks like
for item in jsondata:
    print item
## So I know there are three top level items

## Get the full list of items in "Locations"
for item in jsondata['Locations'][0]:
    print item


## Jumping around, but apparently I did this in 2011?
### Open a CSV WRiter
f=csv.writer(open('/tmp/test.csv','wb'))

###and write to it. 
for item in jsondata['Locations']:
    f.writerow([item['hasFsl'], item['code'], item['contactEmail'], item['special'], item['city'], item['privateFacl'], item['nameDisplay'], item['faclTypeDescription'], item['state'], item['phoneNumber'], item['latitude'], item['type'], item['locationtype'], item['zipCode'], item['hasCamp'], item['complexCode'], item['address'], item['securityLevel'], item['name'], item['gender'], item['region'], item['longitude'], item['hasFdc'],  item['timeZone'], item['nameTitle']])
 




## Good rundown of dict tools
### https://yuji.wordpress.com/2008/05/14/python-basics-of-python-dictionary-and-looping-through-them/
## And a post I found helpful
### http://stackoverflow.com/questions/1871524/convert-from-json-to-csv-using-python
## Work from http://stackoverflow.com/questions/5318747/using-python-to-extract-dictionary-keys-within-a-list
