from GoogleNews import GoogleNews
from readability import Document
from Summarize import summarize
from fetch_url import fetch_url
import sys
import re

number_of_links = int(sys.argv[1])
query = '+'.join(sys.argv[2:])
regex = re.compile("<(.*?)>|\&#13;")

article_list = []
summary_list = []

links = GoogleNews.search(query,number_of_links)


if not links:
	print "No links found"

else:
	result = fetch_url.fetch_parallel(links)

	while not result.empty():
		article = Document(result.get()).summary() 
		article = re.sub(regex, "", article)
		article = article.encode('ascii','ignore')
		ss = summarize.SimpleSummarizer()
		summary = ss.summarize(article,5)
		summary = summary.encode('ascii','ignore')
		article_list.append(article)
		summary_list.append(summary)


""" All the outputs are written to appropriate files in this part of the code """

for i in range(0,number_of_links):
	f2 = open(query + str(i),'w')
	f2.write(article_list[i-1] + '\n SUMMARY OF THE ABOVE ARTICLE: \n' + summary_list[i-1])
	f2.close()
	
