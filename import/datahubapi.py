import urllib.request as urllib2
import json as simplejson
from pymongo import MongoClient

def waterquality_station(geo_attr, attr_id):
	url = "http://datahub.chesapeakebay.net/api.JSON/WaterQuality/Station/" + geo_attr + "/" + attr_id
	print(url)
	response = urllib2.urlopen(url)
	data = simplejson.load(response)
	print(data)
	client = client = MongoClient('localhost', 27017)
	db = client.peaks 
	collection = db.waterquality 
	stations = db.stations
	station_id = stations.insert_one(data).inserted_id
	print(station_id)



	
