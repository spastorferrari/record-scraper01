from bs4 import BeautifulSoup
import requests as re
import pandas as pd
# ----------------------------------------------------------------- dependencies

url = "https://rollinrecs.com/rap-hip-hop-r-b/?_bc_fsnf=1&in_stock=1"
data = re.get(url) # re to get 'url' string
# ------------------------------------------------------------------ request url

soup = BeautifulSoup(data.text, "html.parser") # setup soup from url
discs = soup.select(".product-grid-item-name") # list of all items in page
price = soup.select(".price-value") # list of all prices
# ------------------------------------------------------------------ get data

# list of artists I want to accept into listing
artists = ['kanye west', 'mac miller','the notorious b.i.g.', 'asap rocky', 'frank ocean', 'kedrick lamar', 'tyler, the creator', 'asap mob']

record_name,artist_name,record_price = [], [], [] # setup indiv. cols.

# parse jay-z because of '-' first, then rest of artists
for i in range(len(discs)):
    if "jay-z" in (discs[i].text).lower():
        record_name.append(discs[i].text.split(' - ')[1][:-1])
        artist_name.append('Jay-Z')
        record_price.append(price[i].text)

    for n in artists:
        if n in (discs[i].text).lower():
            record_name.append(discs[i].text.split('\u200e–')[1][1:-1])
            artist_name.append(discs[i].text.split('\u200e–')[0][1:-1])
            record_price.append(price[i].text)


# convert prices to integers
record_price = [float(price.split('$')[1].split('\n')[0]) for price in record_price]

# construct dictionary
d = {'name':artist_name, 'record':record_name, 'price':record_price}
# construct pandas dataframe
listing = pd.DataFrame(d)

print(listing.to_markdown())
# --------------------------------------------------------------------------END 
