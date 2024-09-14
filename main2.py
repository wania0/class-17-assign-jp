from flask import Flask, request
app = Flask(__name__)

books = [
    {"id" : 1, "name" : "Atomic Habits"},
    {"id" : 2, "name" : "Power Of Subconcious Mind"},
    {"id" : 3, "name" : "You Are Stronger Than You Know"},
    {"id" : 4, "name" : "The Secret Of Thinking"},
    {"id" : 5, "name" : "The Joyful Mind"}
]

@app.route("/")
def text():
   return  "assignment class 17"

# Add a new book to the collection.
@app.route("/books", methods = ['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return "Book added successfully"

# Retrieve all books from the collection.
@app.route("/books", methods = ['GET'])
def get_all_books():
    return books

# Get a single book by its ID.
@app.route("/books/<int:id>", methods=['GET'])
def get_book(id):
    for book in books:
        if book['id'] == id:
            return book
    return "book not found"

# Update a book by its ID.
@app.route("/books/<int:id>", methods=['PUT'])
def update_book(id):
    for book in books:
        if book['id'] == id:
            data = request.get_json() 
            book['name'] = data['name'] 
            return "Book name updated successfully"
    return "Book not found"

# Delete a book by its ID.
@app.route("/books/<int:id>", methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return "Book deleted Successfully"
    return "Book not found"

app.run(
    debug=True,
    port=3000
)