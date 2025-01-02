from django.contrib import admin
from .models import News, Semester, StudyProgram, Module, UserStudyProgram, StudentModule, Appointment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')

@admin.register(StudyProgram)
class StudyProgramAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester')
    search_fields = ('name', 'description')
    list_filter = ('semester', 'study_programs')

@admin.register(UserStudyProgram)
class UserStudyProgramAdmin(admin.ModelAdmin):
    list_display = ('user', 'study_program')
    search_fields = ('user__username', 'study_program__name')


@admin.register(StudentModule)
class StudentModuleAdmin(admin.ModelAdmin):
    list_display = ('user', 'module', 'is_active')
    list_filter = ('is_active', 'module')
    search_fields = ('user__username', 'module__name')
    
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'scheduled_at', 'display_users', 'category')
    search_fields = ('title', 'description')
    list_filter = ('scheduled_at','category')

    def display_users(self, obj):
        return ", ".join([user.username for user in obj.users.all()])
    display_users.short_description = 'Benutzer'
