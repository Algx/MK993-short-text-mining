# Week 3: Sentiment



Order of Coverage:

* Simple Sentiment Counting
* Using TextBlob
* NLTK Sentiment for Tweets
* NaiveBayes in Scikit-Learn
* NaiveBayes in Scikit-Learn-TrumpClassifier
* Sentiment Homework



This week you need to install Textblob.


> pip install TextBlob

Docs: http://textblob.readthedocs.io/en/dev/quickstart.html


#### Useful background:

* An introduction to sentiment analysis by Lincoln Mullen-- https://lct-master.org/files/MullenSentimentCourseSlides.pdf

* An article summarizing approaches: http://www.sciencedirect.com/science/article/pii/S2090447914000550

* An excellent draft chapter on use of Sentiment Lexicons: https://web.stanford.edu/~jurafsky/slp3/18.pdf

* Another site/lexicons for different text domains: https://nlp.stanford.edu/projects/socialsent/

* More references including lexicon files (word lists categorized by sentiment):
https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html


### Vocabulary concepts:

* valence, or polarity:  "positive", "negative", "neutral".
* emotion: "anger", "joy", etc.

There are a few basic approaches to sentiment analysis: 

* Word lists -- look for words in lists that have emotion -- "bad" etc., and count up the score.  This is very common and easy to do, if you have the word lists.
* Build a classifier -- use metadata or scored texts, like 1-star reviews and 5-star reviews -- to determine what the characteristics of a bad and good review are.  Naive Bayes or SVM's are good choices for text here.  Also now LSTMs (neural net models for text).
* Use an existing trained model (we will use one for social media).


### Links:

* https://nlp.stanford.edu/projects/socialsent/

* https://www.oreilly.com/learning/perform-sentiment-analysis-with-lstms-using-tensorflow

* Very good article on results with short and long texts for sentiment: https://nlp.stanford.edu/pubs/sidaw12_simple_sentiment.pdf

### Web Viewer for Sentiment.json file

If you want to view your sentiment.json file for a book in the web viewer, copy the sentiment.json file into the sentiment_vis directory.

>cd sentiment_vis
>python -m http.server 8001

Then in a web browser, open url localhost:8001.
Pick the net_sentiment.html file.  Mouse over a point to see the words!


