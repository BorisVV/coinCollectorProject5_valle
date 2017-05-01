from django.contrib import admin

from .models import DisplayQuarters, Join

admin.site.register(DisplayQuarters)


class JoinAdmin(admin.ModelAdmin):
    # list_display = ['email', 'time', 'updated']
    class Meta:
        model = Join

admin.site.register(Join, JoinAdmin)



# class PersonInline(admin.StackedInline):
#     """ Details a person in line. """
#     model = Person
#     can_delete = False
#     verbose_name_plural = 'person'
#
#     fields = ('username', 'email', 'first_name', 'last_name', 'age') #, 'city', 'state')
#
# class UserAdmin(UserAdmin):
#     inlines = [
#         PersonInline
#     ]
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
