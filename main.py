import random
import re

# ====================================== #
# Script for parsing the 01.raw.csv file #
# ====================================== #




raw_csv = open('spreadsheets/02_adapted.csv', 'r')
filtered_csv = open('spreadsheets/03_filtered.csv', 'w')

# Aux functions
def grab_data(arr):
    without_links = re.sub(r'http\S+', '', arr[1].lower())
    without_at_dell = re.sub(r'@dell\S+', 'Dell',  without_links)
    without_ats = re.sub(r'@\S+', 'Fulano',  without_at_dell)
    return [arr[0], without_ats.replace('@', '')]


def filter_to_ok(arr):
    return abs(int(arr[0])) == 1




# Read and parse data
lines = filter(filter_to_ok, map(grab_data, [x.split('\t') for x in raw_csv.readlines()]))

# Add data to filtered file
for line in lines:
    filtered_csv.write(line[0] + "\t - " + line[1])

# Close all files
raw_csv.close()
filtered_csv.close()