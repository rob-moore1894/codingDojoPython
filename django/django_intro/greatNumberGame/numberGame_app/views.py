from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'randnum' not in request.session:
        request.session['randnum'] = random.randint(1,100)
        print(request.session['randnum'])
    return render(request, "index.html")

def guess(request):
    user_guess = int(request.POST['user_guess'])
    if request.session['randnum'] == user_guess:
        print("Got it right!")
        request.session.clear()
    elif request.session['randnum'] > user_guess:
        print("Too Low")
    elif request.session['randnum'] < user_guess:
        print("Too High")
    return redirect("/")