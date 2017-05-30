from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from djangoweliang.models import *

class MyUserInline(admin.StackedInline):
    model = MyUser
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (MyUserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(House)
admin.site.register(Reviews)
# Register your models here.
