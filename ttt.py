import sys
import io
import re
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
url=input('enter the url ')
#Checking of valid URL
def is_valid_url(url):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)
#Access the size of webpage
print("Task to access the size of webpage in bytes")
try:
    html=urlopen(url)
    k=html.read()
    soup=BeautifulSoup(k,'lxml')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
except AttributeError as e:
    print(e)    
else:
    print("size of web page is"+"="+str(sys.getsizeof(k))+"bytes")
    #Accessing the number of links
    print("Task to access the number of links in page pointing to the same domain")
    a=0
    for link in soup.find_all('a',href=True):
        if ((link['href']== url) or (link['href']=='/')):
            a=a+1
    print("Number of links pointing to same domain is "+str(a))
