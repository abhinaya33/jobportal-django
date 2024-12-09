from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from . models import Customuser,Company,postjob,job_seekers,JobApplication
from django . http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def about(request):
    return render(request,'about.html')
def blog_single(request):
    return render(request,'blog-single.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def faq(request):
    return render(request,'faq.html')
def gallery(request):
    return render(request,'gallery.html')
def index(request):
    return render(request,'index.html')
def job_listings(request):
    return render(request,'job-listings.html')
def job_single(request,id):
    x=postjob.objects.get(id=id)
    return render(request,'job-single.html',{'data':x})
# def login(request):
#     return render(request,'login.html')
def main(request):
    return render(request,'main.html')
def portfolio_single(request):
    return render(request,'portfolio-single.html')
def portfolio(request):
    return render(request,'portfolio.html')
# def post_job(request):
#     return render(request,'post-job.html')
def service_single(request):
    return render(request,'service-single.html')
def services(request):
    return render(request,'services.html')
def testimonials(request):
    return render(request,'testimonials.html')
def admindash(request):
    return render(request,'admintemplate/admindash.html')
def employerlogin(request):
    return render(request,'employertemplate/login.html')
def adminloginpage(request):
    return render(request,'admintemplate/adminloginpage.html')
def adminlogin(request):
    if request.method=='POST':
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None and user.is_superuser:
            login(request,user)
            next=request.GET.get('next')
            if next:
                return redirect(next)
            return redirect(admindash)
        else:
            messages.error(request,'invalid credential')
    return render(request,'admintemplate/adminloginpage.html')        
def employersreg(request):
    return render(request,'employertemplate/employerregistration.html')
def register_employers(req):
    if req.method=='POST':
        na=req.POST['name']
        un=req.POST['username']
        sim=req.FILES['simg']
        em=req.POST['email']
        ph=req.POST['phno']
        pa=req.POST['password']
        x=Customuser.objects.create_user(username=un,password=pa,email=em,is_Company=True)
        y=Company.objects.create(name=na,image=sim,email=em,phno=ph,user=x)
        y.save()
        return redirect(login_employer)
    else:
        return render(req,'employertemplate/employerregistration.html')
    
def employersdash(request):
    return render(request,'employertemplate/employerdash.html')
def login_employer(request):
    if request.method=='POST':
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None and user.is_Company:
            login(request,user)
            next=request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('employersdash')
        else:
            messages.error(request,'invalid credential')
    return render(request,'employertemplate/login.html')   
def viewemployerspage(request):
    data=Company.objects.all
    return render(request,'admintemplate/view_employers.html',{'data:data'})    
@login_required 
def employer_displaypage(request):
    logined_user=request.user.id
    employers_data=Company.objects.all()
    return render(request,'admintemplate/view_employers.html',{'employers_data':employers_data})    
def postjobpage(request):
    return render(request,'employertemplate/postjob.html')
def delete_employers(request,id):
    x=Company.objects.get(id=id)
    x.delete()
    return redirect(employer_displaypage)
@login_required
def post_job(request):
    if request.method == 'POST':
        tit = request.POST['title']
        com=request.POST['company']
        jdes = request.POST['description']
        cdd = request.POST['comdescription']
        cat = request.POST['category']
        loc = request.POST['location']
        sa = request.POST['salary']
        typ = request.POST['jobtype']
        clo = request.POST['closing_date']
        imgg= request.FILES['logo']
        x=postjob.objects.create(company=request.user.company,job_title=tit,company_discription=jdes,category=cat,description=cdd,location=loc,salary=sa,job_type=typ,image=imgg,closing_date=clo)
        x.save()
        messages.success(request, 'Job added successfully!')
        return redirect(job)
    return render(request, 'employertemplate/postjob.html')

def viewjob(request):
    return render(request,'employertemplate/viewjobs.html') 
def job(request):
    x=postjob.objects.filter(company=request.user.company)
    return render(request,'employertemplate/viewjobs.html',{'x':x})
def delete_jobs(request,id):
    x=postjob.objects.get(id=id)
    x.delete()
    return redirect(job)
def indexpage(request):
    all_job=postjob.objects.all()
    job_count = all_job.count() 
    company = Company.objects.all().count()
    jobseeker = job_seekers.objects.all().count()
    return render(request,'index.html',{'all_job':all_job, 'job_count':job_count, 'company':company, 'jobseeker':jobseeker})

def singlejob(request):
    return render(request,'base1.html')
def userreg(request):
    return render(request,'userprofile/userreg.html')
def register_jobseekers(req):
    if req.method=='POST':
        na=req.POST['name']
        un=req.POST['username']
        sim=req.FILES['simg']
        em=req.POST['email']
        ph=req.POST['phno']
        pa=req.POST['password']
        x=Customuser.objects.create_user(username=un,password=pa,email=em,is_Job_Seekers=True)
        y=job_seekers.objects.create(name=na,image=sim,email=em,phno=ph,user=x)
        y.save()
        return redirect(login_jobseeker)
    else:
        return render(req,'userprofile/userreg.html')
def userdash(request):
    return render(request,'userprofile/userdash.html')  
def login_jobseeker(request):
    if request.method=='POST':
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None and user.is_Job_Seekers:
            login(request,user)
            next=request.GET.get('next')
            if next:
                return redirect(next)
            return redirect(indexpage)
        else:
            messages.error(request,'invalid credential')
    return render(request,'userprofile/userreg.html') 

def userpro(request):
    return render(request,'userprofile/profile.html')

@login_required(login_url='/jobz/login_jobseeker')
def apply_job(request,id):
    data = job_seekers.objects.get(user=request.user)
    jobs = postjob.objects.get(id=id)
    if request.method == 'POST':
        # jb=request.POST['job']
        # aplct=request.POST['applicant']
        res=request.FILES['resume']
        covl=request.POST['cover_letter']
        x=JobApplication.objects.create(job=jobs,applicant=request.user.jobseeker,resume=res,cover_letter=covl)
        x.save()
        messages.success(request, 'job applied')
        return redirect(indexpage)
    return render(request,'userprofile/jobapply.html',{'job_seekers':data,'id':id})
    
def logout_admin(request):
    logout(request)
    return redirect('adminloginpage')

def logout_jobseeker(request):
    logout(request)
    return redirect('login_jobseeker')    

def getApllication(request,id):
    pstJob = postjob.objects.get(id=id)
    job = JobApplication.objects.filter(job=pstJob)
    return render(request, 'employertemplate/displyuserdetails.html', {'job':job})






        






        