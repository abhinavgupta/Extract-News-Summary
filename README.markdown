## Extract - News - Summary

### Requirements

 - lxml
 - networkx
 - numpy
 - nltk
 - sklearn

### Install

    git clone https://github.com/abhinavgupta/Extract-News-Summary
    cd Extract-News-Summary/
    sudo python setup.py install

### Use script

    ENSscript 5 star wars

### Example

    from ENS import Document, fetch_url, textRank, newsSearch

    links = newsSearch("Star Wars 7", 5)
    for link in links:
        article = Document(url=link).summary()
        article = re.sub(regex, "", article)
        article = article.encode('ascii','ignore')
        summary = textRank(article)
        summary = summary.encode('ascii','ignore')

        print article
        print "*** SUMMARY ***"
        print summary


### Old code. blah.

*************************************************************************
*       README file for Summarizing News Articles with user Query       *
*************************************************************************

REQUIREMENTS: a. Python and it's standard libraries
              b. NLTK along with the "punkt sentence tokenizer" and "english-pickle"
              c. Python lxml-library


The sub-folder contains the following MAIN scripts of the same name:

*************
*  SCRIPT 1 *
*************
GoogleNews.py - An independent script that can fetch the desired number of URLs for a particular search query

USAGE: The script consists of the following function:
        search(query, number of links)

query = Is the desired query seperated by '+' 

eg: If your desired search is "Mayawati BSP election" then the query string should be "Mayawati+BSP+election"



*************
*  SCRIPT 2 *
*************
readability.py - Independent script that extracts relevant text from a URL

USAGE: The script consists of uses a lot of support scripts for cleaning, housekeeping, debugging and logging. The "Document" class in the mentioned script isuseful for the task of extracting relavant text. Following is the way to use it in python terminal

>> from readability import Document
>> html = urllib2.urlopen(INSERT_URL_HERE).read()
>> article = Document(html).summary()
        

OUTPUT: Relevant Text. (Uses the algorithm by the arc90 readability project. Check my other github repo for the same)

*************
*  SCRIPT 3 *
*************
summarize.py - (Summarize folder) Independent script that creates the summary using simple analysis for sentences.

USAGE: Following is the way to use it in a python terminal
>> import summarize
>> ss = summarize.SimpleSummarizer()
>> summary = ss.summarize(INSERT_TEXT_TO_BE_SUMMARIZED_HERE,NUMBER_OF_LINES_FOR_SUMMARY)

OUTPUT: Summarized text.

*************
*  SCRIPT 4 *
*************
Summary.py - (TextRank folder) Independent script that creates the summary using TextRank for sentences.

USAGE: Following is the way to use it in a python terminal
>> import Summary
>> result = Summary.textrank(article)

OUTPUT: Summarized text.


*************
*  SCRIPT 5 *
*************
Extract_News_Summary.py - A script that uses all the above scripts

INPUT: Query and number of news articles to be scraped

USAGE: On the terminal do the following

python Extract_News_Summary.py <Number of links> <Query>

example: python Extract_News_Summary.py 50 India Pakistan Cricket

*************
*  SCRIPT 6 *
*************
Extract_News_Summary_TextRank.py - A script that generates summary of articles using the TextRank method

INPUT: Query and number of news articles to be scraped

USAGE: On the terminal do the following

python Extract_News_Summary.py <Number of links> <Query>

example: python Extract_News_Summary.py 50 India Pakistan Cricket


TODO: 1. Get urllib exception handling - Exception handling added
      2. Unicode-ASCII conversion is weakly handled
      3. If possible better scraping
      4. More complex Summarization algorithms - Added TexRank. LexRank to be added soon
      5. urllib2 fetching is slow - Used threads ti improve fetching. Twice as fast results

