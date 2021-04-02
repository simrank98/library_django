from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentsDetails



# Create your views here.
class StudentsList(APIView):
    def get(self,request):
        data = list(StudentsDetails.objects.all().values())
        print(data)
        return Response({"Students":data})

    def post(self,request):
        x = request.data
        y = StudentsDetails(name = x.get("name"), roll = x.get("roll"), department = x.get("dept"))
        y.save()
        return Response({"message":"THis method is post"})
        
