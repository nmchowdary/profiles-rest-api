from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """ TEST API VIEW """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Retrns a list of ApI view features"""
        an_apiview = [
        'use HTTP methods as functions (get, post, patch, put, delete)',
        'is similar to a traditional Django view',
        'gives you the most control over you application logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'methos': 'PUT'})

    def patch(self, request, pk=None):
        """ Handle a partial update of an object"""
        return Response({'mesthod': "PATCH"})

    def delete(self, request, pk=None):
        """delete an object """
        return Response({'method': 'DELETE'})
