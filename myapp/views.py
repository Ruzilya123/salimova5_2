from django.shortcuts import render
from .forms import Form
from .models import Post

def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        content = request.POST['content']
        Post.objects.create(title=title, url=url, content=content)
    return render(request, 'index.html', context={'articles': Post.objects.all()})


def form(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            return render(request, 'form.html', context={
                'form': form,
                'data': request.POST
            })
    else:
        form = Form()
    
    print([i for i in form])
    
    return render(request, 'form.html', {'form': Form})
