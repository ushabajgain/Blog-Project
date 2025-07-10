from django.shortcuts import get_object_or_404, render, redirect
from ..models import Blog
from django.contrib.auth.decorators import login_required

def index(request):
    blog = Blog.objects.all()
    
    return render(request, 'main/index.html', {'blog': blog})

@login_required
def create_blog(request):
    errors = {}

    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        description = request.POST.get('description')

        if not title:
            errors['title'] = "Title is required"

        if not category:
            errors['category'] = "Category is required"

        if not image:
            errors['image'] = "Image is required"    

        if not description:
            errors['description'] = "Description is required"

        if errors:
            return render(request, 'main/create_blog.html', {
                'errors': errors,
                'data': request.POST
            })

        Blog.objects.create(
            title=title,  
            category=category,
            image=image,
            description=description,
            author=request.user
        )

        return redirect('index')

        # return render(request, 'main/create_blog.html', {
        #     'message': "Blog Posted Successfully"
        # })

    
    return render(request, 'main/create_blog.html')

def single_page(request, id): 
    # blog = Blog.objects.get(id=id)
    blog = get_object_or_404(Blog, id=id)
    print(blog)
    return render(request,'main/single_page.html',{'blog':blog})