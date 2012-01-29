#!/usr/bin/env python
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

mech = Browser()
url = "http://www.silentera.com/PSFL/filmographies/actors/Arbuckle-Roscoe.html"
page = mech.open(url)
html = page.read()

soup = BeautifulSoup(html)


for node in soup.findAll('p'):
    print ''.join(node.findAll(text=True))
