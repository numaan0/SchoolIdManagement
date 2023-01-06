from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from . import models
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
# Create your views here.
try:
    
    def index(request):
        if request.method=="POST":
            username= request.POST['username']
            password= request.POST['password']                       
            Luser = authenticate(request,username=username,password=password)
            print(Luser)
            if Luser is not None:
                auth.login(request, Luser)
                return redirect('home')
            else:
                messages.info(request,"Invalid Credentials")
                return redirect('index')
        return render(request,'index.html')
    
    def register(request):
        if request.method == "POST":
            sname = request.POST['sname']
            email = request.POST['emailSignup']
            password = request.POST['password']
            phonenumber = request.POST['phonenumber']
            username= str(sname.replace(" ",""))
            user= models.User.objects.create_user(schoolname=sname,password=password,email=email,username=email)
            user.save()
            print("done")
            return redirect('/home')
        
        return render(request,"register.html")
    
    @login_required
    def home(request):
        if request.method=="POST":
            fname=request.POST["name"]
            father=request.POST["father"]
            mother=request.POST["mother"]
            phone=request.POST["pnumber"]
            enumber=request.POST["enumber"]
            dob=request.POST["dob"]
            address=request.POST["address"]
            photo=request.FILES["photo"]
            role=request.POST['role']
            if role == 'Teacher':
                Tdata= models.Teacher.objects.create(usert=request.user,fullname=fname,father=father,mother=mother,phno=phone,ephno=enumber,dob=dob,address=address,photo=photo,role=role)
                Tdata.save()
                redirect("/home")
            if role == 'Student':
                rollnumber=request.POST['rollNumber']
                standard= request.POST['standard']
                Sdata= models.Student.objects.create(users=request.user,fullname=fname,father=father,mother=mother,phno=phone,ephno=enumber,dob=dob,address=address,photo=photo,role=role,rollNumber=rollnumber,standard=standard)
                #Sdata.save()
                redirect("/home")
            else:
                return redirect("/home")
         
        return render(request,'homepage.html')

    @login_required
    def profile(request):
        cur=request.user
        students= models.Student.objects.filter(users=cur)
        teachercount=models.Teacher.objects.filter(usert=cur).count()  
        #oldImage=models.Teacher.objects.filter(fullname='Test Teacher 1').values_list('photo',flat=True) 
        if teachercount>0:
            print(teachercount)
            teachers=models.Teacher.objects.filter(usert=cur)
            stu={"students":students,"teachers":teachers}
        else:
            stu={"students":students}
        return render(request,'profile.html',stu)
    
    @login_required
    def editprofile(request,role,pk):
        studentdata=models.Student.objects.filter(id=pk).first()
        #teacherdata=models.Teacher.objects.filter(id=pk).first()
        cRole = role
        print(role)
        if request.method=="POST":
            fname=request.POST["name"]
            father=request.POST["father"]
            mother=request.POST["mother"]
            phone=request.POST["pnumber"]
            enumber=request.POST["enumber"]
            dob=request.POST["dob"]
            address=request.POST["address"]
            #photo=request.FILES["photo"]
            role=request.POST['role']
            print(role)
            if role=="Teacher":
                print("in teacher student in edit profile function")
                #oldImage=models.Teacher.objects.filter(id=pk).values_list('photo',flat=True).get
                """ oldImage=models.Teacher.objects.filter(id=pk).first()
                if os.path.exists(oldImage.photo.path):
                    os.remove(oldImage.photo.path)"""
                
                Ndata=models.Teacher.objects.create(usert=request.user,fullname=fname,father=father,mother=mother,phno=phone,ephno=enumber,dob=dob,address=address,role=role)
                Ndata.save()
                models.Student.objects.filter(id=pk).delete()
                print("done saving teacher in editprofile function")
                return redirect("/profile")
            if role=="Student":
                print("in student teacher function")
                rollnumber=request.POST['rollNumber']
                standard= request.POST['standard']
                models.Student.objects.filter(id=pk).update(users=request.user,fullname=fname,father=father,mother=mother,phno=phone,ephno=enumber,dob=dob,address=address,role=role,rollNumber=rollnumber,standard=standard)
                
                
                print("done saving Student")
                return redirect("/profile")
        
        data={"eData":studentdata, "role":cRole, "id":pk}
        return render(request,"editprofile.html",data)

    
    @login_required
    def editteacher(request,role,pk):
        studentdata=models.Student.objects.filter(id=pk).first()
        teacherdata=models.Teacher.objects.filter(id=pk).first()
        cRole = role
        print(role)
        if request.method=="POST":
            fname=request.POST["name"]
            father=request.POST["father"]
            mother=request.POST["mother"]
            phone=request.POST["pnumber"]
            enumber=request.POST["enumber"]
            dob=request.POST["dob"]
            address=request.POST["address"]
            #photo=request.FILES["photo"]
            role=request.POST['role']
            if role=="Student":
                print("in student edit teacher function")
                rollnumber=request.POST['rollNumber']
                standard= request.POST['standard']
                
                Ndata = models.Student.objects.create(users=request.user,fullname=fname,father=father,mother=mother,phno=phone,ephno=enumber,dob=dob,address=address,role=role,rollNumber=rollnumber,standard=standard)
                Ndata.save()
                models.Teacher.objects.filter(id=pk).delete()
                print("done saving Student edit teacher function")
                return redirect("/profile")
            if role=="Teacher":
                print("in teacher")
                #oldImage=models.Teacher.objects.filter(id=pk).values_list('photo',flat=True).get
                
                models.Teacher.objects.filter(id=pk).update(usert=request.user,fullname=fname,father=father,mother=mother,phno=phone,ephno=enumber,dob=dob,address=address,role=role)
                
                print("done saving teacher edit teacher function")
        
        
        data={"eData":teacherdata, "role":cRole, "id":pk}
        return render(request,"editteacher.html",data)
    
    @login_required
    def updateImage(request,role,pk):
        if role=="Teacher":
            if request.method == "POST":
                photo = request.FILES['photo']
                oldImage=models.Teacher.objects.filter(id=pk).first()
                print(oldImage.photo,photo)
                if os.path.exists(oldImage.photo.path) and oldImage.photo !="photos/default.png":
                        os.remove(oldImage.photo.path)
                        print("removed the image ",oldImage.photo)
                #models.Teacher.objects.filter(id=pk).update(usert=request.user,photo=photo)
                oldImage.photo=photo
                oldImage.save()
                return redirect("/profile")
            return render(request,'editteacher.html')
        if role == "Student":
            if request.method == "POST":
                photo = request.FILES['photo']
                oldImage=models.Student.objects.filter(id=pk).first()
                if os.path.exists(oldImage.photo.path) and oldImage.photo !="photos/default.png":
                        os.remove(oldImage.photo.path)
                        print("removed the image")
                #models.Student.objects.filter(id=pk).update(users=request.user,photo=photo)
                oldImage.photo=photo
                oldImage.save()
                return redirect("/profile")
            return render(request, 'editprofile.html')
    @login_required
    def log_out(request):
        logout(request)
        messages.success(request,"Logged out successfully")
        return redirect("/")
except Exception as e:
    
    redirect('index')
     