import Secret
import lyricsgenius
import time
import streamlit as st
import numpy as np
import pandas as pd
import json
import os


def get_lyrics(artist):
    # Create and Configure Scraper
    genius = lyricsgenius.Genius(Secret.GENIUS_ACCESS_TOKEN)
    genius.verbose = True
    genius.remove_section_headers = False
    genius.skip_non_songs = True
    genius.excluded_terms = ["(Remix)", "(Snippet)"]

    # Create Artist Object, including all Songs
    result = genius.search_artist(artist, sort="title")
    artist.result()


def process_data(file):
    with open(file) as json_file:
        data = json.load(json_file)
    print(data)
    # Now somehow Process the data :)


if __name__ == "__main__":
    # execute only if run as a script
    artist_list = ["Kollegah", "Ufo361"]

    for artist in artist_list:
        file = "Lyrics_{}.json".format(artist)
        if not os.path.isfile(file):
            get_lyrics(artist)
        process_data(file)




