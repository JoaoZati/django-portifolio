from django.shortcuts import render


# Create your views here.
def description(request):
    context = {}
    return render(request, 'applications/description.html', context)
