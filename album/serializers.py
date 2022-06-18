from rest_framework import serializers

from album.models import Student


class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"
