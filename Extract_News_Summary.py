import urllib2
from readability import Document,summarize, GoogleNews
import sys
import re

number_of_links = int(sys.argv[1])
query = '+'.join(sys.argv[2:])
regex = re.compile("<(.*?)>|\&#13;")

article_list = []
summary_list = []

links = GoogleNews.search(query,number_of_links)                                  #Perform Google News search

if not links:
  print "No links found"                                                          #If no links for a query then..

else:
  for l in links:
    html = urllib2.urlopen(l).read()
    article = Document(html).summary()
    article = re.sub(regex, "", article)
    article = article.encode('ascii','ignore')
    ss = summarize.SimpleSummarizer()
    summary = ss.summarize(article,5)
    summary = summary.encode('ascii','ignore')
    article_list.append(article)
    summary_list.append(summary)


  """ All the outputs are written to appropriate files in this part of the code """
for i in range(1,number_of_links):
  f2 = open(query + str(i),'w')
  f2.write(article_list[i-1] + '\n' + summary_list[i-1])
  f2.close()
