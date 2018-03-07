import urllib.request as urllib2
import simplejson
import pymongo

from pymongo import MongoClient

def geoAttr_stations(client):
	url = "http://datahub.chesapeakebay.net/api.JSON/Station/"
	response = urllib2.urlopen(url)
	data = simplejson.load(response)
	db = client.geo_attr
	stations = db.stations
	station_ids = stations.insert_many(data).inserted_ids
	print(station_ids)

def waterquality_station(geo_attr, attr_id):
	url = "http://datahub.chesapeakebay.net/api.JSON/WaterQuality/Station/" + geo_attr + "/" + attr_id
	print(url)
	response = urllib2.urlopen(url)
	data = simplejson.load(response)
	print(data[0])
	client = MongoClient('localhost', 27017)
	db = client.waterquality 
	stations = db.stations
	station_id = stations.insert_one(data[0]).inserted_id
	print(station_id)

def waterquality_monitoringevent(start_date, end_date, program_id, project_id, geo_attr, attr_id):
	url = "/".join(["http://datahub.chesapeakebay.net/api.JSON/WaterQuality/MonitorEvent/", 
			start_date, end_date, program_id, project_id, geo_attr, attr_id])
	print(url)
	response = urllib2.urlopen(url)
	data = simplejson.load(response)
	print(data[0])
	client  = MongoClient('localhost', 27017)
	db = client.waterquality 
	events = db.monitoringevent 
	event_id = events.insert_one(data[0]).inserted_id
	print(event_id)	


	
