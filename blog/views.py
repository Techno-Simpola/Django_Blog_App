from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def addPost(request):
    submitted = False
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addPost?submitted=True')

    else:
        form = PostForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'addPost.html', {'form': form, 'submitted': submitted})
