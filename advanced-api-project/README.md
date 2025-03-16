# API Endpoints

The `advanced_api_project` provides the following endpoints for managing books:

- **GET /books/**: Retrieve a list of all books.
- **GET /books/<id>/**: Retrieve a single book by ID.
- **POST /books/create/**: Create a new book (Authenticated users only).
- **PUT /books/update/<id>/**: Update an existing book (Authenticated users only).
- **DELETE /books/delete/<id>/**: Delete a book (Authenticated users only).

## Permissions
- Unauthenticated users can only view books (List and Detail views).
- Authenticated users can create, update, and delete books.
