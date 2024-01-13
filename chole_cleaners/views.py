from django.shortcuts import render
from .models import Service, Contact, AboutUs, Career, Tender, Blog, Comment
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, UserProfileForm
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CommentForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def contact(request):
    if request.method == 'POST':
        # Handle form submission here
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, phone=phone, message=message)

    return render(request, 'contact.html')


def about_us(request):
    directors = AboutUs.objects.filter(title='Board of Directors').exclude(name__isnull=True, content__isnull=True)
    return render(request, 'aboutus.html', {'directors': directors})

def careers(request):
    careers_list = Career.objects.all()
    return render(request, 'careers.html', {'careers_list': careers_list})

def tenders(request):
    tenders_list = Tender.objects.all()
    return render(request, 'tenders.html', {'tenders_list': tenders_list})

def blogs(request):
    blogs_list = Blog.objects.all()
    return render(request, 'blog.html', {'blogs_list': blogs_list})

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog_item'

class BlogsListView(ListView):
    model = Blog
    template_name = 'blogs_list.html'  # Replace with your actual template
    context_object_name = 'blogs'

def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('blog_detail', args=[blog_id]))
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})