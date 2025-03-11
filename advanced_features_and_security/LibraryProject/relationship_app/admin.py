from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile, Author, Librarian, Book

# Custom user admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'date_of_birth', 'profile_photo', 'is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Librarian)
admin.site.register(Book)
