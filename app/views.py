from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from app.models import Post,Category
from django.views.generic.base import TemplateView, RedirectView
from app.serializers import PostSerializer
from app.forms import ContactForm, PostForm
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from app.auth import CustomAuth
# Create your views here.
class Contact(TemplateView):
    template_name = 'app/contact.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        forms = ContactForm()
        context = {'form':forms}
        return context
    def post(self, request):
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save() 
            return HttpResponseRedirect('/')
class CreatePost(TemplateView):
    template_name = 'app/create.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        postblog = Post.objects.all()
        formz = PostForm()
        context = {'forms':formz,'allblogs':postblog}
        return context
    def post(self, request):
        formz = PostForm(request.POST)
        if formz.is_valid():
            formz.save()
            return HttpResponseRedirect('/')
class Home(TemplateView):
    template_name = 'app/index.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        all_posts_to_display = Post.objects.filter(is_active=True)
        all_cat = Category.objects.all()
        print('---'*40)
        print(all_cat)
        context = { 'allposts':all_posts_to_display, 'categories':all_cat}
        return context
def bolgpost(request, slug):
    blog_post_slug = Post.objects.filter(slug=slug).first()
    context = {'blogslug':blog_post_slug}
    return render(request, 'app/blogpost.html', context)
class DeletePost(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_post = kwargs['id']
        Post.objects.get(pk=del_post).delete()
        return super().get_redirect_url(*args, **kwargs)
class Update(View):
    def get (self, request, id):
        get_post_id = Post.objects.get(pk=id)
        form = PostForm(instance=get_post_id)
        return render(request, 'app/update.html', {'form':form})
    def post(self, request, id):
        get_post_id = Post.objects.get(pk=id)
        form = PostForm(request.POST, instance=get_post_id)
        if form.is_valid():
            form.save() 
        return render(request, 'app/update.html', {'form':form})
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title','content']
    authentication_classes = [CustomAuth]
    permission_classes =[IsAuthenticated]
class ReadOnlyPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # insert username in url to call API