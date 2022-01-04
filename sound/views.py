from django.shortcuts import render
from rest_framework.response import Response
from .models import Sound
from rest_framework.views import APIView
from .serializers import SoundSerializer

class SoundListAPI(APIView):
    def get(self, request):
        queryset = Sound.objects.all()
        print(queryset)
        serializer = SoundSerializer(queryset, many=True)
        return Response(serializer.data)
