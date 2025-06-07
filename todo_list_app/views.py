from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import User, Task, Message
from django.contrib.auth import authenticate, login, logout
import re
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    today = datetime.date.today().strftime('%A %d/%m/%Y')

    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()

    return render(request, 'pages/index.html', {'tasks': tasks, 'user': request.user, 'today': today, 'completed': completed_tasks, 'pending': pending_tasks})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')

        user = User.objects.filter(email=email)

        if not email or not message_content or not full_name:
            return render(request, 'pages/contact.html', {'error': 'All fields are required.'})
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            return render(request, 'pages/contact.html', {'error': 'Invalid email format.'})

        message = Message.objects.create(
            content=message_content,
            user=user
        )
        message.save()

        return render(request, 'pages/contact.html', {'success': 'Message sent successfully!'})

    return render(request, 'pages/contact.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        configured_password = request.POST.get('password_confirmation')

        if not all([first_name, last_name, username, email, password, configured_password]):
            return render(request, 'pages/signup.html', {'error': 'All fields are required.'})
        if password != configured_password:
            return render(request, 'pages/signup.html', {'error': 'Passwords do not match.'})
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            return render(request, 'pages/signup.html', {'error': 'Invalid email format.'})
        if User.objects.filter(username=username).exists():
            return render(request, 'pages/signup.html', {'error': 'Username already exists.'})
        if User.objects.filter(email=email).exists():
            return render(request, 'pages/signup.html', {'error': 'Email already exists.'})
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    return render(request, 'pages/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, 'pages/login.html', {'error': 'Account inactive'})
            else:
                return render(request, 'pages/login.html', {'error': 'Invalid credentials'})
        except Exception as e:
            return render(request, 'pages/login.html', {'error': 'An error occurred. Please try again.'})

    return render(request, 'pages/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        user = request.user  # Assuming the user is logged in
        task = Task.objects.create(title=title, description=description, user=user)
        return HttpResponseRedirect(reverse("index"))


    return render(request, 'pages/index.html')

@login_required
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return HttpResponseRedirect(reverse("index"))
    except Task.DoesNotExist:
        return render(request, 'pages/task_not_found.html', {'task_id': task_id})

@login_required
def delete_completed_tasks(request):
    Task.objects.filter(completed=True).delete()
    return HttpResponseRedirect(reverse("index"))

@login_required
def update_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        if request.method == 'POST':
            task.title = request.POST.get('title', task.title)
            task.description = request.POST.get('description', task.description)
            task.completed = request.POST.get('completed', 'off') == 'on'
            task.save()
            return HttpResponseRedirect(reverse("index"))
        return render(request, 'pages/index.html', {'task': task})
    except Task.DoesNotExist:
        return render(request, 'pages/task_not_found.html', {'task_id': task_id})


