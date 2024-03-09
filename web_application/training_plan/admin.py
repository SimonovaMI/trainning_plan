from django.contrib import admin
from .models import FitnessClub, ClubZone, ClubCard, UserAdditionalInfo, Group, Schedule, Plan, PlanGroup
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class UserAdditionalInfoInline(admin.StackedInline):
    model = UserAdditionalInfo
    can_delete = False


class CustomizedUserAdmin(UserAdmin):
    inlines = (UserAdditionalInfoInline,)


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(FitnessClub)
admin.site.register(ClubZone)
admin.site.register(ClubCard)
admin.site.register(Group)
admin.site.register(Schedule)
admin.site.register(Plan)
admin.site.register(PlanGroup)

