class Song:
    """entries a song, the artist, the duration of the song and the album and year it was from

    Attributes:
        title(str): name of the song
        artist(Artist): Artist object that is responsible for this song
        album(Album): Album this song is from
        year(int): When was this song  released
    Method:
        __init__
    """
    def __init__(self, title, album, artist, year) -> None:
        self.name = title
        self.album = album
        self.artist = artist
        self.year = year


class Album:
    """for creating an Album object

    Attributes:
        name(str): Name of the album    
        artist(Artist): Artist object that  is responsible for this song
        tracks(List[Song]): tracklist in the album
    Methods:
        add_song: adds a song to the album
    """
    
    def __init__(self, name, artist) -> None:
        self.name = name
        self.artist = Artist("Various artists")
        self.tracks = []

    def add_song(self, track, position=None):
        """Adds a song to the tracklist at a required position

        Args:
            track (str): The song that needs to be added. If the song isn't already in the album.
            position(int): The position where the song needs to be added. Defaulted to the end of the album
        """
        if track not in self.tracks:
            if position is None:
                self.tracks.append(track)
            else:
                self.tracks.insert(position, track)
    

class Artist:
    """Takes a record of artist's name and their albums list
    
    Attributes:
        name(str): Name of the artist
        album_list(List[Album]): list of albums of that artist
    Methods:
        add_album: Adds the album in the album_list if the album isn't there already.
    """
    def __init__(self, name) -> None:
        self.name = name
        self.album_list = []

    def add_album(self, album):
        if album not in self.album_list:
            self.album_list.append(album)


def find_object(field, object_list):
    """Check the object_list to see if an object with the 'name' attribute equal to the 'field' exists, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    """Loads data from a text file and converts it into a tuple with fields:
    artist_field, album_field, 
    """
    with open("albums.txt", 'r') as fields:
        for line in fields:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            print(f"{artist_field} {album_field} {year_field} {song_field}")


if __name__ == "__main__":
    load_data()