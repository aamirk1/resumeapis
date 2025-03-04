from rest_framework.response import Response
from api.models import Profile
from api.serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class ProfileView(APIView):
    def post(self,request,format= None):
        serializer = ProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Resume Uploaded Successfully','status':'success', 'candidate':serializer.data},status = status.HTTP_201_CREATED
            )
        return Response(serializer.errors)

    def get(self,request, format = None):
        candidate = Profile.objects.all()
        serializer = ProfileSerializer(candidate,many = True)
        return Response({'status':'success','candidate':serializer.data},status = status.HTTP_200_OK)