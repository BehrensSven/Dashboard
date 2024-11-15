from rest_framework import serializers
from django.contrib.auth.models import User
from .models import News, Module, StudentModule

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
    completion_date = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ['id', 'name', 'description', 'is_active', 'grade', 'completion_date']

    def get_is_active(self, obj):
        user = self.context['request'].user
        try:
            student_module = StudentModule.objects.get(user=user, module=obj)
            return student_module.is_active
        except StudentModule.DoesNotExist:
            return False

    def get_grade(self, obj):
        user = self.context['request'].user
        try:
            student_module = StudentModule.objects.get(user=user, module=obj)
            return student_module.grade
        except StudentModule.DoesNotExist:
            return None

    def get_completion_date(self, obj):
        user = self.context['request'].user
        try:
            student_module = StudentModule.objects.get(user=user, module=obj)
            return student_module.completion_date
        except StudentModule.DoesNotExist:
            return None
        

class CompletedModuleSerializer(serializers.ModelSerializer):
    module_name = serializers.CharField(source='module.name')
    module_description = serializers.CharField(source='module.description')

    class Meta:
        model = StudentModule
        fields = ['module_name', 'module_description', 'grade', 'completion_date']