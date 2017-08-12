import fresh_tomatoes
class Movie():
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title=title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url



inception = Movie("Inception",
                        ("http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5Ban"
                         "BnXkFtZTcwNTI5OTM0Mw@@._V1_SX214_AL_.jpg"),
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")


star_wars = Movie("Star Wars",
                        ("http://ia.media-imdb.com/images/M/MV5BMTU4NTczODkwM15BMl5Ban"
                         "BnXkFtZTcwMzEyMTIyMw@@._V1_SX214_AL_.jpg"),
                        "https://www.youtube.com/watch?v=9gvqpFbRKtQ")


italian_job = Movie("The Italian Job",
                          ("http://ia.media-imdb.com/images/M/MV5BNTI1ODYwNzg3Nl5BMl5B"
                           "anBnXkFtZTcwMDYzMjk3OA@@._V1_SX214_AL_.jpg"),
                          "https://www.youtube.com/watch?v=FEltJsIwSvE")



movie_list = [ inception, star_wars,
               italian_job]


def main():

    fresh_tomatoes.open_movies_page(movie_list)

if __name__ == "__main__":
    main()
