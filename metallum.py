#!/usr/bin/python
import sys
import argparse
import re
import json
from urllib import urlopen, urlencode

site_url = 'http://www.metal-archives.com/'
lyric_id_re = re.compile(r'id=.+[a-z]+.(?P<id>\d+)')
band_name_re = re.compile(r'title="(?P<name>.*)\"')
tags_re = re.compile(r'<[^>]+>')

def get_song_data(band, song):
    """Search on metal-archives for song coincidences"""
    params = dict(
        bandName = band,
        songTitle = song
    )
    url = "".join([site_url, "search/ajax-advanced/searching/songs?", urlencode(params)])
    return json.load(urlopen(url))['aaData']

def get_lyrics_by_song_id(song_id):
    """Search on metal-archives for lyrics based on song_id"""
    url = "".join([site_url, "release/ajax-view-lyrics/id/", song_id])
    return tags_re.sub('', urlopen(url).read().strip())

def main():
    """Runs the program and handles command line options"""
    parser = argparse.ArgumentParser(description='Get lyrics from http://metal-archives.com')
    parser.add_argument('band', type=str, help='The name of the band. Ex: "Dark Reality"')
    parser.add_argument('song', type=str, help='The title of the song. Ex: "Mopin Carol"')
    args = parser.parse_args()

    song_data = get_song_data(args.band, args.song)

    if len(song_data):
        data = song_data[0] # use the first coincidence
        song_id = lyric_id_re.search(data[4]).group("id")
        band_name = band_name_re.search(data[0]).group("name")
        song_title = data[3]

        title = "".join([band_name, " - ", data[3], "\n"]).decode('utf-8')
        lyrics = get_lyrics_by_song_id(song_id).decode('utf-8')

        print "".join([title, "\n", lyrics])
    else:
        return sys.exit("Lyrics not found")

if __name__ == '__main__':
    main()
