from ENS import readable, fetch_url, textRank, newsSearch
import sys
import re

number_of_links = int(sys.argv[1])
query = '+'.join(sys.argv[2:])
DEFAULT_ENCODING = 'latin-1'

article_list = []
summary_list = []

links = newsSearch(query,number_of_links)

if not links:
	print "No links found"

else:
	result = fetch_url.fetch_parallel(links)

	while not result.empty():
		url_entry = result.get()
		article = readable(url_entry[0],url_entry[1],DEFAULT_ENCODING) 
		summary = textRank(article)
		summary = summary.encode('ascii','ignore')
		article_list.append(article)
		summary_list.append(summary)


""" All the outputs are written to appropriate files in this part of the code """

for i in range(0,number_of_links):
    print str(i)
    print article_list[i-1]
    print "*** SUMMARY ***"
    print summary_list[i-1]
	
