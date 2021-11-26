import datetime

from django.test import TestCase

from . import models
from . import exercise

class YamodBaseTest(TestCase):

    def setUp(self):
        self.genres=["Action","Horror","Scifi"]
        self.movies = [
            ("Blade Runner", datetime.date(year=1982,month=6,day=25),100),
            ("Blade Runner 2049", datetime.date(year=2017,month=10,day=6),150),
            ("Nomadland", datetime.date(year=2020,month=9,day=11),110),
            ("The French Dispatch", datetime.date(year=2021,month=7,day=12),100),
            ("Rushmoore", datetime.date(year=1998,month=9,day=17),95)
        ]
        # Setup database
        [models.Genre.objects.create(name=name) for name in ["Action","Horror","Scifi"]]
        [models.RoleType.objects.create(name=name) for name in ["Actor","Producer","Director"]]
        [models.Movie.objects.create(movie_title=movie_title,
                                     released=released,
                                     original_title=movie_title,
                                     runtime=runtime) for movie_title,released,runtime in self.movies]

class YamodModelTest(YamodBaseTest):

    def test_create_genre(self):
        genre = exercise.create_genre()
        self.assertEqual(genre.name,"Comedy")

    def test_delete_genre(self):
        exercise.delete_genre()
        self.assertEqual(models.Genre.objects.count(),2)

    def test_filter_movie_by_year(self):
        movies_2000 = exercise.filter_movie_by_year()  
        self.assertEqual(movies_2000.count(),3)

    def test_filter_movie_by_runtime(self):
        movies_90 = exercise.filter_movie_by_runtime()
        self.assertEqual(movies_90.count(),3)

    def test_filter_movie_starting_with_b(self):
        movies_with_b = exercise.filter_movie_starting_with_b()
        self.assertEqual(movies_with_b.count(),2)

    def test_filter_movie_containing_blade(self):
        movies_containing_blade = exercise.filter_movie_containing_blade()
        self.assertEqual(movies_containing_blade.count(),2)

    def test_genre_to_str(self):        
        # Implement the __str__ method of model class Genre and Movie
        # Genre should return the name and Movie should return the movie_title
        # (Implementation is done in models.py)
        for movie_title,released,runtime in self.movies:
            self.assertEqual(str(models.Movie.objects.get(movie_title=movie_title)),movie_title)

    def test_update_role_type(self):
        exercise.update_role_type()
        self.assertEqual(models.RoleType.objects.filter(name="Actor/Actress").count(),1)

    def test_get_or_create_role_type(self):
        exercise.get_or_create_role_type()
        self.assertEqual(models.RoleType.objects.count(),3)
        self.assertEqual(models.RoleType.objects.filter(name="Producer").count(),1)
