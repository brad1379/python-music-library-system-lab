class Song:
    count = 0
    genres = []
    artists = []
    genre_count = 0
    artists_count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls):
        pass

    @classmethod
    def add_to_genres(cls):
        pass

    @classmethod
    def add_to_artists(cls):
        pass

    @classmethod
    def add_to_genre_count(cls):
        pass

    @classmethod
    def add_to_artists_count(cls):
        pass
