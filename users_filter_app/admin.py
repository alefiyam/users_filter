from django.contrib import admin
from users_filter_app.models import *

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)