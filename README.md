# Notes API

This is a simple RESTful API for managing notes using Python with the Django framework.

## Setup

### 1. Create and Activate Virtual Environment

Before installing the dependencies, it's recommended to create and activate a virtual environment to isolate the project's dependencies. Open a terminal and run the following commands:

```bash
# Create a virtual environment (use 'venv' or 'virtualenv' depending on your Python version)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

### 2. Install Dependencies

Ensure you have Python and pip installed on your system. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations

Run the following commands to apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Optional)

You can create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

## Run the API Locally

Start the development server:

```bash
python manage.py runserver
```

The API will be accessible at [http://localhost:8000/api/notes/](http://localhost:8000/api/notes/).

## API Endpoints

- Create a new note: `POST http://localhost:8000/api/notes/`
- Retrieve all notes: `GET http://localhost:8000/api/notes/`
- Retrieve a single note by ID: `GET http://localhost:8000/api/notes/<note_id>/`
- Update a note: `PUT http://localhost:8000/api/notes/<note_id>/`
- Delete a note: `DELETE http://localhost:8000/api/notes/<note_id>/`

## Examples

### Create a New Note

#### Using `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title": "Example Note", "content": "This is a sample note."}' http://localhost:8000/api/notes/
```

#### Using `httpie`:

```bash
http POST http://localhost:8000/api/notes/ title="Example Note" content="This is a sample note."
```

### Retrieve All Notes

#### Using `curl`:

```bash
curl http://localhost:8000/api/notes/
```

#### Using `httpie`:

```bash
http GET http://localhost:8000/api/notes/
```

### Retrieve a Single Note by ID

Replace `<note_id>` with the actual ID of the note.

#### Using `curl`:

```bash
curl http://localhost:8000/api/notes/<note_id>/
```

#### Using `httpie`:

```bash
http GET http://localhost:8000/api/notes/<note_id>/
```

### Update a Note

Replace `<note_id>` with the actual ID of the note.

#### Using `curl`:

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Note", "content": "This note has been updated."}' http://localhost:8000/api/notes/<note_id>/
```

#### Using `httpie`:

```bash
http PUT http://localhost:8000/api/notes/<note_id>/ title="Updated Note" content="This note has been updated."
```

### Delete a Note

Replace `<note_id>` with the actual ID of the note.

#### Using `curl`:

```bash
curl -X DELETE http://localhost:8000/api/notes/<note_id>/
```

#### Using `httpie`:

```bash
http DELETE http://localhost:8000/api/notes/<note_id>/
```

These examples demonstrate how to perform basic CRUD operations on your Notes API. Adjust the data and URLs based on your actual API structure and requirements. Additionally, you can use tools like Postman for a more user-friendly interface to interact with your API.

## Django Admin

To access the Django admin interface (if a superuser is created), go to [http://localhost:8000/admin/](http://localhost:8000/admin/) and log in using the superuser credentials.
