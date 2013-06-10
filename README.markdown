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
