from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import Post

def home(request):
    return render(request,"sayfalar/index.html",{'title':'Emekliye Kredi'})
def about(request):
    return render(request, "sayfalar/about.html", {'title':'Hakkımızda'})
def basvuru(request):
    return render(request, "sayfalar/basvuru.html", {'title':'Kredi Başvurusu'})
def contact(request):
    return render(request, "sayfalar/contact.html", {'title':'Bize Ulaşın'})
def EmekliyeKredi(request):
    return render(request, "sayfalar/EmekliyeKredi.html", {'title':'Emekliye Kredi'})
def ptt_kredi(request):
    return render(request, "sayfalar/ptt_kredi.html", {'title':'Ptt Kredi'})
def SicilBozuk(request):
    return render(request, "sayfalar/SicilBozuk.html", {'title':'Sicili Bozuk'})
def kisisel(request):
    return render(request, "sayfalar/Docs/Documents/KisiselVerilerinKorunmasi.pdf", {})
def posts(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'posts.html',context,{'title':'Yorumlar'})
def login(request):
    return render(request,'login.html',{'title':'Giriş'})
def logout(request):
    return render(request,'logout.html',{'title':'Çıkış'})
# def register(request):
#     return render(request,'register.html',{'title':'Kayıt Ol'})

class PostListView(ListView):
    model = Post
    template_name='sayfalar/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name='sayfalar/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name='sayfalar/post_detail.html'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        Post = self.get_object()
        if self.request.user == Post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        Post = self.get_object()
        if self.request.user == Post.author:
            return True
        return False