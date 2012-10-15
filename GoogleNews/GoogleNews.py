import urllib2
from xml.dom.minidom import parseString                             #Standard Python parser for XML files (Non standard HTML)
import sys
def search( term, count ):                                          #Term = query string, count = number of links desired



    results = []                                                    #List for storing the URLs 



    obj = parseString( urllib2.urlopen('http://news.google.com/news?q=%s&output=rss&num=%s' % (term, str(count))).read() ) #Open Google news for the desired query and number of links, get RSS output and parse it as a string with XML DOM  


    links = obj.getElementsByTagName('link')[2: count+2] #From the parsed string get the Elements with the tag name <link>, skip the first two tags


    for link in links:

      results.append( link.childNodes[0].data.split('=')[-1] )  #From the data inside the <link> tag, seperate them at "=" and append the URL in the result list


    return results

