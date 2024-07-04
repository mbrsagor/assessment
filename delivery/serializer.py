from rest_framework import serializers

from academic.models.cgpa import CGPA
from academic.serializers.semester_serializer import SemesterSerializer


class CGPASerializer(serializers.ModelSerializer):
    semester_name = SemesterSerializer(required=False)

    class Meta:
        model = CGPA
        fields = (
            'id', 'student', 'student', 'semester_name', 'point', 'is_publish',
            'created_at', 'updated_at'
        )


class CreateVGPASerializer(serializers.ModelSerializer):
    class Meta:
        model = CGPA
        read_only_fields = ('student',)
        fields = (
            'id', 'student', 'semester', 'point', 'is_publish',
            'created_at', 'updated_at'
        )

    def validate_point(self, value):
        if value < 1 or value > 4:
            raise serializers.ValidationError('Pint has to be between 1 and 4.')
        return value

    def create(self, validated_data):
        if CGPA.objects.filter(**validated_data).exists():
            raise Exception('The semester and point is already exists.')
        return CGPA.objects.create(**validated_data)
