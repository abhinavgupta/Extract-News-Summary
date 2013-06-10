import networkx as nx
import numpy as np 
from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
 
def textRank(document):
    sentence_tokenizer = PunktSentenceTokenizer()
    sentences = sentence_tokenizer.tokenize(document)
 
    bow_matrix = CountVectorizer().fit_transform(sentences)
    normalized = TfidfTransformer().fit_transform(bow_matrix)
 
    similarity_graph = normalized * normalized.T
 
    nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
    scores = nx.pagerank(nx_graph)
    text_rank_graph = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
    number_of_nodes = int(0.25*len(text_rank_graph))
    
    if number_of_nodes < 3:
		number_of_nodes = 3
		
    del text_rank_graph[number_of_nodes:]
    
    summary = ' '.join(word for _,word in text_rank_graph)
    
    return summary
