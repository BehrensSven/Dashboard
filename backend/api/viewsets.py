from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .serializers import UserSerializer, NewsSerializer, ModuleSerializer, CompletedModuleSerializer, StudentProgressSerializer, AppointmentSerializer
from django.contrib.auth.models import User
from .models import News, StudentModule, UserStudyProgram, Appointment
from .permissions import IsOwnerOrAdmin

# --- ViewSets ---

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # Set permissions based on action
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action in ['modules', 'progress', 'completed_modules']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['get'], url_path='modules')
    def modules(self, request):
        # Return modules associated with the current user
        user = request.user
        student_modules = StudentModule.objects.filter(user=user)
        modules = [sm.module for sm in student_modules]
        serializer = ModuleSerializer(modules, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'], url_path='completed-modules', permission_classes=[IsAuthenticated])
    def completed_modules(self, request, pk=None):
        user = self.get_object()
        if request.user != user and not request.user.is_staff:
            raise PermissionDenied("You are not authorised to access this data.")
        student_modules = StudentModule.objects.filter(user=user, is_active=False).order_by('-completion_date')
        serializer = CompletedModuleSerializer(student_modules, many=True)
        return Response(serializer.data)    
    
    @action(detail=False, methods=['get'], url_path='progress', permission_classes=[IsAuthenticated])
    def progress(self, request):
        # Return progress data for the current user
        user = request.user
        try:
            UserStudyProgram.objects.get(user=user)
        except UserStudyProgram.DoesNotExist:
            return Response({'error': 'You are not enrolled in any degree program.'}, status=400)
        serializer = StudentProgressSerializer(user)
        return Response(serializer.data)
    
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        # Staff sees all appointments; regular users see nur ihre eigenen
        user = self.request.user
        if user.is_staff:
            return Appointment.objects.all()
        else:
            return Appointment.objects.filter(users=user)

    def perform_create(self, serializer):
        serializer.save()
        
    @action(detail=False, methods=['get'], url_path='appointments')
    def appointments(self, request):
        user = request.user
        appointments = Appointment.objects.filter(users=user)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
