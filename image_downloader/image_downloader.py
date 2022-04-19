import json
import sys
from os.path import exists

import requests

baseUrl = 'http://idicolorz.it/picture/export-image/?artist={}&year={}&id={}'


def download(path):
    f = open(path, "r")
    data = json.load(f)
    length = len(data)
    for n, i in enumerate(data):
        artist = i['Artist'].lower().replace(' ', '-')
        year = i['Year']
        id = i['Picture_ID']
        title = i['Title']
        image_url = baseUrl.format(artist, year, id)
        print('downloading picture {}, from {}'.format(str(n+1) + '/' + str(length), image_url))
        img_data = requests.get(image_url).content
        with open( title.replace(' ', '_') + '_' + str(id) + '.jpg', 'wb') as handler:
            handler.write(img_data)


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 2 and exists(sys.argv[1]):
        download(sys.argv[1])
    else:
        print('to execute this script pass as argument the path of the picture.json file')


