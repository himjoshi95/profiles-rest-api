from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """TEST API View"""

    def get(self, request,  format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django Views',
            'Gives you the most control over you application logic',
            'Is mapped maunally to URLs',
        ]
        return Response({'message': 'Hello!','an_apiview':an_apiview})
