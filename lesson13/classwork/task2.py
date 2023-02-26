from copy import deepcopy


class Song:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.number_of_listens = 0

    def listen(self):
        self.number_of_listens += 1

    def __gt__(self, other):
        if not isinstance(other, Song):
            raise ValueError("The second object must be Song.")

        return self.length > other.length

    def __eq__(self, other):
        if not isinstance(other, Song):
            raise ValueError("The second object must be Song.")

        return self.name == other.name and self.length == other.length


class Album:
    def __init__(self, name, genre, author):
        self.name = name
        self.genre = genre
        self.author = author
        self.songs = []

    def __len__(self):
        return len(self.songs)

    def append(self, song):
        self.songs.append(song)

    def remove(self, song):
        return self.songs.remove(song)

    def get_info(self):
        return {
            "Name": self.name,
            "Genre": self.genre,
            "Author": self.author,
            "Songs": [obj.name for obj in self.songs]
        }

    def sort(self):
        songs_copy = deepcopy(self.songs)
        songs_copy.sort(key=lambda el: el.number_of_listens, reverse=True)
        return [{"Name": song.name, "Listens": song.number_of_listens}
                for song in songs_copy]


song1 = Song("Yellow Suubmarine", 3.20)
song2 = Song("Yesterday", 3.3)
song3 = Song("Help", 2.5)
song1.listen()
song2.listen()
song2.listen()
song2.listen()

print(song1.number_of_listens)
print(song2.number_of_listens)
print(song3.number_of_listens)

album = Album("Test", "Rock", "The Beatles")
album.append(song1)
album.append(song2)
album.append(song3)
print(album.get_info())
album.remove(song3)
print(album.get_info())
album.append(song3)
print(album.sort())
print(len(album))
