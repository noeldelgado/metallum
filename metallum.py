#!/usr/bin/env python
import sys
import argparse
import re
import json
from urllib import urlopen, urlencode

_site_url = 'http://www.metal-archives.com/'

def _get_song_data(band, song):
    """Search on metal-archives for song coincidences"""
    song_params = dict(
        bandName = band,
        exactBandMatch = 1,
        songTitle = song,
        exactSongMatch = 1
    )
    song_params = urlencode(song_params)
    song_url = _site_url + "search/ajax-advanced/searching/songs?" + song_params
    return json.load(urlopen(song_url))['aaData']

def _get_lyrics_by_song_id(song_id):
    """Search on metal-archives for lyrics based on song_id"""
    tags_re = re.compile(r'<[^>]+>')
    lyrics_url = _site_url + "release/ajax-view-lyrics/id/%s" % (song_id)
    lyrics_response = urlopen(lyrics_url)
    lyrics = lyrics_response.read().strip()
    lyrics = tags_re.sub('', lyrics) + "\n"
    return lyrics

def main():
    """Runs the program and handles command line options"""
    parser = argparse.ArgumentParser(description='Get lyrics from http://metal-archives.com')
    parser.add_argument('band', type=str, help='The name of the band. Ex: "Dark Reality"')
    parser.add_argument('song', type=str, help='The title of the song. Ex: "Mopin Carol"')
    args = parser.parse_args()

    song_data = _get_song_data(args.band, args.song)
    if len(song_data) :
        id_re = re.compile(r'id=.+[a-z]+.(\d+)')
        song_id = id_re.search(song_data[0][4]).group(1)
        print _get_lyrics_by_song_id(song_id)
    else :
        return sys.exit("Lyrics not found")

if __name__ == '__main__':
    main()
