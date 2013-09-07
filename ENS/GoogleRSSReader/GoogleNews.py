import urllib2
# Standard Python parser for XML files (Non standard HTML)
from xml.dom.minidom import parseString
import sys

def newsSearch( term, count ):                                          
    # Term = query string, count = number of links desired
    term = "+".join(term.split())
    results = [] # List for storing the URLs 

    # Open Google news for the desired query and number of links, 
    # get RSS output and parse it as a string with XML DOM  
    obj = parseString(urllib2.urlopen(
    'http://news.google.com/news?q=%s&output=rss&num=%s' % (term, 
     str(count))).read())
    # From the parsed string get the Elements with the tag name <link>, skip the first two tags
    links = obj.getElementsByTagName('link')[2: count+2] 
    for link in links:
        # From the data inside the <link> tag, seperate them at "="
        # and append the URL in the result list
        results.append( link.childNodes[0].data.split('=')[-1] )  
    return results
