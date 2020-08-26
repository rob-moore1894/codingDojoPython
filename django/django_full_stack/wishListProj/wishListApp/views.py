from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users, Products
from django.db.models import Q
import bcrypt

# Create your views here.
def index(request):
    return redirect('/main')

def main(request):
    return render(request, "index.html")

def register(request):
    regValidation = Users.objects.regValidator(request.POST)
    print(regValidation)
    if len(regValidation) > 0:
        for value in regValidation.values():
            messages.error(request, value)
        return redirect('/main')
    else:
        #encrypt the password first
        hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        newUser = Users.objects.create(name = request.POST['name'], username= request.POST['username'], password= hashedPw, date_hired=request.POST['date-hired'])
        request.session['loggedInId'] = newUser.id 

    return redirect('/dashboard')

def login(request):
    loginValidation = Users.objects.loginValidator(request.POST)
    print(loginValidation)
    if len(loginValidation) > 0:
        for value in loginValidation.values():
            messages.error(request, value)
        return redirect('/main')
    else: 
        usersByUsername = Users.objects.filter(username= request.POST['usernameLogin'])
        request.session['loggedInId'] = usersByUsername[0].id
        return redirect('/dashboard')


def dashboard(request):
    context = {
        'loggedInUser': Users.objects.get(id=request.session['loggedInId']),
        'all_items': Products.objects.all(),
        'all_users': Users.objects.all(),
        'user_items': Products.objects.filter(Q(favoriters= Users.objects.get(id=request.session['loggedInId'])) | Q(uploader = Users.objects.get(id=request.session['loggedInId']))),
        'other_users_items': Products.objects.exclude(uploader = Users.objects.get(id=request.session['loggedInId'])),
    }
    return render(request, "dashboard.html", context)

def createItemView(request):
    return render(request, "createItem.html")

def createItem(request):
    itemValidation = Users.objects.productValidator(request.POST)
    print(itemValidation)
    if len(itemValidation) > 0:
        for value in itemValidation.values():
            messages.error(request, value)
        return redirect('/wish_items/create')
    else:
        this_user = Users.objects.get(id=request.session['loggedInId'])
        print(request.session['loggedInId'])
        print(f"User = {this_user}")
        newItem = Products.objects.create(item = request.POST['item-product'], uploader=this_user)
        print(f"Item = {newItem.item}; Added By = {newItem.uploader.username}; ")
    return redirect('/dashboard')

def viewItem(request, itemId):
    context = {
        'oneItem': Products.objects.get(id= itemId), 
    }
    return render(request, "item.html", context)

def addItem(request, itemId):
    print(itemId)
    user_adding = Users.objects.get(id=request.session['loggedInId'])
    item_adding = Products.objects.get(id = itemId)
    user_adding.products_favorited.add(item_adding)
    return redirect('/dashboard')

def removeItem(request, itemId):
    user_removing = Users.objects.get(id=request.session['loggedInId'])
    item_removing = Products.objects.get(id = itemId)
    user_removing.products_favorited.remove(item_removing)
    return redirect('/dashboard')


def delete(request, itemId):
    Products.objects.filter(id=itemId).delete()
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/main')