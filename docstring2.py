
# ====================================================
# Comparing unordered data
# ====================================================

# We will cut some data in albums2.txt for "ZZ top" and move them to a different spot on the file
# Say within "Aerosmith" betwen "Permanent Vacation" and "Gems"
# so we are putting the data in a different order

# Now when you run this code, we see it shows 31 artists instead of 28.
# When we compare contents of albums2.txt and checkfile2.txt (Highlight both > View > Compare files)
# It still says they are identical.

# ==================
# Cause of problem:
# ==================
# The cause of this problem is that each artist boundary (from one artist to another)
# causes a new artist object to be created without considering whether there is already an object for that artist
# So we end up with two artist objects for "Aerosmith" and two for "ZZ Top"

# ==========
# Solution:
# ==========

# A solution is to check whether there is an artist object for the artist before creating a new object one for that artist
# We also check if there is an album object for the album before creating a new album object whenever a new album is found


# ============
# Flowchart-1
# ============
# This is how this original code (docstring.py) runs
# Saves existing artist and creates new artist immediately it encounters a new artist.
# Saves existing album and creates new album immediately it encounters a new album.

# ============
# Flowchart-2
# ============
# It encounters new artist, it creates new artist object, then saves artist object
# this means an artist will be added to the list before any albums are added to it.
# It encounters new album, it creates new album object, then saves album object
# This means an album will be added to the artist list before any songs are added to it.

# If we were using a database to store these details, that means that if something goes wrong, we could end up with
# albums in the database with some songs missing
# But in this case, the code is simple and fits in memory and we can see it all, so nothing to worry

# ============
# Flowchart-3
# ============
# It encounters new artist, Checks if that new artist already exist, it creates new artist object, then saves artist object
# It encounters new album, checks if that new album already exist, it creates new album object, then saves album object

# =====================
# find_object function
# ======================
# we see that the function to check if new artist and new album already exist are identical, so we can use a function to do that
# We will create a function called "find_object" to do that

# ==========
# Run code
# ==========
# After code has been revised, delete checkfile2.txt (Rightclick it > Delete > Do refactor) and then run the code again

# ========================
# Results of running code
# ========================

# When we run this code, we get 29 artists (should get 28)
# Also when you compare albums2.txt with checkfile2.txt, you see there are differences
# These differences are not about content but because they are ordered differently




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



# =======================
# find_object function
# =======================

# This find_object function will work with both "artist" and "album"
# it checks the name attribute for all lines and returns that name attribute if it finds one, otherwise returns None

def find_object(field, object_list):
    """ Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists
        return it if found
        otherwise return None
    """
    for item in object_list:    # We will iterate through all the items in object_list
        if item.name == field:  # if item.name is same as field (a parameter passed to this method)
            return item         # we return that item that was found

    return None  # Otherwise return None if item.name is not found in fields


# ============================================================
# modify load_data function to work with find_object function
# ============================================================
# Changes are labeled Change1, Change2 etc

def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums2.txt", "r") as albums:
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
                artist_list.append(new_artist)  # Change1: We append new artist to artist list
            elif new_artist.name != artist_field:  # Meaning we've just read details of a new_artist
                # Change2: We retrieve the artist object if there is one:
                # Change3: Otherwise create a new artist object and add it to the artist list:
                new_artist = find_object(artist_field, artist_list)  # Change2: use find_object function and give it parameters to see if it can find them

                if new_artist is None:  # Meaning if it cannot find the artist_field in artist_list
                    new_artist = Artist(artist_field)  # Change3: Create new_artist field using Artist Class
                    artist_list.append(new_artist)  # Then append new_artist to artist_list

                new_album = None   # The new_artist created initially has no albums, hence initialized with None

            # Now we create new_album for the new_artist created
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)  # We create new album
                new_artist.add_album(new_album)  # Change4: We add new album to artist list immediately we create it.

            elif new_album.name != album_field:  # Meaning we just read a new album for current artist
                # Change5: Retrieve the album object if found in album list
                # Change6: if not found, create new album and store it in artists collection of albums
                new_album = find_object(album_field, new_artist.albums)  # Change5: use find_object function to check if album_field is in new_artist.albums list

                if new_album is None:  # if we did not find the new album in our albums list
                    new_album = Album(album_field, year_field, new_artist)  # We create the album using Album function
                    new_artist.add_album(new_album)



            # Now we create a new song object and add it to the current album collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    # =============================================================================================================
    # Change7: We now don't need this code to handle the last song because code changes we made above handles that:
    # =============================================================================================================
        # After reading the last line in the text file, we will have an artist and album that has not been stored
        # We will store them now.
        # NOTE: If both new_artist and new_album is not None, then we have reached the end of the albums.txt
        # NOTE that indentation is alligned with for loop above. So after for loop processes all the above code, it will
        # then process this one.

        # NOTE that in the above approach, the objects are not stored in the collection until a new record is read from the file
        # For example, current album is added to the artist album list when a record containing a different album is read.
        # This is why the last set of data will not be stored and we need to add it with this code here.

        # if new_artist is not None:
        #     if new_album is not None:
        #         new_artist.add_album(new_album)
        #     artist_list.append(new_artist)

    # We will keep this return
    # Then we return the artist list that we have created from this code.
        return artist_list


# Verifying number of artists
# output from "print("There are {} artists".format(len(artists)))" below shows there are 28 artists.
# We can verify if this is true or not by creating a new file named "checkfile.txt" and then comparing it with
# original file "albums.txt"

# Create "checkfile.txt" by writing to it.

def create_checkfile(artist_list):
    """ Create a check file from the object data for comparison with the original file """
    with open("checkfile2.txt", 'w') as checkfile:  # we are creating new file named checkfile, hence method r for write
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

