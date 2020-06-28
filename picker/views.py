from django.shortcuts import render, get_object_or_404, redirect
from .models import Number

# Create your views here.
def result(request):
    num = Number.objects.last()
    return render(request, 'result.html', {'num': num})

def change(request):
    import random
    
    ran_num = random.randrange(1, 11)
    if ran_num == 1:
        num = 1
    elif ran_num in range(2,4): # 2, 3
        num = 2
    elif ran_num in range(4, 8): # 4, 5, 6, 7
        num = 3
    elif ran_num in range(9, 10): # 8, 9
        num = 4
    else: # 10
        num = 5
    numbers = Number.objects.all()
    numbers.delete()
    Number.objects.create(number=num)
    return redirect('result')

def fever(request):
    import random

    ran_num = random.randrange(1, 15)
    if ran_num == 1:
        num = 1
    elif ran_num in range(2, 4): # 2, 3
        num = 2
    elif ran_num in range(4, 6): # 4, 5
        num = 3
    elif ran_num in range(6, 8): # 6, 7
        num = 4
    elif ran_num == 8:
        num = 5
    elif ran_num in range(9, 12): # 9, 10, 11
        num = 0
    else: # 12, 13, 14
        num = 6
    numbers = Number.objects.all()
    numbers.delete()
    Number.objects.create(number=num)
    return redirect('result')