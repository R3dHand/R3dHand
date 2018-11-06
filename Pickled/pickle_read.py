import pandas as pd
import bs4 as bs
import urllib.request
import re

# Format data frame output
pd.set_option('display.height', -1)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'left')

# Read in csv ventura_county_zip_codes
ventura_county_zip_codes = pd.read_csv(r'C:\Users\corey\Corey-All-\R3dHand\redHand\csv\ventura_county_zip_codes.csv')    
zip_codes = []
cities = []

for line in ventura_county_zip_codes:
	fields = re.findall('(.*)[,]', line)
	print(fields)




#.to_csv(r'.csv')
