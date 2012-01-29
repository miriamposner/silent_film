#!/usr/bin/env python
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

mech = Browser()
url = "http://www.silentera.com/PSFL/filmographies/directors/Micheaux-Oscar.html"
page = mech.open(url)
html = page.read()

soup = BeautifulSoup(html)

table = soup.find('table', width='600')

for row in table.findAll('tr'):
    col = row.findAll('td')
    movies = col.findAll('br')

print movies
