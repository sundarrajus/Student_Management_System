from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Student, CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.core.paginator import Paginator
import csv
from django.http import HttpResponse
from django.db.models import Count


# logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# Delete
@login_required
def delete_student(request, id):

    student = get_object_or_404(Student,id=id)
    if request.user.role != 'admin' and student.added_by != request.user:
        return redirect('student_list')

    student.delete()

    return redirect('student_list')

# Edit
@login_required
def edit_student(request, id):
    student = get_object_or_404(Student,id=id)
    if request.user.role != 'admin' and student.added_by != request.user:
        return redirect('student_list')

    if request.method == "POST":

        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.place = request.POST.get('place')
        student.gender = request.POST.get('gender')
        student.state = request.POST.get('state')

        skills = request.POST.getlist('skillset')
        student.skillset = ",".join(skills)
        student.save()
        return redirect('student_list')

    # users = CustomUser.objects.all()

    skills = student.skillset.split(",") if student.skillset else []

    context = {
        'student': student,
        # 'users': users,
        'skills': skills
    }

    return render(request,'add_student.html',context)

# student_list
@login_required
def student_list(request):
    query = request.GET.get('q')
    if request.user.role == 'admin':
        students = Student.objects.all()
    else:
        students = Student.objects.filter(added_by=request.user)

    if query:
        students = students.filter(name__icontains=query)

    paginator = Paginator(students, 10)   # 10 students per page
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    context = {
        'students': students
    }
    return render(request,'student_list.html',context)


# student detail
@login_required
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    if request.user.role != 'admin' and student.added_by != request.user:
        return redirect('student_list')

    skills = student.skillset.split(",") if student.skillset else []

    context = {
        'student': student,
        'skills': skills
    }

    return render(request, 'student_detail.html', context)


# Add Student
@login_required
def add_student(request):
    if request.method == "POST":

        # added_by = request.POST.get('added_by')
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        place = request.POST.get('place')
        gender = request.POST.get('gender')
        state = request.POST.get('state')

        skills = request.POST.getlist('skillset')
        skillset = ",".join(skills)

        Student.objects.create(
            added_by=request.user,
            name=name,
            email=email,
            age=age,
            place=place,
            gender=gender,
            state=state,
            skillset=skillset
        )

        messages.success(request,"Student added successfully")
        return redirect('student_list')

    # users = CustomUser.objects.all()
    return render(request,'add_student.html')


User = get_user_model()

# Register
def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request,"Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            role='staff'
        )

        messages.success(request,"Account created successfully")
        return redirect('login')

    return render(request,'register.html')

# login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid username or password")

    return render(request,'login.html')


# Dashboard
@login_required
def dashboard(request):

    total_students = Student.objects.count()
    total_staff = CustomUser.objects.filter(role='staff').count()
    my_students = Student.objects.filter(added_by=request.user).count()

    state_data = Student.objects.values('state').annotate(count=Count('state'))

    states = []
    counts = []

    recent_students = Student.objects.order_by('-id')[:5]

    for data in state_data:
        states.append(data['state'])
        counts.append(data['count'])

    context = {
        'total_students': total_students,
        'total_staff': total_staff,
        'my_students': my_students,
        'states': states,
        'counts': counts,
        'recent_students': recent_students
    }

    return render(request,'dashboard.html',context)

# Export the students data
@login_required
def export_students(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)

    writer.writerow(['Name', 'Email', 'Age', 'Place', 'Gender', 'State', 'Skills', 'Added By'])

    students = Student.objects.all()

    for student in students:
        writer.writerow([
            student.name,
            student.email,
            student.age,
            student.place,
            student.gender,
            student.state,
            student.skillset,
            student.added_by.username
        ])

    return response