import datetime

import pytest

from yamod import models
from yamod import exercise

@pytest.fixture
@pytest.mark.django_db
def setup():
    genres = ["Action","Horror","Scifi"]
    movies = [
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
                                runtime=runtime) for movie_title,released,runtime in movies]

@pytest.mark.django_db
class TestBase:
        
        def test_create_genre(self, setup):
            genre = exercise.create_genre()
            assert genre.name == "Comedy"

        def test_delete_genre(self, setup):
            exercise.delete_genre()
            assert models.Genre.objects.count() == 2

        def test_filter_movie_by_year(self, setup):
            movies_2000 = exercise.filter_movie_by_year()  
            assert movies_2000.count() == 3
                
        def test_filter_movie_by_runtime(self, setup):
            movies_90 = exercise.filter_movie_by_runtime()
            assert movies_90.count() == 3

        def test_filter_movie_starting_with_b(self, setup):
            movies_with_b = exercise.filter_movie_starting_with_b()
            assert movies_with_b.count() == 2

        def test_filter_movie_containing_blade(self, setup):
            movies_containing_blade = exercise.filter_movie_containing_blade()
            assert movies_containing_blade.count() == 2

        def test_genre_to_str(self, setup):        
            for movie_title,released,runtime in movies:
                assert str(models.Movie.objects.get(movie_title=movie_title)) == movie_title 
                
        def test_update_role_type(self, setup):
            exercise.update_role_type()
            assert models.RoleType.objects.filter(name="Actor/Actress").count() == 1

        def test_get_or_create_role_type(self, setup):
            exercise.get_or_create_role_type()
            assert models.RoleType.objects.count() == 3
            assert models.RoleType.objects.filter(name="Producer").count() == 1
