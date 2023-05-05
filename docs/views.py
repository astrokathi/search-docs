from rest_framework import viewsets, views
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.http import HttpResponse
# Create your views here.


class UserViewSets(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class Kathi(views.APIView):

    @classmethod
    def get_extra_actions(cls):
        return []

    @api_view(['GET'])
    def return_something(request):
        return HttpResponse('{"Kathi": "I am back"}', status=200, content_type="application/json", charset="utf-8")