from django.urls import path,include
from .import views
urlpatterns = [
    path('about',views.about,name='about'),
    path('blog_single',views.blog_single,name='blog_single'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('faq',views.faq,name='faq'),
    path('gallery',views.gallery,name='gallery'),
    path('index',views.index,name='index'),
    path('job_listings',views.job_listings,name='job_listings'),
    path('job_single/<int:id>',views.job_single,name='job_single'),
    path('main',views.main,name='main'),
    path('portfolio_single',views.portfolio_single,name='portfolio_single'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('service_single',views.service_single,name='service_single'),
    path('services',views.services,name='services'),
    path('testimonials',views.testimonials,name='testimonials'),
    path('admindash',views.admindash,name='admindash'),
    path('adminloginpage',views.adminloginpage,name='adminloginpage'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('employersreg',views.employersreg,name='employersreg'),
    path('register_employers',views.register_employers,name='register_employers'),
    path('employerlogin',views.employerlogin,name='employerlogin'),
    path('employersdash',views.employersdash,name='employersdash'),
    path('login_employer',views.login_employer,name='login_employer'),
    path('viewemployerspage',views.viewemployerspage,name='viewemployerspage'),
    path('employer_displaypage',views.employer_displaypage,name='employer_displaypage'),
    path('postjobpage',views.postjobpage,name='postjobpage'),
    path('delete_employers/<int:id>',views.delete_employers,name='delete_employers'),
    path('post_job',views.post_job,name='post_job'),
    path('viewjob',views.viewjob,name='viewjob'),
    path('job',views.job,name='job'),
    path('delete_jobs/<int:id>',views.delete_jobs,name='delete_jobs'),
    path('indexpage',views.indexpage,name='indexpage'),
    path('singlejob',views.singlejob,name='singlejob'),
    path('userreg',views.userreg,name='userreg'),
    path('register_jobseekers',views.register_jobseekers,name='register_jobseekers'),
    path('userdash',views.userdash,name='userdash'),
    path('login_jobseeker',views.login_jobseeker,name='login_jobseeker'),
    path('userpro',views.userpro,name='userpro'),
    path('apply_job/<int:id>',views.apply_job,name='apply_job'),
    path('logout_admin',views.logout_admin,name='logout_admin'),
    path('logout_jobseeker',views.logout_jobseeker,name='logout_jobseeker'),
    path('getAplication/<int:id>', views.getApllication, name='getApplication'),
 ]