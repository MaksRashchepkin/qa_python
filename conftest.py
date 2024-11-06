import pytest
from main import BooksCollector


@pytest.fixture
def books_collection():
    books_collection = BooksCollector()
    return books_collection


@pytest.fixture
def collector(books_collection):
    my_collection = books_collection
    my_collection.add_new_book('Дюна')
    my_collection.set_book_genre('Дюна', 'Фантастика')
    return my_collection
