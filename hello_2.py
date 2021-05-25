import gensim
from hello import preprocess_text
import pickle

from gensim import similarities

import sys

gensim_dictionary = gensim.corpora.Dictionary.load('gensim_dictionary.gensim')
lsa_model = gensim.models.lsimodel.LsiModel.load('gensim_model.gensim')
gensim_corpus = pickle.load(open('gensim_corpus_corpus.pkl', 'rb'))


test_doc = sys.argv[1]

test_doc = preprocess_text(test_doc)
bow_test_doc = gensim_dictionary.doc2bow(test_doc)
bow_test_doc_lsa = lsa_model[bow_test_doc]

index = similarities.MatrixSimilarity(lsa_model[gensim_corpus])
sims = index[bow_test_doc_lsa]

sims = sorted(enumerate(sims), key=lambda item: -item[1])
for doc_position, doc_score in sims:
    print(doc_score, doc_position)
