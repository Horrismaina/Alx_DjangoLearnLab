from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser, UserProfile

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search capability for these fields
    search_fields = ['title', 'author']
    
    # Add filter options in the right sidebar
    list_filter = ('publication_year', 'author')
    
    # Add field ordering
    ordering = ('title',)

# Customizing the admin interface for CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Display the following fields in the list view of the admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')
    
    # Specify the fields to be used in the forms for adding and editing users
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Add search functionality for CustomUser
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Add filter options for CustomUser
    list_filter = ('is_staff', 'is_superuser', 'is_active')

# Register UserProfile with the admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role')
    list_filter = ('role',)
