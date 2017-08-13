#!/usr/bin/env python

import os
import glob
import hdf5_getters
import json

def get_info(basedir,ext='.h5') :
    resultFile = open("result.txt", "w")
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            h5 = hdf5_getters.open_h5_file_read(f)
            dictionary = {} 
            dictionary["song_title"] = hdf5_getters.get_title(h5).decode('Latin-1')
            dictionary["artist_name"] = hdf5_getters.get_artist_name(h5).decode('Latin-1')
            dictionary["key"] = float(hdf5_getters.get_key(h5))
            dictionary["minor-major"] = float(hdf5_getters.get_mode(h5))
            dictionary["hotness"] = hdf5_getters.get_song_hotttnesss(h5)
            dictionary["artist_location"] = hdf5_getters.get_artist_location(h5).decode('Latin-1')
            dictionary["longitude"] = float(hdf5_getters.get_artist_longitude(h5))
            dictionary["latitude"] = float(hdf5_getters.get_artist_latitude(h5))
            print(dictionary)
            resultFile.write(str(json.dumps(dictionary)) + "\n")
            h5.close()
    resultFile.close()

if __name__ == "__main__":
    listTemp = get_info("MillionSongSubset\data\A\B")
    #listHot = sorted(listTemp, reverse=True)
    #print(listHot)
