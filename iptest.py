from geoip import open_database, geolite2

with open_database('GeoLite2-City.mmdb') as db:
	# match = db.lookup_mine()
	match = geolite2.lookup('1.127.48.248')
	print 'My IP:', match
