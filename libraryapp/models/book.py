from django.db import models
from .library import Library
from .librarian import Librarian

class Book(models.Model):

    title= models.CharField(max_length=50)
    ISBN = models.CharField(max_length=25)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField()
    #This is how you youse a foreign key from an ID of another table
    # on_delete=models.CASCADE means if the library is deleted, all the books are as well
    location = models.ForeignKey(Library, on_delete=models.CASCADE)
    # Now we have a one to many relationship between librarian and a book
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)

