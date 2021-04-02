from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import JournalDetails

# Create your views here.

class JournalList(APIView):
    def get(self,request):
        data = list(JournalDetails.objects.all().values())
        return Response({"Journals":data})

    def post(self,request):
        x = request.data
        y = JournalDetails(name = x.get("name"), publisher = x.get("publisher"), year_of_publish = x.get("year_of_publish"))
        y.save()
        return Response({"message":"this method is post"})