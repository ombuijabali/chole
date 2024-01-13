# Create your models here.
# cleaning_company/models.py

from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Services"

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Contacts"

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(upload_to='director_images/', null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "AboutUs"

class Career(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Careers"

class Tender(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Tenders"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blogs"

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.blog.title}'
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "UserProfiles"