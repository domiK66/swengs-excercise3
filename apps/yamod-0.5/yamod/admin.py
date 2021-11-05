from django.contrib import admin
from yamod import models

class MovieAdmin(admin.ModelAdmin):
    '''
    Update this class. The change list 
    should display movie_title, released data and run time. 
    Moreover, the change list should be searchable by movie and 
    original title.
    '''
    pass
    

class GenreAdmin(admin.ModelAdmin): 
    '''
    Update this class. The change list should be searchable by genre name, 
    the list itself should show the name of the genre
    '''
    pass

class PersonAdmin(admin.ModelAdmin):
    '''
    Update this class. The change list, shoule show credited_name,
    year_of_birth, year_of_death and gender. 
    Add a filter in the change list to add gender
    '''
    pass

# Now register the your admin classes with Django - otherwise 
# you want see them in your admin application:
admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Person, PersonAdmin)



