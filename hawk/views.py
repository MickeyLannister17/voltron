from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.response import Response
from .models import Student

from .serializers import StudentSerializer


# making a Post request
class StudentViews(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# @api_view(['POST'])
# def create_student(request):
# student = Student.objects.all()
# serializer = StudentSerializer(data=request.data)

# if serializer.is_valid():
#     serializer.save()
#  return Response(serializer.data)


class GetStudentViews(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UpdateStudentView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DeleteStudentView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

