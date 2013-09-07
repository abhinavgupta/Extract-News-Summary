# Extract - News - Summary

## Description

This is a pure python package that returns summary of news articles for a serach term provided by the user. The script automates the process of finding appropriate news links, extracting text and summarizing it.

The final script extracts URLs from Google News, so it works best where the search query is a current affaird topic.

Following are the different modules inside the ENS folder:
 - *bsReadability* - This module takes uses BeautifulSoup to extract boilerplate from a given URL
 - *lxmlReadability* - This module uses the more faster lxml library to extract boilerplate from a given URL, however the library is less robust to badly formed HTML and encoding
 - *GoogleRSSReader* - This module takes in a search query and returns the scraped URLs from the Google RSS reader. The Google RSS reader is not strict in their scraping policies
 - *TextRankSummarize* - This module uses a modified PageRank algorithm to mark the most important sentences/phrases in a text. A more graphical and intuitive approach than word-frequency. (NOTE: The parameter defining the number of nodes to be selected for final summary is hardcoded in this script, to play around with it you need to make appropriate changes here)

### Requirements

 - lxml
 - networkx
 - numpy
 - sklearn
 - BeautifulSoup
 - nltk (Remember to install the punkt.tokenzier seperately)

### Install

    git clone https://github.com/abhinavgupta/Extract-News-Summary
    cd Extract-News-Summary/
    sudo sh install.sh

### Use script

There are two versions of the script, one using BeautifulSoup, the other using lxml. This is done specifcially for benchmarking purposes give the pros and cons of both parsers.

To use the BeautifulSoup version via terminal:


    ENS_Soup 5 Narendra Modi

To use the lxml version:

	ENS_lxml 5 Narendra Modi

### Example

    from ENS import Document, fetch_url, textRank, newsSearch

    links = newsSearch("RBI Governor", 5)
    for link in links:
        article = Document(url=link).summary()
        article = re.sub(regex, "", article)
        article = article.encode('ascii','ignore')
        summary = textRank(article)
        summary = summary.encode('ascii','ignore')

        print article
        print "*** SUMMARY ***"
        print summary

### Authors

 - Abhinav Gupta

### TODO

 - Remove networkx and sklearn dependencies
 - Add own tokenizer and remove nltk dependency
 - Solve encoding issue
 - Benchmark the summary 
 - Improve text extraction
