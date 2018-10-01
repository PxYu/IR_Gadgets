import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
from krovetzstemmer import Stemmer
stemmer = Stemmer()

s = "According to Wikipedia, Information Retrieval is the activity of obtaining information resources relevant to an information need from a collection of information resources."

tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(s)
print tokens

words = [w.lower() for w in tokens]
print words

non_stopped_words = [w for w in words if not w in stopwords]
print non_stopped_words

stemmed_words = [stemmer.stem(w) for w in non_stopped_words]
print stemmed_words