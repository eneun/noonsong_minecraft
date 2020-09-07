from django.shortcuts import render, get_object_or_404, redirect
from .models import Number, Reservation

# Create your views here.
def result(request):
    num = Number.objects.last()
    return render(request, 'result.html', {'num': num})

def reservation(request):
    if request.method == 'POST':
        name = request.POST['name']
        value = Number.objects.last().number
        reservation = Reservation.objects.create(name=name, value=value)
        return redirect('reservation')
    else:
        reservations = Reservation.objects.all()
        return render(request, 'reservation.html', {'reservations': reservations})

def completion(request, id):
    reservation = get_object_or_404(Reservation, pk=id)
    if reservation.status == False:
        reservation.status = True
    else:
        reservation.status = False
    reservation.save()
    return redirect('reservation')

def delete(request):
    reservations = Reservation.objects.filter(status=True)
    reservations.delete()
    return redirect('reservation')

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

def generate():
    import random
    change = random.randrange(1, 10)
    if change == 1:
        pass
    elif change == 2:
        pass
    elif change == 3:
        pass
    else:
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