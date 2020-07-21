import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

import math
import operator
from nltk.stem import WordNetLemmatizer

import spacy
from spacy.lang.en.stop_words import STOP_WORDS 
from string import punctuation

from heapq import nlargest

punctuation += '\n\t'

def spacy_summarizer(raw_text):
	raw_text = re.sub("[\[][0-9][\]]", "", raw_text)

	stop_words = list(STOP_WORDS)
	nlp_loader = spacy.load('en_core_web_sm')

	word_token = nlp_loader(raw_text)
	word_freq = {}
	for word in word_token:
		if word.text.lower() not in stop_words:
			if word.text.lower() not in punctuation:
				if word.text not in word_freq.keys():
					word_freq[word.text] = 1
				else:
					word_freq[word.text] += 1
	max_freq = max(word_freq.values())
	for word in word_freq.keys():
		word_freq[word] /= max_freq

	sent_token = [sent for sent in word_token.sents]
	sent_score= {}
	for sent in sent_token:
		for word in sent:
			if word.text.lower() in word_freq.keys():
				if sent not in sent_score.keys():
					sent_score[sent] = word_freq[word.text.lower()]
				else:
					sent_score[sent] += word_freq[word.text.lower()]

	summary = nlargest(5, sent_score, key=sent_score.get)
	final_summary = [word.text for word in summary]
	summary = ''.join(final_summary)
	return summary 

def nltk_summarizer(raw_text):
	raw_text = re.sub("[\[][0-9][\]]", "", raw_text)

	stop_words = set(stopwords.words("english"))
	word_token = nltk.word_tokenize(raw_text)

	word_freq = {}  
	for word in word_token:  
	    if word not in stop_words:
	        if word not in word_freq.keys():
	            word_freq[word] = 1
	        else:
	            word_freq[word] += 1

	max_freq = max(word_freq.values())

	for word in word_freq.keys():  
	    word_freq[word] /= max_freq

	sent_token = nltk.sent_tokenize(raw_text)
	sent_scores = {}  
	for sent in sent_token:  
	    for word in nltk.word_tokenize(sent.lower()):
	        if word in word_freq.keys():
	            if len(sent.split(' ')) < 30:
	                if sent not in sent_scores.keys():
	                    sent_scores[sent] = word_freq[word]
	                else:
	                    sent_scores[sent] += word_freq[word]


	select_length = 5
	summary_sentences = nlargest(select_length, sent_scores, key=sent_scores.get)
	summary = ' '.join(summary_sentences)  
	return summary 













