from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np


username='michael.aa.watson'
browser = webdriver.Chrome('C:\\Users\\mwatson\\Documents\\github\\chromedriver.exe')


browser.get('https://www.instagram.com/'+username+'/saved')
Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
