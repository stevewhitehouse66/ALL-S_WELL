from django.shortcuts import render
from .models import About

def about_page(request):
    about_content = About.objects.first()  # Assuming there's only one about content for simplicity
    return render(request, 'about/about_page.html', {'about_content': about_content})
