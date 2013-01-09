#!/usr/bin/env python
import sstg
import athlete_data

link_dict = {"Home":"/"}
DATA_BASE_DIR = "./data/"
ATHLETE_FILE_NAMES = ["sarah2.txt", "james2.txt", "julie2.txt", "mikey2.txt"]

print sstg.start_response()
print sstg.include_header("The international spacecraft challenge!")

new_athlete_filenames = []
athlete_dict = {}

for each_file in ATHLETE_FILE_NAMES:
    new_athlete_filenames.append(DATA_BASE_DIR + each_file)

athlete_data.put_to_store(new_athlete_filenames)
athlete_dict = athlete_data.get_from_store()

print sstg.start_form("POST","/cgi-vin/specific.py")
print sstg.radio_buttons("athletes", athlete_dict.keys())
print sstg.end_form()


print sstg.include_footer(link_dict)

