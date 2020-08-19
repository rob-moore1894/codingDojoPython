from django.shortcuts import render, redirect
from .models import Player, Fan
from django.contrib import messages

# Create your views here.
def index(request):
    print("wazaaaaaa")
    allPlayers = Player.objects.all()
    print(allPlayers)
    # to pass info to HTML, need a dictionary
    context = {
        'allThePlayers': allPlayers
    }

    return render(request, "index.html", context)


def createPlayer(request):
    print("in post request function")
    #REQ.POST REPRESENTS INFORMATION SUBMITTED FROM THE FORM ON A POST REQUEST
    errorsObject = Player.objects.playerValidator(request.POST)
    print(request.POST) 
    if len(errorsObject)>0:
        for key, value in errorsObject.items():
            messages.error(request, value)
        return redirect('/')
    #create a player using the info from form
    newPlayer = Player.objects.create(firstname = request.POST['fname'], lastname = request.POST['lname'] , team = request.POST['team'])
    print(newPlayer)
    return redirect("/")


def showPlayer(request, idPlayer):
    print("in showPlayer")
    print(idPlayer)
    # ClassName.objects.get(id=1) - gets the record in the table with the specified id
    playerToShow = Player.objects.get(id = idPlayer)
    print(playerToShow)
    specificFans = Fan.objects.exclude(favPlayers= playerToShow)
    print("printing onlyfans ->", specificFans)

    # ClassName.objects.exclude(field1="value for field1", etc.) - gets any records not matching the query provided
    context = {
        'playaPlaya': playerToShow,
        'allFans': Fan.objects.all(),
        'specificFans': specificFans
    }

    return render(request, "player.html", context)

def addFanToPlayer(request, idPlayer):
    # 2 ways to get the players id: route paramater (idPlayer) or from hidden input in the form (request.POST)
    #the id of Fan selected comes from the select dropdown option in request.POST
    print("******")
    print(request.POST)
    print("******")
    this_fan = Fan.objects.get(id=request.POST['faninfo'])
    this_player = Player.objects.get(id = idPlayer) #using the route parameter variable
    # this_player = Player.objects.get(id = request.POST['playerinfo'])
    print(this_fan.firstname)
    print(this_player.firstname)
    #2 ways to make the many to many join

    # this_fan.favPlayers.add(this_player) 
    this_player.fans.add(this_fan)
    
    return redirect(f"/players/{idPlayer}")


def deletePlayer(request, idPlayer):
    # c = ClassName.objects.get(id=1)
    # c.delete()
    p = Player.objects.get(id= idPlayer)
    p.delete()
    return redirect("/")

def editPlayer(request, idPlayer):
    # print(idPlayer)
    context = {
        'playerToEdit': Player.objects.get(id=idPlayer)
    }

    return render(request, "edit.html", context)

def updatePlayer(request, idPlayer):
    print(request.POST)
    p = Player.objects.get(id = idPlayer)
    p.firstname = request.POST['fname']
    p.lastname = request.POST['lname']
    p.team = request.POST['team']
    p.save()
    return redirect("/")
