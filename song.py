# from __future__ import print_function # for python 2

class Song:
    """Class to represent a song
    
    Attributes:
        title (str): Title of a song
        artist(Artist): An Artist object representing the song's creator
        duration(int): The duration of song in seconds. Can be 0
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration
        # print("New song added:"
        # f"\n'{title}' by {artist}, duration: {duration} seconds")


class Album:
    """Class to represent an Album using it's tracklist
    
    Attributes:
        name(str): Name of the album
        year(int): Year the album was released
        artist(Artist): The artist responsible for the album.If not specified, 
            the artist defaulted to artist with the name "Various Artist"
        tracks(List[Song]): A list of songs on the album
    Methods: 
        add_song: Used to add a new song to the album's tracklist
    """

    def __init__(self, name, year, artist=None) -> None:
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various artists")
        else:
            self.artist = artist

        self.tracks = []
        # print("Created a new album:"
        # f"\n{name} by {artist}")

    def add_song(self, song, position=None):
        """Adds a song to the tracklist

        Args:
            song (Song): A song to add
            position (int, optional): If specified, the song will be added to that position
                in the tracklist - inserting song in between other songs if necessary.
                Defaults to None.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details

    Attributes:
        name(str): Name of the artist
        albums(List[album]): A list of albums by the artist
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums
    Methods:
        add_album: used to add new album to artist's album list
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


def find_object(field, object_list):
    """Check object_list to see if an object with 'name' attribute equal to 'field' exists, return if it does"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    with open('albums.txt', 'r') as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field))
            
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # we've just read details for a new artist
                # retreive the artist object if there is one
                ## otherwise, create new object and add it to the artist_list
                new_artist =  find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)    
                new_album = None
            
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)

            elif new_album.name != album_field:
                # we've just read a new album for the current artist
                # retreive the album object if there's one
                # otherwise, create a new album object and store it in the artist's collection
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # create a new song object and add that to the current album collection
            new_song = Song(song_field, new_artist) 
            new_album.add_song(new_song)
        
    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for the comparision with the original file
    """
    with open('checkfile.txt', 'w') as check_file:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                    file=check_file)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))
    create_checkfile(artists)