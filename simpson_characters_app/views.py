from rest_framework.views import APIView, Response #<-- Utilize to handle API behavior
from django.shortcuts import render
import requests # Pythons user friendly way to make requests to API's
from django.shortcuts import get_object_or_404
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1 # Authenticates a user with public and secret keys
from dotenv import load_dotenv # Allows us to interact with .env files
import os # os will make it possible to grab key value pairs from .env

load_dotenv()  # take environment variables from .env.

 
# Going to stray from the lecture and do it the way that Tiffany showed, using the built in serializer
class SimpsonChar(APIView):
    # What will trigger it?
    
    def get(self, request, character_id):
        character = None
        char_id_str = str(character_id)
        print(char_id_str)
        
        print(type(char_id_str))
        # make the endpoint variable so we know where we are going to get the information
        endpoint = f"https://thesimpsonsapi.com/api/characters/{char_id_str}"
        print(endpoint)

        # Need a response variable so that we can assign the response to something we can later parse out. 
        response = requests.get(endpoint)

        # convert to json
        responseJSON = response.json()

        # display results>name>random phrase from phrases
        return Response(responseJSON)
    