from rest_framework import generics
from user_auth.models import User
from user_auth.serializers import ProfileSerializer



class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    name = 'user-detail'
