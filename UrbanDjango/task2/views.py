from django.shortcuts import render
from django.views.generic import TemplateView


# Create your view here
def index(request):
    return render(request, 'class_template.html')


def index2(request):
    return render(request, 'func_template.html')