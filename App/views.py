from django.shortcuts import render
from .models import * 
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .filters import studentFilter


@api_view(["GET"])
def getAllStudent(request):
    filterset=studentFilter(request.GET,queryset=Student.objects.all().order_by("id"))
    serializers=studentSerializer(filterset.qs,many=True)
    return Response(serializers.data)   
@api_view(["GET"])
def getById(request,id):
    student=get_object_or_404(Student,pk=id)
    serializers=studentSerializer(student,many=False)
    return Response(serializers.data) 
@api_view(["POST"])
def addStudent(request):
    student=Student()
    student.name=request.data.get("name")
    student.age=int(request.data.get("age"))
    student.address=request.data.get("address")
    student.save()
    serializers=studentSerializer(student,many=False)
    return Response(serializers.data)
@api_view(["DELETE"])
def deleteStudent(request,id):
    student=get_object_or_404(Student,pk=id)
    student.delete()
    return Response({"message":"record of the student dekete successfully"})
@api_view(["PUT"])
def updateStudent(request,id):
    student=get_object_or_404(Student,pk=id)
    student.name=request.data["name"]
    student.age=int(request.data["age"])
    student.address=request.data["address"]
    #student.save()
    serializers=studentSerializer(student,many=False)
    return Response ({"message":"update successfully"})
