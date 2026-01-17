from rest_framework import serializers
from .models import Student
from class_app.serializers import ClassSerializer

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = (
#             "name",
#             "student_email",
#             "personal_email",
#             "locker_number",
#             "locker_combination",
#             "good_student", 
#             "classes"
#         )