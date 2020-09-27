import pandas as pd
from pandas import DataFrame
import numpy as np
import sys
import urllib
import re
from html.parser import HTMLParser
link = "https://unstats.un.org/sdgs/indicators/indicators-list/"
f = urllib.request.urlopen(link)
myfile = f.read()
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
html = myfile
soup3=BeautifulSoup(html,'html.parser')
spans = []
spans.append(soup3.findAll('li')[89])
spans.append(soup3.findAll('li')[90])
spans.append(soup3.findAll('li')[91])
spans.append(soup3.findAll('li')[92])
spans.append(soup3.findAll('li')[93])
spans.append(soup3.findAll('li')[94])
spans.append(soup3.findAll('li')[95])
spans.append(soup3.findAll('li')[96])
spans.append(soup3.findAll('li')[97])
spans.append(soup3.findAll('li')[98])
spans.append(soup3.findAll('li')[99])
spans.append(soup3.findAll('li')[100])

df = pd.DataFrame() 
df['indicators']=spans
df
