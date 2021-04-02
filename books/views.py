from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import BookDetails

# Create your views here.

class BooksVeiw(APIView):
    def get(self, request):
        books = list(BookDetails.objects.all().values())
        return Response({"Books":books})


    def post(self,request):
        c = request.data
        d = BookDetails(title = c.get("title"), author = c.get("author"), area_related = c.get("area_related"))
        d.save()
        return Response({"message": "This method is post"})



