from django.contrib import admin
from .models import Student
# Register your models here.
class InformationAdmin(admin.ModelAdmin):
    list_display=('username','Email_address','first_name','gender','dob')
admin.site.register(Student,InformationAdmin)