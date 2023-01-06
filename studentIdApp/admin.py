from django.contrib import admin
from .models import User,Teacher,Student
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ExportActionMixin
# Register your models here.

class studentAdmin(ExportActionMixin,admin.ModelAdmin):    
    list_display=('fullname', 'father',"mother",'phno','ephno',"dob",'address','photo','role','rollNumber','standard')
    list_filter =['users']
admin.site.register(Student,studentAdmin)

class teacherAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=('fullname', 'father',"mother",'phno','ephno',"dob",'address','photo','role')
    list_filter =['usert']
admin.site.register(Teacher,teacherAdmin)



admin.site.register(User,UserAdmin)

