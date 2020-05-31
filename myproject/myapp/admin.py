from django.contrib import admin

# Register your models here.

from myapp.models import login
from myapp.models import session
from myapp.models import student
admin.site.register(login)
admin.site.register(session)
admin.site.register(student)
