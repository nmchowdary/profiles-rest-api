from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ TEST API VIEW """

    def get(self, request, format=None):
        """Retrns a list of ApI view features"""
        an_apiview = [
        'use HTTP methods as functions (get, post, patch, put, delete)',
        'is similar to a traditional Django view',
        'gives you the most control over you application logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
