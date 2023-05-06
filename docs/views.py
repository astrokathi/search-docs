from django.core.files.temp import NamedTemporaryFile
from django.core.files.uploadedfile import TemporaryUploadedFile
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, FileUploadSerializer, QuerySerializer
from rest_framework.response import Response
from rest_framework.decorators import action
import os
from docs.chatbot import Chatbot


# Create your views here.
class UserViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        # ...

        # Return a response
        return Response({'message': 'Custom action response'})


class Kathi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        data = {
            "message": "This is a stub response",
            "status": "success",
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        data = {
            "message": "This is a stub response",
            "status": "success",
        }
        return Response(data)


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    serializer_class = FileUploadSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        file_obj = request.data['file']
        if isinstance(file_obj, TemporaryUploadedFile):
            # File has already been saved to a temporary file on disk.
            # Move it to a permanent location.
            temp_file_path = file_obj.temporary_file_path()
            print(file_obj.name)
            permanent_file_path = os.path.join(os.getcwd(), 'data', 'tmp.' + file_obj.name.split('.')[-1])
            os.rename(temp_file_path, permanent_file_path)
        else:
            # File is still in memory. Create a temporary file object and save it to disk.
            with NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(file_obj.read())
                print(file_obj.name.split('.')[-1], "from permanent  store")
                permanent_file_path = os.path.join(os.getcwd(), 'data', 'tmp.' + file_obj.name.split('.')[-1])

                os.rename(temp_file.name, permanent_file_path)

        return Response({'message': 'File uploaded'})


class QueryView(APIView):
    serializer_class = QuerySerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        query = request.data['query']
        bot = Chatbot("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", path=os.path.join(os.getcwd(), 'data'))
        response = bot.generate_response(query)

        return Response({'response': response})
