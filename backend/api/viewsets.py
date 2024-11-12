from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, NewsSerializer, ModuleSerializer
from django.contrib.auth.models import User
from .models import News, StudentModule

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'modules':
            permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    
    @action(detail=False, methods=['get'], url_path='modules')
    def modules(self, request):
        user = request.user
        student_modules = StudentModule.objects.filter(user=user)
        modules = [sm.module for sm in student_modules]
        serializer = ModuleSerializer(modules, many=True, context={'request': request})
        return Response(serializer.data)    
    
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]
