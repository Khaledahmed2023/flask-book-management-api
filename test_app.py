# Import necessary modules for testing
import pytest
from app import *

# Define a fixture to create a test client
@pytest.fixture
def client():
    # Create a test client using the app's test client
    with app.test_client() as client:
        yield client

# Test: Retrieve all books
def test_get_books(client):
    # Send a GET request to the '/books' endpoint
    response = client.get("/books")
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check if the response contains a list of books
    assert isinstance(response.json, list)

# Test: Retrieve all reviews
def test_get_all_reviews(client):
    # Send a GET request to the '/reviews' endpoint
    response = client.get("/reviews")
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check if the response contains a key 'reviews'
    assert "reviews" in response.json

# Test: Retrieve reviews for a specific book
def test_get_reviews_for_book(client):
    # Specify a book ID
    book_id = 1
    
    # Send a GET request to the '/reviews/{book_id}' endpoint
    response = client.get(f"/reviews/{book_id}")
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check if the response contains keys 'book_id' and 'reviews'
    assert "book_id" in response.json
    assert "reviews" in response.json

# Test: Retrieve the top books
def test_get_top_books(client):
    # Send a GET request to the '/books/top' endpoint
    response = client.get("/books/top")
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check if the response contains a key 'top_books'
    assert "top_books" in response.json

# Test: Retrieve information about an author
def test_get_author_route(client):
    # Specify an author's name
    author_name = "John_Doe"
    
    # Send a GET request to the '/author/{author_name}' endpoint
    response = client.get(f"/author/{author_name}")
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check if the response contains keys 'author' and 'summary'
    assert "author" in response.json
    assert "summary" in response.json
