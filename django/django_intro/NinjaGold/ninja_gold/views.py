from django.shortcuts import render, redirect
from datetime import datetime
import random

# Create your views here.
def index(request):
    if 'total_gold' not in request.session: 
        request.session['total_gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, "index.html")

def process_money(request):
    now = datetime.now()
    current_time = now.strftime("(%Y/%m/%d %I:%M %p)")
    if request.POST['location'] == 'farm':
        gold = random.randint(10, 20)
    elif request.POST['location'] == 'cave':
        gold = random.randint(5, 10)
    elif request.POST['location'] == 'house':
        gold = random.randint(2, 5)
    elif request.POST['location'] == 'casino':
        gold = random.randint(-50, 50)
    request.session['total_gold'] += gold

    if gold < 0:
        request.session['activities'].append({'message':f"Entered a casino and lost {abs(gold)} golds...Ouch {current_time}", 'action':'lost'})
    else:
        request.session['activities'].append({'message':f"Earned {gold} from the {request.POST['location']}! {current_time}", 'action':'gained'})
    return redirect('/')