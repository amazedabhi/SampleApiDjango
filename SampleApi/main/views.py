from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from . import serializers
import json


class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

# Create your views here.
@api_view()
def usersApi(request):
    student1= Student('Abhinav',1,100)
    student2= Student('Deepak',2,90)
    student3= Student('Nishant',3,75)
    serializer = serializers.StudentSerializer([
        student1,
        student2,
        student3
        ],many=True)
    return Response(serializer.data)
