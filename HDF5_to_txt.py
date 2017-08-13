# This is the script for transfearing all HDF5 files to JSON objects stored in a text file

#!/usr/bin/env python

import os
import glob
import hdf5_getters
import json

def get_info(basedir,ext='.h5') :
    # Create new text file for storing the result of JSON objects
    resultFile = open("result.txt", "w")
    # Going through all sub-directories under the base directory
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            # Open the HDF5 for reading the content
            h5 = hdf5_getters.open_h5_file_read(f)
            # Creating dictionary to convert to JSON object
            dictionary = {} 
            # Storing all fields 
            dictionary["song_title"] = hdf5_getters.get_title(h5).decode('Latin-1')
            dictionary["artist_name"] = hdf5_getters.get_artist_name(h5).decode('Latin-1')
            dictionary["key"] = float(hdf5_getters.get_key(h5))
            dictionary["minor-major"] = float(hdf5_getters.get_mode(h5))
            dictionary["hotness"] = hdf5_getters.get_song_hotttnesss(h5)
            dictionary["artist_location"] = hdf5_getters.get_artist_location(h5).decode('Latin-1')
            dictionary["longitude"] = float(hdf5_getters.get_artist_longitude(h5))
            dictionary["latitude"] = float(hdf5_getters.get_artist_latitude(h5))
            print(dictionary)
            # Write the created JSON object to the text file
            resultFile.write(str(json.dumps(dictionary)) + "\n")
            h5.close()
    resultFile.close()

# Main function for initiating the script
if __name__ == "__main__":
    listTemp = get_info("MillionSongSubset\data\A\B")
