from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import CustomUser
from .serializers import UserSerializer

class UserListView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

def count_visits(request):
    # Get the current visit count from the session, or set it to 0 if it doesn't exist
    visit_count = request.session.get('visit_count', 0)
    # Increment the visit count
    visit_count += 1
    # Update the session with the new count
    request.session['visit_count'] = visit_count
    # Return the visit count as JSON
    return JsonResponse({'visit_count': visit_count})
