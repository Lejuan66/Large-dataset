# This is the Mapper function
# Creates <key, value> pairs where the key is a JSON object storing necessary data and value is the continent name

#!/usr/bin/env python

import sys
import json

# Go through each line from the text file
for line in sys.stdin:
	try:
		# Load the string as an JSON object
		song = json.loads(line)
	except:
		continue

	# Extracting the longitude and latitude values for determining continent
	longitude = song.get('longitude')
	latitude = song.get('latitude')

	# These are the coordinates for Europe
	if ( -9 < longitude < 66) and (36 < latitude < 71.8):
		print("%s\t%s" % (json.dumps(song), "EUROPE"))
	# These are the coordinates for Africa
	if ( -17 < longitude < 52) and (-35 < latitude < 37):
		print("%s\t%s" % (json.dumps(song), "AFRICA"))
	# These are the coordinates for Asia
	if ( 30 < longitude < 180) and (10 < latitude < 70):
		print("%s\t%s" % (json.dumps(song), "ASIA"))
	# These are the coordinates for South America
	if ( 40 < longitude < 80) and (-50 < latitude < 10):
		print("%s\t%s" % (json.dumps(song), "SOUTH AMERICA"))
	# These are the coordinates for North America
	if ( -165 < longitude < -55) and (30 < latitude < 75):
		print("%s\t%s" % (json.dumps(song), "NORTH AMERICA"))
