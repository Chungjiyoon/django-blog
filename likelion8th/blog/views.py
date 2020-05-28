from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from .form import BlogForm
# Create your views here.

def list(request):
    blogs= Blog.objects.all()
    return render(request, 'list.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk = blog_id) #객체 하나하나를 식별할 수 있는 식별자=pk=아이덴티티
    return render(request, 'detail.html',{'blog':blog})

def new(request):
#1. 데이터가 입력된 후 제출 버튼을 누르고 데이터 저장 = post why? 눈으로 못봐서
#2. 정보가 입력되지 않은 빈칸으로 되어있는 페이지 보여주기 = get url을 통해 눈으로 보여지기 때문
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('list')
            
    else:
        form = BlogForm()
        return render(request, 'new.html', {'form':form})

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.pub_date = timezone.datetime.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('/blog/'+str(new_blog.id)) #/하나 더 붙이면 /blog/blog 했을 때 앞의 blog가 사라짐

def edit(request,blog_id):
    edit_blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'edit.html',{'blog':edit_blog})

def update(request,blog_id):
    update_blog = get_object_or_404(Blog, pk = blog_id)
    update_blog.title = request.POST['title']
    update_blog.pub_date = timezone.datetime.now()
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request,blog_id):
    delete_blog = get_object_or_404(Blog, pk = blog_id)
    delete_blog.delete()
    return redirect('list')