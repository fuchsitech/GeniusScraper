import Secret
import lyricsgenius

genius = lyricsgenius.Genius(Secret.GENIUS_ACCESS_TOKEN)
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
print(artist.songs)
