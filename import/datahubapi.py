import urllib.request as urllib2
import simplejson
import pymongo

from pymongo import MongoClient

def waterquality_station(geo_attr, attr_id):
	url = "http://datahub.chesapeakebay.net/api.JSON/WaterQuality/Station/" + geo_attr + "/" + attr_id
	print(url)
	response = urllib2.urlopen(url)
	data = simplejson.load(response)
	print(data[0])
	client = client = MongoClient('localhost', 27017)
	db = client.waterquality 
	stations = db.stations
	station_id = stations.insert_one(data[0]).inserted_id
	print(station_id)



	
