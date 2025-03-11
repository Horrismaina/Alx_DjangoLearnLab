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

# CustomUserAdmin to manage CustomUser in the admin
class CustomUserAdmin(UserAdmin):
    # Define the fields to display in the list view
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    
    # Define the fields to search for
    search_fields = ('username', 'email')
    
    # Add filters in the right sidebar
    list_filter = ('is_staff', 'is_active')
    
    # Define the fieldsets to control how the fields are displayed in the admin form
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Define the fields for adding new users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    
    ordering = ('username',)

# Register CustomUser with CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

# Register UserProfile for management in the admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role')

