from django.contrib import admin
from api.models import Task

# Register your models here.
@admin.register(Task)
class TAskAdmin(admin.ModelAdmin):
    class Meta:
        model = Task
        list_display = ['id', 'title']

