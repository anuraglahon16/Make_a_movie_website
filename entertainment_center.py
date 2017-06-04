"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media

def main():
    """Creates three Movie objects."""
    sachin = media.Movie("Sachin:A Billion Dreams",
                          "Greatest batsman of cricket",
                          "https://upload.wikimedia.org/wikipedia/en/8/86/Sachin_A_Billion_Dreams_Poster.jpg",
                          "https://www.youtube.com/watch?v=8gTeE6pa4Kg",
                          "26 May 2017")

    ms_dhoni_the_untold_story = media.Movie("M.S. Dhoni: The Untold Story",
                          "Ranchi lad M S Dhoni aspires to play cricket for India and became the most successful captain",
                          "https://upload.wikimedia.org/wikipedia/en/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg",
                          "https://www.youtube.com/watch?v=atVof3pjT-I",
                          "May 2016")

    Half_girlfriend = media.Movie("Half Girlfriend",
                           "Riya suggests a compromise to Madhav when she agrees to be his half girlfriend",
                           "https://upload.wikimedia.org/wikipedia/en/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg",
                           "https://www.youtube.com/watch?v=KmlBnmyelHI",
                           "19 May 2017")



    movies = [sachin, ms_dhoni_the_untold_story, Half_girlfriend]


    # Open the movie website in the user's browser
    fresh_tomatoes.open_movies_page(movies)
if __name__ == '__main__':
    main()
