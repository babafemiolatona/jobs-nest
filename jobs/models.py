from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    TYPE = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    location = models.CharField(max_length=200, null=False, blank=False)
    type = models.CharField(max_length=200, choices=TYPE, null=False, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateTimeField(null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    website = models.URLField(null=False, blank=False)
    # logo = models.ImageField(upload_to='company_logos/', null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    resume = models.FileField(upload_to='uploads/', null=False, blank=False)
    cover_letter = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    is_shortlisted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class UserProfile(models.Model):
    USER_TYPE = (
        ('Employer', 'Employer'),
        ('Job Seeker', 'Job Seeker'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=200, choices=USER_TYPE, null=False, blank=False)    
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username
