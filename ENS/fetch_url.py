import threading, urllib2
import Queue

DEFAULT_ENCODING = 'latin-1'

def read_url(url, queue):
	try:
    		data = urllib2.urlopen(url).read().decode(DEFAULT_ENCODING)
	except urllib2.HTTPError, e:
	    checksLogger.error('HTTPError = ' + str(e.code))
	except urllib2.URLError, e:
	    checksLogger.error('URLError = ' + str(e.reason))
	except httplib.HTTPException, e:
	    checksLogger.error('HTTPException')
	except Exception:
	    import traceback
	    checksLogger.error('generic exception: ' + traceback.format_exc())

    	print('Fetched %s from %s' % (len(data), url))
    	queue.put([url,data])

def fetch_parallel(list_of_urls):
    result = Queue.Queue()
    threads = [threading.Thread(target=read_url, args = (url,result)) for url in list_of_urls]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return result
