import sqlite3
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from libraryapp.models import Book
from libraryapp.models import model_factory
from ..connection import Connection

@login_required
def book_list(request):
    # Always have to specify request method for a view
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            #this .row special class puts column headers in place of row indexes...much easier to write code
            conn.row_factory = model_factory(Book)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.ISBN,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)


            all_books = db_cursor.fetchall()
# import book model, create an instance of book and set the book properties to the colums that come back in the dataset.
            # for row in dataset:
            #     book = Book()
            #     book.id = row['id']
            #     book.title = row['title']
            #     book.isbn = row['isbn']
            #     book.author = row['author']
            #     book.year_published = row['year_published']
            #     book.librarian_id = row['librarian_id']
            #     book.location_id = row['location_id']
            #     #append all instances of books to list
            #     all_books.append(book)
        #convert to HTML
        #
        template = 'books/list.html'
        context = {
            'all_books': all_books
        }
        #In DJANGO you have to manually wire up URLs
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO libraryapp_book
        (
            title, author, ISBN,
            year_published, location_id, librarian_id
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (form_data['title'], form_data['author'],
            form_data['ISBN'], form_data['year_published'],
           form_data["location"], request.user.librarian.id))

    return redirect(reverse('libraryapp:books'))