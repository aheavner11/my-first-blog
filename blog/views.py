from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

# Create your views here.
#adding a comment
#adding another comment
#adding a third comment
