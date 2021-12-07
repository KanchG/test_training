from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests
import json

client = MongoClient('mongodb+srv://kanchana:<password>@cluster0.uyrxb.mongodb.net/<dbname>?authSource=admin&replicaSet=atlas-l4lhjf-shard-0&w=majority&readPreference=primary&retryWrites=true&ssl=true')
db = client.latestNews
#MongoDB connection made

def get_news_list():
	url = "https://www.thehindu.com/latest-news/"
	req = requests.get(url)
	soup = BeautifulSoup(req.text, "html.parser")
	#using web scrapping to collect data
	news1=[]
	for uls in soup.find_all('ul',class_='latest-news'):
		count = 1
		newslist = uls.find_all("li")
		#collecting only first 10 news from webpage
		for i in newslist[0:10]:
			#collecting only the required data by excluding the html tags
			link = i.select_one('a')['href']
			time = i.select_one('span.l-datetime').text
			name = i.select_one('span.homeSection-name').text
			#creating dict from the news collected
			news = {
			"news_time" : time,
			"news_tag" : name,
			"news_link" : link
			}
			#filling up the DB with latest_news using insert_one query
			record = db.latestNews.insert_one(news)
	print('Latest News collected Successfully!')

def read_news(given_tag):
	#check for requested tag to be read from DB
	search_list = db.latestNews.find({"news_tag": given_tag})
	for i in search_list:
		#print collection in dict type
		print("Dict type output:"+"\n")
		print(i)
		json_news = json.dumps(i, default=str)
		print("\n")
		print("JSON output:"+"\n")
		#print the same in JSON
		print(json_news)
		print("\n")

#create new DB and save data
get_news_list()
#read filtered data by tag name
#please change tag name to verify
read_news("National")
read_news("Kerala")
