class Song:
    """Class to represent a song
    
    Attributes:
        title (str): Title of a song
        artist(str): name of the song's creator
        duration(int): The duration of song in seconds. Can be 0
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """Class to represent an Album using it's tracklist
    
    Attributes:
        name(str): Name of the album
        year(int): Year the album was released
        artist(str): The name of the artist responsible for the album.If not specified, 
            the artist defaulted to artist with the name "Various Artist"
        tracks(List[Song]): A list of songs on the album
    Methods: 
        add_song: Used to add a new song to the album's tracklist
    """

    def __init__(self, name, year, artist=None) -> None:
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the tracklist

        Args:
            song (Song): The title of a song to add
            position (int, optional): If specified, the song will be added to that position
                in the tracklist - inserting song in between other songs if necessary.
                Defaults to None.
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:    
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """Basic class to store artist details

    Attributes:
        name(str): Name of the artist
        albums(List[album]): A list of albums by the artist
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums
    Methods:
        add_album: used to add new album to artist's album list
        add_song: Adds a song to the album of that artist
    """

    def __init__(self, name) -> None:
        self.name = name
        self.albums = []
    
    def add_album(self, album):
        """Add new album to the list

        Args:
            album (Album): An Album object added to the list:
            if the album is already present, it will not be added again. (although it is yet to be implemented) 
        """
        self.albums.append(album)
    
    def add_song(self, name, year, title):
        """Add a new song to the collection of albums
        This method will add the song to an album in the collection.
        A new album will be created in the collection if it doesn't already exist
        Args:
            name (str): name of the album
            year (int): year the album was produced
            title (str): title of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + "Not found")
            album_found = Album(name, year, self.name)
        else:
            print("Found album" + name)

        album_found.add_song(title)


def find_object(field, object_list):
    """Check object_list to see if an object with 'name' attribute equal to 'field' exists, return if it does"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

        
    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for the comparision with the original file
    """
    with open('checkfile.txt', 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.name}".format(new_artist, new_album, new_song),
                    file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists))) 
    create_checkfile(artists)
