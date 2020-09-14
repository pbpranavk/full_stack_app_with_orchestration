from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Story
from .serializers import StorySerializer

# Create your views here.
from rest_framework import generics


class StoryList(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


# class StoryApi(APIView):
#     def get(self, request, format=None):
#         stories = Story.objects.all()
#         return Response(stories)

#     def post(self, request, format=None):
#         serializer = StorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = StorySerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)