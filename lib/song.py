class Song:
    # Class attribute to keep track of the number of songs
    count = 0
    # Class attribute to store unique genres
    genres = []
    # Class attribute to store unique artists
    artists = []
    # Class attribute to store genre count
    genre_count = {}
    # Class attribute to store artist count
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        # Increment count when a new song is created
        Song.add_song_to_count()
        # Add genre and artist to respective lists
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count = {genre: sum(1 for song in cls.all_songs() if song.genre == genre) for genre in cls.genres}

    @classmethod
    def add_to_artist_count(cls):
        cls.artist_count = {artist: sum(1 for song in cls.all_songs() if song.artist == artist) for artist in cls.artists}

    @staticmethod
    def all_songs():
        return [song for song in Song.__dict__.values() if isinstance(song, Song)]
