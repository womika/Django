from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'next_visit')
    ordering = ('id',)

admin.site.register(Doctor, DoctorAdmin)
