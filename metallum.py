#!/usr/bin/env python
import sys
import argparse
import re
import json
from urllib import urlopen, urlencode

site_url = 'http://www.metal-archives.com/'
lyrics_not_available = '(lyrics not available)'
lyric_id_re = re.compile(r'id=.+[a-z]+.(?P<id>\d+)')
band_name_re = re.compile(r'title="(?P<name>.*)\"')
tags_re = re.compile(r'<[^>]+>')

def get_songs_data(band, song):
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
    return tags_re.sub('', urlopen(url).read().strip()).decode('utf-8')

def iterate_songs_and_print(songs):
    '''Iterate over returned song matches. If the lyrics are different than\
    "(lyrics not available)" then break the loop and print them out.\
    Otherwise the last song of the list will be printed.'''
    for song in songs:
        band_name = band_name_re.search(song[0]).group("name")
        song_title = song[3]
        song_id = lyric_id_re.search(song[4]).group("id")
        lyrics = get_lyrics_by_song_id(song_id)
        if lyrics != lyrics_not_available:
            break

    title = "".join([band_name, " - ", song_title, "\n"])
    sys.exit("".join(["\033[4m", title, "\n\033[0m", lyrics, "\n"]))

def main():
    """Runs the program and handles command line options"""
    parser = argparse.ArgumentParser(description='Get lyrics from http://metal-archives.com')
    parser.add_argument('band', type=str, help='The name of the band. Ex: "Dark Reality"')
    parser.add_argument('song', type=str, help='The title of the song. Ex: "Mopin Carol"')
    args = parser.parse_args()

    songs_data = get_songs_data(args.band, args.song)

    if len(songs_data):
        iterate_songs_and_print(songs_data)

    sys.exit("\n\033[031m Lyrics not found\n")

if __name__ == '__main__':
    main()
