import pytest
from main import BooksCollector

@pytest.mark.usefixtures('collector')
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector.get_books_genre() == {'Дюна': 'Фантастика', 'Гордость и предубеждение и зомби': '',
                                               'Что делать, если ваш кот хочет вас убить': ''}



    def test_add_new_book_already_added_book(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')
        assert len(collector.books_genre) == 2


    @pytest.mark.parametrize('name', ['',
                                      'Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции'])
    def test_add_new_book_name_out_of_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert len(books_collection.get_books_genre()) == 1



    @pytest.mark.parametrize('name', ['К югу от границы',
                                      'Любовь как роза, красива, но шипы больны',
                                      'Я'])
    def test_add_new_book_name_in_the_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert name in books_collection.get_books_genre()



    def test_set_book_genre_to_existing_book(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение': 'Фантастика'}



    def test_set_book_genre_to_not_existing_book(self, collector):
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_books_genre() == {}



    def test_set_book_genre_to_not_existing_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Трагикомедии')
        assert collector.get_books_genre() == {'Гордость и предубеждение': ''}



    def test_get_book_genre_by_name(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'



    @pytest.mark.parametrize('name, genre', [('Гордость и предубеждение и зомби', 'Ужасы'),
                                             ('Что делать, если ваш кот хочет вас убить', 'Комедии')])
    def test_get_books_with_specific_genre_by_genre(self, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]



    def test_get_books_for_children(self, collector):
        collector.add_new_book('Дюна1')
        collector.set_book_genre('Дюна1', 'Ужасы')
        assert len(collector.books_genre) == 2
        assert len(collector.get_books_for_children()) == 1 
        assert collector.get_books_for_children() == ['Дюна']



    def test_add_book_in_favorites_not_added_in_favorites_book(self, collector):
        collector.add_book_in_favorites('Дюна')
        assert 'Дюна' in collector.get_list_of_favorites_books() and len(collector.get_list_of_favorites_books()) == 1



    def test_add_book_in_favorites_added_in_favorites_book(self, collector):
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert 'Дюна' in collector.get_list_of_favorites_books() and len(collector.get_list_of_favorites_books()) == 1



    def test_add_book_in_favorites_not_added_dict_book(self, collector):
        book = 'Идиот'
        collector.add_book_in_favorites(book)
        assert len(collector.get_list_of_favorites_books()) == 0



    def test_delete_book_from_favorites(self, collector):
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert len(collector.get_list_of_favorites_books()) == 0



    def test_delete_book_from_favorites_deleted_book(self, collector):
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Вверх')
        assert len(collector.get_list_of_favorites_books()) == 1 and 'Вверх' not in collector.get_list_of_favorites_books()



    def test_get_list_of_favorites_books(self, collector):
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Вверх')
        assert collector.get_list_of_favorites_books() == ['Дюна', 'Вверх']
