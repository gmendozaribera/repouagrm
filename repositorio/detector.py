from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity


def detector(ruta1,ruta2):
    data_set= (ruta1,ruta2)
    count_vect = CountVectorizer()
    term_freq_matrix=count_vect.fit_transform(data_set)
    #print(count_vect.vocabulary_,'\n')
    tfidf = TfidfTransformer()
    tf_idf_matrix = tfidf.fit_transform(term_freq_matrix)
    #print (tf_idf_matrix.todense(),'\n')
    similarity=cosine_similarity(tf_idf_matrix[0:1], tf_idf_matrix[1:2])
    return "La similaridad entre los documentos es del: " +str(int(similarity[0][0]*100))+ "%"