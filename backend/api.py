from django.http import StreamingHttpResponse, HttpResponseRedirect, HttpResponse
from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework import generics
from rest_framework.views import APIView, Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
import json

from backend.models import List
from backend.serializers import ListSerializer
# perm = permissions.IsAuthenticated
perm = permissions.AllowAny


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    permission_classes = [
        perm
    ]
    serializer_class = ListSerializer
