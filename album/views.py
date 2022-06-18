from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from django.http import HttpResponse

from album.serializers import StudentsSerializer

from album.models import Student


class GetStudent(APIView):

    def post(self, request):
        print(request.data)
        student_name = request.data.get('name')
        issue_year = request.data.get('issue_year')
        group = request.data.get('group')
        all_students = Student.objects.filter(issue_year=issue_year, group=group)
        student = Student.objects.filter(name=student_name, issue_year=issue_year, group=group)[0]

        print(len(all_students))
        if len(all_students) != 0:
            print(all_students[0])
            return Response({"success": "http://127.0.0.1:8000/images/" + str(student.image)})



        return Response("NOT_FOUND", status=status.HTTP_400_BAD_REQUEST)


class GetAllStudents(generics.ListAPIView):
    serializer_class = StudentsSerializer

    def get_queryset(self):
        return Student.objects.all()


class CreateStudent(APIView):

    def post(self, request):
        print(request.data)
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
