from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """TEST API View"""

    """This configures our APIView to have the serailizer class
    we created in the previous video"""
    serializer_class = serializers.HelloSerializer

    def get(self, request,  format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django Views',
            'Gives you the most control over you application logic',
            'Is mapped maunally to URLs',
        ]
        return Response({'message': 'Hello!','an_apiview':an_apiview})
    
    def post(self,request):
        """Create a hello message with our name"""

        """The self.serializer_class() function is a function that comes with APIView
         that retrives the configured serializer_class for our view  """
        
        """This is the standard way to retrive the serailizer class"""
        serializer = self.serializer_class(data=request.data)
        """Second part assigns the data, so when you make a post request
        to our APIView, the data gets passed in as request.data"""
        """We assign this data to our serializer class and then we create a new variable(serializer in this case)"""

        """The django_restframework serializers provide the functionality to validate the input as per our specs serializer field(in our case name not longer than 10 characters)"""
        if serializer.is_valid():
            """If the serializer is valid, then we want to retrieve the name field from the validated data"""
            name =  serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self, request ,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


    
