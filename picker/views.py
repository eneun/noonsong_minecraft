from django.shortcuts import render, get_object_or_404, redirect
from .models import Number

# Create your views here.
def result(request):
    num = Number.objects.last()
    return render(request, 'result.html', {'num': num})

def change(request):
    import random
    import datetime
    num = random.randrange(1, 6)
    Number.objects.create(number=num)
    return redirect('result')