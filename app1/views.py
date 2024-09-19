from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import Ride
from .serializers import RideSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status

# Create your views here.
@api_view(['GET','POST','PUT'])
def index(request):
    if request.method=='GET':
        people_details = {
            "name": "Rider App",
        }
        return Response(people_details)
    elif request.method=='POST':
        print("This is a POST Method")
        return Response("This is a POST Method")
    elif request.method=='PUT':
        print("This is a PUT Method")
        return Response("This is a PUT Method")
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(rider=self.request.user)

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        ride = self.get_object()
        ride.status = request.data.get('status', ride.status)
        ride.save()
        return Response({'status': ride.status})
    
def match_ride_with_driver(ride):
    available_drivers = User.objects.filter(is_driver=True)
    return available_drivers.first()


# a. Create a User
# Method: POST
# URL: http://127.0.0.1:8000/users/
# Body: Select raw and JSON, then provide the user data. Example:
# json
# Copy code
# {
#   "username": "testuser",
#   "email": "testuser@example.com",
#   "password": "securepassword123"
# }

# b. List Users
# Method: GET
# URL: http://127.0.0.1:8000/users/

# c. Retrieve a User
# Method: GET
# URL: http://127.0.0.1:8000/users/{user_id}/

# d. Update a User
# Method: PUT
# URL: http://127.0.0.1:8000/users/{user_id}/
# Body: Provide the updated user data in raw and JSON. Example:
# json
# Copy code
# {
#   "username": "updateduser",
#   "email": "updateduser@example.com",
#   "password": "newsecurepassword123"
# }

# e. Delete a User
# Method: DELETE
# URL: http://127.0.0.1:8000/users/{user_id}/




# # Login 5. 
# Testing Again
# Try making the login request again with Postman to http://127.0.0.1:8000/api-token-auth/ with the POST method and the appropriate JSON payload:

# json
# Copy code
# {
#   "username": "testuser",
#   "password": "securepassword123"
# }

# b. Send Request
# Click on the "Send" button in Postman. If the credentials are correct, you should receive a JSON response containing the token:

# json
# Copy code
# {
#   "token": "your_generated_token_here"
# }



# Creating new ride
# a. Open Postman and select the request you want to send (for example, creating a ride).
# b. Go to the "Authorization" tab.
# c. Set the "Type" to "Bearer Token".
# d. In the "Token" field, paste your token (55c2bc7bad95c23515d0a0941e08abc94d240b52).
# Alternatively, you can manually add the token as a header:

# Go to the Headers tab in Postman.
# Add a new header with:
# Key: Authorization
# Value: Token 55c2bc7bad95c23515d0a0941e08abc94d240b52
# 3. Making Authenticated Requests
# You can now make requests to any API endpoints that require authentication, such as:

# Creating a new ride (POST /rides/)
# Updating a ride's status (PATCH /rides/{ride_id}/update_status/)

# Example:
# {
#   "rider":["This field is required."],
#   "pickup_location":["This field is required."],
#   "dropoff_location":["This field is required."]
# }