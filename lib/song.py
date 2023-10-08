class Song:
    
    count = 0
    genres = []
    artists = []
    names = []
    genre_count = {}
    artist_count = {}


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_artists(artist)
        self.add_to_genres(genre)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)


    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count+=increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre in cls.genres:
            return
        else:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist in cls.artists:
            return
        else:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count.keys():
            new_val = cls.genre_count[genre] + 1
            cls.genre_count[genre] = new_val
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count.keys():
            new_val = cls.artist_count[artist] + 1
            cls.artist_count[artist] = new_val
        else:
            cls.artist_count[artist] = 1