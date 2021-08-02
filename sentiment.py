from pprint import pprint
from database import db 
from datetime import date
import pandas as pd
import json
import pymongo
today = str(date.today())

def get_news():
	import requests as r
	url="https://news-headlines.tradingview.com/headlines/yahoo/?category=bitcoin&locale=en&proSymbol=BITTREX%3ABTCUSDT"
	d=r.get(url)
	pprint(d)
	d=d.json()
	return d
#print(d[-1]['shortDescription'])
#p=get_news()

#results = []
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sia = SIA()

#for line in d:
def sentiment_analysis(line):
	pol_score = sia.polarity_scores(line['title'])
	pol_score['date']=today
	pol_score['id']=line['id']
	pol_score['shortDescription']=line['shortDescription']
	pol_score['source']=line['source']
	pol_score['published']=line['published']
	pol_score['link']=line['link']
	pol_score['headline'] = line['title']
	return pol_score

def sentiment():
	for i in p:
		post=sentiment_analysis(i)
		h=db.news.find_one({'headline':post['headline']})
		if h != None:
			if h['headline'] != post['headline']:
				q=db.news
				q=q.insert_one(post).inserted_id
				print(q)
		else:
			q=db.news
			q=q.insert_one(post).inserted_id
			print(q)


def decision(p):
	if p >=0.0151:
		s="POSITIVE"
	elif p<=-0.0151:
		s="NEGATIVE"
	else:
		s="NEUTRAL"
	return s



def todays_sentiment():
	h=list(db.news.find().sort("_id", pymongo.DESCENDING).limit(1))[0]
	d=h['date']
	k=list(db.news.find({'date':d}))
	length=len(k) 
	r=pd.DataFrame(k)
	r=r['compound'].mean()
	return r
def today_sentiment():
	h=list(db.news.find().sort("_id", pymongo.DESCENDING).limit(1))[0]
	d=h['date']
	k=list(db.news.find({'date':d}))
	length=len(k) 
	r=pd.DataFrame(k)
	r=r['compound'].mean()
	r=decision(r)
	return r


