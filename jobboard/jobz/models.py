from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customuser(AbstractUser):
  is_Job_Seekers=models.BooleanField(default=False)
  is_Company=models.BooleanField(default=False)

class Company(models.Model):
  user=models.OneToOneField('Customuser',on_delete=models.CASCADE,related_name='company')
  name=models.CharField(max_length=100)
  image=models.ImageField(upload_to='Company/')
  phno=models.IntegerField()
  email=models.EmailField(max_length=100)

class job_seekers(models.Model):
  user=models.OneToOneField('Customuser',on_delete=models.CASCADE, related_name='jobseeker')
  name=models.CharField(max_length=100)
  image=models.ImageField(upload_to='job_seekers/',null=True,blank=True)
  phno=models.IntegerField()
  email=models.EmailField(max_length=100)

class postjob(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_discription=models.CharField(max_length=300,default="Default description")
    category = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    job_type = models.CharField(max_length=20)
    image=models.ImageField(upload_to='job/',null=True,blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateTimeField()

class JobApplication(models.Model):
    job = models.ForeignKey(postjob, on_delete=models.CASCADE, related_name='job')
    applicant = models.ForeignKey(job_seekers, on_delete=models.CASCADE, related_name='application')
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

# class review(models.model):
#     company = models.ForeignKey(employers, on_delete=models.CASCADE)
#     reviewer = models.ForeignKey(employers, on_delete=models.CASCADE, related_name='reviews')
#     comment = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

   




