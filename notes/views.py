from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer

class NoteListAPIView(APIView):
    """
    API endpoint for listing and creating notes.

    - GET: Retrieve a list of all notes.
    - POST: Create a new note.

    GET:
    - URL: /api/notes/
    - Response:
      - Status Code: 200 OK
      - Body: A JSON array containing serialized data of all notes.

    POST:
    - URL: /api/notes/
    - Request:
      - Body: JSON data containing the title and content of the new note.
    - Response:
      - Status Code: 201 Created
      - Body: JSON data containing the details of the newly created note.
      - Error Response:
        - Status Code: 400 Bad Request
        - Body: JSON data containing error details if the input is invalid.
    """
    def get(self, request, *args, **kwargs):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDetailAPIView(APIView):
    """
    API endpoint for retrieving, updating, and deleting a single note.

    - GET: Retrieve details of a single note by its ID.
    - PUT: Update a single note by its ID.
    - DELETE: Delete a single note by its ID.

    GET:
    - URL: /api/notes/<note_id>/
    - Parameters:
      - note_id (int): The ID of the note to retrieve.
    - Response:
      - Status Code: 200 OK
      - Body: JSON data containing the details of the requested note.
      - Error Response:
        - Status Code: 404 Not Found if the note with the specified ID does not exist.

    PUT:
    - URL: /api/notes/<note_id>/
    - Parameters:
      - note_id (int): The ID of the note to update.
    - Request:
      - Body: JSON data containing the updated title and content.
    - Response:
      - Status Code: 200 OK
      - Body: JSON data containing the details of the updated note.
      - Error Response:
        - Status Code: 404 Not Found if the note with the specified ID does not exist.
        - Status Code: 400 Bad Request if the input is invalid.

    DELETE:
    - URL: /api/notes/<note_id>/
    - Parameters:
      - note_id (int): The ID of the note to delete.
    - Response:
      - Status Code: 204 No Content on successful deletion.
      - Error Response:
        - Status Code: 404 Not Found if the note with the specified ID does not exist.
    """
    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        note = self.get_object(pk)
        if note:
            serializer = NoteSerializer(note)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, *args, **kwargs):
        note = self.get_object(pk)
        if note:
            serializer = NoteSerializer(note, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        note = self.get_object(pk)
        if note:
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
