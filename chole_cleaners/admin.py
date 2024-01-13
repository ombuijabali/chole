from django.contrib import admin
from .models import Service, Contact, AboutUs, Career, Tender, Blog, UserProfile, Comment

# Register your models here.
# cleaning_company/admin.py

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('user__username', 'first_name', 'last_name', 'email', 'phone_number')