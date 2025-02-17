from rest_framework import serializers
from django.contrib.auth.models import User
from .enum import AppointmentCategory
from .models import News, Module, StudentModule, UserStudyProgram, Appointment
from datetime import date

# --- Serializer Definitions ---

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create user with password hashing
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
    
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
        # Retrieve active status from StudentModule
        user = self.context['request'].user
        try:
            return StudentModule.objects.get(user=user, module=obj).is_active
        except StudentModule.DoesNotExist:
            return False

    def get_grade(self, obj):
        # Retrieve grade from StudentModule
        user = self.context['request'].user
        try:
            return StudentModule.objects.get(user=user, module=obj).grade
        except StudentModule.DoesNotExist:
            return None

    def get_completion_date(self, obj):
        # Retrieve completion date from StudentModule
        user = self.context['request'].user
        try:
            return StudentModule.objects.get(user=user, module=obj).completion_date
        except StudentModule.DoesNotExist:
            return None
        

class CompletedModuleSerializer(serializers.ModelSerializer):
    module_name = serializers.CharField(source='module.name')
    module_description = serializers.CharField(source='module.description')

    class Meta:
        model = StudentModule
        fields = ['module_name', 'module_description', 'grade', 'completion_date']
        
class StudentProgressSerializer(serializers.Serializer):
    total_modules = serializers.IntegerField()
    modules_passed = serializers.IntegerField()
    time_studied_days = serializers.IntegerField()
    standard_duration_days = serializers.IntegerField()

    def to_representation(self, user):
        try:
            user_study_program = UserStudyProgram.objects.get(user=user)
        except UserStudyProgram.DoesNotExist:
            return {'error': 'Der Benutzer ist in keinem Studiengang eingeschrieben.'}

        study_program = user_study_program.study_program

        total_modules = Module.objects.filter(study_programs=study_program).count()
        modules_passed = StudentModule.objects.filter(user=user, is_active=False, grade__isnull=False).count()
        time_studied_days = (date.today() - user_study_program.enrollment_date).days
        standard_duration_days = user_study_program.time_model * 365

        return {
            'total_modules': total_modules,
            'modules_passed': modules_passed,
            'time_studied_days': time_studied_days,
            'standard_duration_days': standard_duration_days,
        }

class AppointmentSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=AppointmentCategory.choices, default=AppointmentCategory.PERSONAL)

    class Meta:
        model = Appointment
        fields = ['id', 'title', 'description', 'scheduled_at', 'users', 'category']
        read_only_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request', None)
        # Make 'users' read-only for non-staff users
        if request and not request.user.is_staff:
            self.fields['users'].read_only = True

    def create(self, validated_data):
        # Create appointment and add current user if not staff
        appointment = super().create(validated_data)
        request = self.context.get('request', None)
        if request and not request.user.is_staff:
            appointment.users.add(request.user)
        elif 'users' in self.initial_data:
            appointment.users.set(self.initial_data.get('users'))
        return appointment

    def update(self, instance, validated_data):
        # Only update the category explicitly; others handled by super()
        instance.category = validated_data.get('category', instance.category)
        return super().update(instance, validated_data)