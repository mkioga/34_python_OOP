
# ===============================================================
# Writing Song class in Object Oriented Programming (OOP) Format
# ===============================================================

# OOP uses classes and function but it also includes concepts like:
# Encapsulation - putting data and method in one function
# Composition -
# Inheritance -
# Delegation - involves passing responsibility for a task to another object that is better suited to do it.

# This code is now functioning using OOP approach
# Its now easier to understand and easier to modify without introducing bugs
# It delegates tasks to other objects hence keeping them simpler and more focused on a single task.



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

        self.name = title  # NOTE we add title to self.name instead of self.title because we use "if item.name == field" under function "find_objects"
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
            song (Song): The title of a song to add
            position (Optional[int]): if specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise the song will be added to the end of the list
        """

        # Use find_object to see if the song exist already.
        song_found = find_object(song, self.tracks)  # look for song.tracks to see if it exist in the list
        if song_found is None:  # if song is not found
            song_found = Song(song, self.artist)  # We create new song using "Song" function and assign it to song_found
            if position is None:  # If there are no songs in this track
                self.tracks.append(song_found)  # Add this song_found in the first position
            else:  # else if there are already some songs in the track
                self.tracks.insert(position, song_found)  # inserts the position and song in self.tracks list


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

    # We create add_song method here to be used in load_data
    def add_song(self, name, year, title):
        """ Add a new song to the collection of albums

        This method will add the song to an album in the collection
        A new album will be created in the collection if it doesn't already exist

        Args:
            name(str): The name of the album
            year(int): The year the album was produced.
            title(str): The title of the song
        """

        # Here we check if album exist under artist.
        album_found = find_object(name, self.albums)
        if album_found is None:  # If there is no album found
            print(name + "not found")  # we print "Album name not found
            album_found = Album(name, year, self)  # Create new album using "Album" function and assign it to album_found variable
            self.add_album(album_found)  # We add new_album to song.
        else:  # if we found an existing album with same name
            print("found album" + name)  # we print found album name

        # so we add song to album_found
        album_found.add_song(title)



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
# modify load_data function to make it OOP
# ============================================================


def load_data():
    artist_list = []

    with open("albums2.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            # This print shows the four field variables that we have made
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            # We will check if artist exist in the artist list (See  flowchart3.jpg)
            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:  # if we do not find new_artist in the list
                new_artist = Artist(artist_field)  # we create the new_artist in the Artist field
                artist_list.append(new_artist)  # Then we append the created new_artist into the artist_list

            # Then we add a song to the new_artist we just created
            # NOTE: We use the "add_song" method which was created above under class "Artist"
            new_artist.add_song(album_field, year_field, song_field)


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
                for new_song in new_album.tracks:  # NOTE: we use 2.name below instead of 2.title because of "self.name = title" under class Song
                    print("{0.name}\t{1.name}\t{1.year}\t{2.name}".format(new_artist, new_album, new_song),
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
