from django.shortcuts import render

# Create your views here.

def test_view(request):
    context = {
        'message': 'Hello, Django!'
    }
    return render(request, 'test_template.html', context)