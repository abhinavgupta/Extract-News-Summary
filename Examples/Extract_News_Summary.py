from ENS import Document, fetch_url, textRank, newsSearch, SimpleSummarizer
import sys
import re

number_of_links = int(sys.argv[1])
query = '+'.join(sys.argv[2:])
regex = re.compile("<(.*?)>|\&#13;")

article_list = []
summary_list = []

links = newsSearch(query,number_of_links)


if not links:
	print "No links found"

else:
	result = fetch_url.fetch_parallel(links)

	while not result.empty():
		article = Document(result.get()).summary() 
		article = re.sub(regex, "", article)
		article = article.encode('ascii','ignore')
		ss = SimpleSummarizer()
		summary = ss.summarize(article,5)
		summary = summary.encode('ascii','ignore')
		article_list.append(article)
		summary_list.append(summary)


""" All the outputs are written to appropriate files in this part of the code """

for i in range(0,number_of_links):
    print str(i)
    print article_list[i-1]
    print "*** SUMMARY ***"
    print summary_list[i-1]
	
