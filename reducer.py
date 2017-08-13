# This is the Reducer function
# Takes the Mappers <key, value> pairs and summarizes to a single result 
# displaying the top hotness songs for each continent

#!/usr/bin/env python

import sys
import json
import ast

# Initiating the top lists for each continent
topEurope = [[" "," ", 0],[" "," ", 0],[" "," ", 0],[" "," ", 0],[" "," ", 0]]
topNAmerica = [[" "," ", 0],[" "," ", 0],[" "," ", 0],[" "," ", 0],[" "," ", 0]]
topSAmerica = [[" "," ", 0],[" "," ", 0],[" "," ", 0],[" "," ", 0],[" "," ", 0]]
topAsia = [[" "," ", 0],[" "," ", 0],[" "," ", 0],[" "," ", 0],[" "," ", 0]]
topAfrica = [[" "," ", 0],[" "," ", 0],[" "," ", 0],[" "," ", 0],[" "," ", 0]]


for line in sys.stdin:
	line = line.strip()

        # The JSON object from Mapper
	location = line.split("\t")[1]
        # The continent name (string) from Mapper
	objTemp = line.split("\t")[0]

        # Load to JSON object from string
	obj = json.loads(objTemp)


	if location == "EUROPE":
		for i, value in enumerate(topEurope):
                        # Checks If current song's hotness is larger than any of the ones already stored in list 
			if (obj.get('hotness') > topEurope[i][2]):
                                # If so, remove the song with lowest hotness value
				topEurope.remove(min(topEurope, key=lambda x:x[2]))
                                # Insert the current song instead
				topEurope.append([obj.get('song_title'), obj.get('artist_name'), obj.get('hotness')])
			break

	if location == "NORTH AMERICA":
                for i, value in enumerate(topNAmerica):
                        if (obj.get('hotness') > topNAmerica[i][2]):
                                topNAmerica.remove(min(topNAmerica, key=lambda x:x[2]))
                                topNAmerica.append([obj.get('song_title'), obj.get('artist_name'), obj.get('hotness')])
			break

	if location == "SOUTH AMERICA":
                for i, value in enumerate(topSAmerica):
                        if (obj.get('hotness') > topSAmerica[i][2]):
                                topSAmerica.remove(min(topSAmerica, key=lambda x:x[2]))
                                topSAmerica.append([obj.get('song_title'), obj.get('artist_name'), obj.get('hotness')])
			break


        if location == "ASIA":
                for i, value in enumerate(topAsia):
                        if (obj.get('hotness') > topAsia[i][2]):
                                topAsia.remove(min(topAsia, key=lambda x:x[2]))
                                topAsia.append([obj.get('song_title'), obj.get('artist_name'), obj.get('hotness')])
                        break

        if location == "AFRICA":
                for i, value in enumerate(topAfrica):
                        if (obj.get('hotness') > topAfrica[i][2]):
                                topAfrica.remove(min(topAfrica, key=lambda x:x[2]))
                                topAfrica.append([obj.get('song_title'), obj.get('artist_name'), obj.get('hotness')])
                        break


# These are just printing functions for making the result file look a bit nicer
 
print("Top Songs For European Artists")
print("\n")
for i, value in enumerate(topEurope):
        print("Artist name: " + str(topEurope[i][1].encode('utf-8').strip()) + "\n" + "Song Name: " + str(topEurope[i][0].encode('utf-8').strip()) + "\n" + "Hotness: " + str(topEurope[i][2]))
print("\n")
print("Top Songs For North American Artists")
print("\n")
for i, value in enumerate(topNAmerica):
        print("Artist name: " + str(topNAmerica[i][1].encode('utf-8').strip()) + "\n" + "Song Name: " + str(topNAmerica[i][0].encode('utf-8').strip()) + "\n" + "Hotness: " + str(topNAmerica[i][2]))
print("\n")
print("Top Songs For South American Artists")
print("\n")
for i, value in enumerate(topSAmerica):
        print("Artist name: " + str(topSAmerica[i][1].encode('utf-8').strip()) + "\n" + "Song Name: " + str(topSAmerica[i][0].encode('utf-8').strip()) + "\n" + "Hotness: " + str(topSAmerica[i][2]))
print("\n")
print("Top Songs For Asian Artists")
print("\n")
for i, value in enumerate(topAsia):
        print("Artist name: " + str(topAsia[i][1].encode('utf-8').strip()) + "\n" + "Song Name: " + str(topAsia[i][0].encode('utf-8').strip()) + "\n" + "Hotness: " + str(topAsia[i][2]))
print("\n")
print("Top Songs For African Artists")
print("\n")
for i, value in enumerate(topAfrica):
        print("Artist name: " + str(topAfrica[i][1].encode('utf-8').strip()) + "\n" + "Song Name: " + str(topAfrica[i][0].encode('utf-8').strip()) + "\n" + "Hotness: " + str(topAfrica[i][2]))
print("\n")




