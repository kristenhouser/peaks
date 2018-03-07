import urllib.request as urllib2
import simplejson
import pymongo
import datahubapi

from pymongo import MongoClient

def main():
	print("starting station import...")
	client = MongoClient('localhost', 27017)
	db = client.geo_attr
	stations = db.stations

	# import all station geographical attributes
	datahubapi.geoAttr_stations(client)

	# iterate through all attributes to import all station details
	for station in stations.find():
		datahubapi.waterquality_station("Station", str(station["StationId"]))	

if __name__== "__main__":
  main()

