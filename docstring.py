
# ====================================================
# Docstrings and Raw literals
# ====================================================

# ============
# Docstrings:
# ============

# Docstrings are used for commenting your code. They are enclosed in three doublequotes """  docstring """
# Here is a code in class "Song" that is commented with Docstrings

# Miltiline docstrings:
# =====================
# docscrings like one below containing many lines in the description
# First line of a Multiline docstring should have a summary of the description e.g "Class to represent a song"
# then we can have attributes and argument details as shown

# One of the uses of well described docstrings is to provide help using "help" function
# in this case, we will type "help(Song)" and it will show you what class "Song" is all about

# The logic for this code is in Flowchart_1

class Song:
    """  Class to represent a song

    Attributes:
        title (str): The title of the song is a string
        artist (artist): An artist object representing the songs creator
        duration(int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """ Song init method

        Args:
            title(str): initializes the 'title' attribute
            artist(artist): An artist object representing the song's creator
            duration(Optional)(int): Initial value for the 'duration attribute'.
                Will default to zero if not specified
        """

        self.title = title
        self.artist = artist
        self.duration = duration

    def sing(self):
        print("This is a method without docstring description. We will add it later")


# This shows you the descriptions of class Song
# Output here shows description for the whole class "Song"

help(Song)

print("="*40)

# We can also request help for a particular method
# NOTE: we will not all the init method using "Song.__init__(), but will just request some info on it using "Song.__init__" without ()
# This gives info about the init method only and not the whole class "Song"

help(Song.__init__)

print("="*40)

# ==================
# using __doc__
# ==================
# NOTE: __doc__ represents "docstring" and is used to pull what is written in docstring descriptions

# You can also get help info about the class "Song" by print(Song. __doc__) attribute
# It only gives result for Class "Song" because we only specified Song in the pring

print("print(Song.__doc__)")
print(Song.__doc__)

print("="*40)

# If we specify Song.__init__, it will show description info for Song.__init__

print("print(Song.__init__.__doc__)")
print(Song.__init__.__doc__)

print("="*40)

# =============================================
# using __doc__ to add docstring description
# =============================================

# You can use below command to add docstring, although this method is not recommended.
# We see the description is added to function sing

# Code to add descriotion using __doc__

Song.sing.__doc__ = """  Description added to sing using __doc__ """

print("print(Song.sing.__doc__):")
print(Song.sing.__doc__)
print("="*40)


# ==========================================
# Album Class to store songs
# ==========================================

# We will make an Album class to store the songs that make up an album
# Then create its docstring to describe it.

class Album:
    """ Class to represent an album, using its track list

    Attributes:
        name (str): The name of the album
        year (int): The year album was released.
        artist (Artist): The artist responsible for the album, if not specified,
        the artist will default to an artist with the name "various artists".
        tracks (List[songs]): A list of the songs on the album

    Methods:
        add_song: Used to add a new song to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")  # Artist class is defined below
        else:
            self.artist = artist

        self.tracks = []  # We save tracks here. NOTE that tracks don't have to be under __init__, we create them when we initialize


    def add_song(self, song, position=None):
        """ Adds a song to the track list

        Args:
            song (Song): A song to add
            position (Optional[int]): if specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise the song will be added to the end of the list
        """

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)  # inserts the position and song in self.tracks list


class Artist:
    """ Basic class to store artist details

    Attributes:
        name (str): The name of the artist
        albums (List[Album]): A list of the albums by this artist.
            The list contains only those albums in this collection. It is
            not an exhaustive list of the artists published albums.

    Methods:
        add_album: Use to add a new album to the artist's album list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []  # Album list created and initialized here with empty list

    def add_album(self, album):
        """ Add a new album to the list

        Args:
            album (Album): Album object to add to the list
                if the album is already present, it will not be added again (Although this is yet to be implemented)
        """

        self.albums.append(album)

# NOTE: We have circular reference here which can cause some trouble reclaiming memory that is not used
# This is remedied using "Garbage Collection". We will read about it further
# See picture circular_reference.jpg under 34_OOP to see about circular reference where classes are stored and referenced
# by each other in a circular form.

# NOTE: we downloaded albums.txt and put it in 34_OOP folder and will be using it
# you can double click albums.txt on the left to see its content.


# We will now create a function to load album.txt data and call it only if the program is
# executed as a script i.e. run within this program i.e. __name__ == __main__

def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            # This print shows the four field variables that we have made
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            # Method 1: of putting data from albums.txt into the classes
            # As each row of the data in albums.txt is read, we will create a "song" object and add it to the "album"
            # When a new "album" is found in the data, the current "album" will be stored in the "artist" album list
            # and a new album object created with that current rows details.

            # When a record for a new "artist" is read, the current artist will be saved in the "artist" list
            # And new "artist" object will be created with data in the current row.

            # We will put all the code to populate all the objects from the data file in a function and then that function
            # will return a list of artist objects when it finishes processing the file.

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:  # Meaning we've just read details of a new_artist
                # We store current album in the current artists collection, then create a new_artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)  # Create new_artist field using Artist Class
                new_album = None   # The new_artist created initially has no albums, hence initialized with None

            # Now we create new_album for the new_artist created
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)  # We create new album
            elif new_album.name != album_field:  # Meaning we just read a new album for current artist
                # Store current album in the artist collection then create a new_album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)


            # Now we create a new song object and add it to the current album collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After reading the last line in the text file, we will have an artist and album that has not been stored
        # We will store them now.
        # NOTE: If both new_artist and new_album is not None, then we have reached the end of the albums.txt
        # NOTE that indentation is alligned with for loop above. So after for loop processes all the above code, it will
        # then process this one.

        # NOTE that in the above approach, the objects are not stored in the collection until a new record is read from the file
        # For example, current album is added to the artist album list when a record containing a different album is read.
        # This is why the last set of data will not be stored and we need to add it with this code here.

        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    # Then we return the artist list that we have created from this code.
    return artist_list


# Verifying number of artists
# output from "print("There are {} artists".format(len(artists)))" below shows there are 28 artists.
# We can verify if this is true or not by creating a new file named "checkfile.txt" and then comparing it with
# original file "albums.txt"

# Create "checkfile.txt" by writing to it.

def create_checkfile(artist_list):
    """ Create a check file from the object data for comparison with the original file """
    with open("checkfile.txt", 'w') as checkfile:  # we are creating new file named checkfile, hence method r for write
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)

                    # NOTE: python 2 does not allow print above where you have {0.name} etc
                    # To run this pring format in python 2, you need to import print_function at the top of code using:
                    # from __future__ import print_function

# we will then call "create_checkfile" under the last code to get result


# Now we test if its called as a script
# And it will print all the songs in albums.txt
# NOTE: We use this code to call load_data() and run this line:
# print("{} : {} : {} : {}".format(artist_field, album_field, year_field, song_field))

# if __name__ == "__main__":
#     load_data()


# for other part of load_data() starting with "if new_artist is None", we use this code

if __name__ == '__main__':
    artists = load_data()  # prints data in format: artist_field, album_field, year_field, song_field
    print("There are {} artists".format(len(artists))) # Counts the number of artists

    create_checkfile(artists)  # we give it artists parameters that we got from above code and it will create new checkfile.txt

# ========================
# Compare files
# ========================

# You can compare "albums.txt" and "checkfile.txt" using two methods:

# Method 1:
# Click both albums.txt and checkfile.txt > View > Compare files
# It will pull up a window with both files and say "No difference" if they are same.
# it will also show you if there are any differences

# Method 2:
# Click albums.txt > View > Compare with > Choose checkfile.txt > Ok
# It will give you similar window with comparison
# This is useful if you are comparing files in different projects and want to navigate to the new project.

# ====================================================
# Comparing unordered data
# ====================================================

# In this code, we see that it shows number of artists to be 28
# We will modify original albums file to have unordered list of data and see what happens
# See docstring2.py

