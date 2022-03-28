import os
from bs4 import BeautifulSoup

files = os.listdir("..")

for file in files:
    print( "file : ", file)
