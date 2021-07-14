# This script moves the data from the unzipped .csv files
# into the postgresql database

import os
import urllib.request

S3_ENDPOINT = os.environ.get("S3_ENDPOINT")
BUCKET_NAME = os.environ.get("BUCKET_NAME")

BUCKET_ROOT_URL = S3_ENDPOINT + '/swift/v1/' + BUCKET_NAME + '/'

def fetch_url(url):
    response = urllib.request.urlopen(url)
    return response.read().decode('utf-8')

def parse_csv_file(csv_data):
    rows = csv_data.split('\n')
    parsed_data = map(lambda row : row.split(','), rows)
    return list(parsed_data)


def parse_files(files):
    file_names = files.split('\n')
    for file_name in file_names:
        if (file_name.endswith('.csv')):
            data = fetch_url(BUCKET_ROOT_URL + file_names[0])
            print(parse_csv_file(data))

print('Fetching csv file list...')
files = fetch_url(BUCKET_ROOT_URL)
print('Parsing csv files...')
parse_files(files)