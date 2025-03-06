from django.shortcuts import render, redirect
from . models import mnb_deviza, mnb_name, Tranzakciok
import requests
import datetime

from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import  MnbSerializer, MnbNameSerializer

from . import forms
from django.contrib.auth import login, logout, authenticate  # add to imports
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from . import mnb_deviza_download

#-------------------------------------------------------------------------------------------------------------------------------------

#Ez a metódus végzi a bejelentkezett felhasználó váltását és a home.html renderelését.
@login_required
def home(request):
    
    latest_date = mnb_deviza.objects.latest('date').date # Az mnb_deviza táblában található legfrisseb dátumok lekérése
    latest_rates = mnb_deviza.objects.filter(date=latest_date) # Lista, ami a dátum szerinti legfrissebb adatokat (Árfolyam, valutanem) tartalmazza 
    
    if latest_date==datetime.date.today(): #a valuta adatbázis automatikus frissítése (még nem tesztelt)
        pass
    else:
        restMNBRefresh(request)


    rates_dict = {rate.currency: rate.value for rate in latest_rates}

    if request.method == 'POST':
        amount = round(float(request.POST['amount'])) #Váltandó összeg, kerekítve
        from_currency = request.POST['from_currency'] #Erről a pénznemről váltunk. Ez a váltási költség pénzneme is.
        to_currency = request.POST['to_currency'] #Ezze a pénznemr váltunk.
       

        from_rate = rates_dict[from_currency]
        to_rate = rates_dict[to_currency]

        converted_amount = round(float(amount * (from_rate / to_rate))) #A váltott összeg kerekítve.

        kuldeskoltsege=0 #Kiszámolja a küldés költségét a váltandó összegből ami a váltandó összeg fél százaléka, pénzneme.
        if amount <= 100:
            kuldeskoltsege=round(float(amount* 0.05)) #Ha a váltanó pénz kevesebb mint 100 akkor a küldés költsége a váltandó pénz 5%-a.
        else:
            kuldeskoltsege=round(float(amount* 0.025)) #Ha a váltandó pénz több mint 1000 akkor a küldés összege a váltandó pénz 2,5°%-a.
         
        osszeslevonas=round(float(amount+kuldeskoltsege)) #Az az összeg amit a küldő fél átvált plusz küldés ára.
        
        return render(request, 'home.html', {
            'osszeslevonas': osszeslevonas,
            'kuldeskoltsege': kuldeskoltsege,
            'converted_amount': converted_amount,
            'from_currency': from_currency,
            'to_currency': to_currency,
            'amount': amount,
            'currencies': rates_dict.keys()
        })
    else:
        return render(request, 'home.html', {'currencies': rates_dict.keys()})

#Az küldés gomb megnyomása után ez a metódus felel az adatok lementéséért a Tranzakciók adatbázisba.
@login_required
def save_data(request):
    if request.method == 'POST':
        felhasznalonev = request.user.username
        kedvezmenyezett = request.POST['kedvezmenyezett'] #kedvezményezett neve
        szamlaszamkedv = request.POST['szamlaszamkedv'] #kedvezményezett számlaszáma
        kuldendoosszeg = request.POST['converted_amount']
        kuldendopm = request.POST['to_currency'] #küldendő pénznem
        megjegyzes = request.POST['megjegyzes']
        
        tranzakcio = Tranzakciok(
            felhasznalonev=felhasznalonev,
            kedvezmenyezettneve=kedvezmenyezett,
            kedvezmenyezettszamlaszam=szamlaszamkedv,
            elkuldottosszeg=kuldendoosszeg,
            elkuldottdevizanem=kuldendopm,
            megjegyzesek=megjegyzes
        )
        tranzakcio.save()
        return redirect('home')
    return redirect('home') #visszairányítás a home oldalra.


#Ez a metódus felel az elküldött adatok megjelenítéséért.
@login_required
def tranzakciok(request):
    felhasznalo=request.user.username #az épp bejelentkezett felhasználó neve
    tranzakciok = Tranzakciok.objects.filter(felhasznalonev=felhasznalo).order_by("-kuldesdatuma") # A tranzakciós adatok, szűrve a felhasználó neve alapján 
    return render(request, 'tranzakciok.html', {"adatok": tranzakciok})


#-------------------------------------------------------------------------------------------------------------------------------------

@api_view(['GET'])
# frontend lekérdezése: lekérdezi az előző 30nap adatait
# ez a grafikonokhoz kell
def restMNBValuta(request):
    if request.method == "GET":
        allData = mnb_deviza.objects.filter(date__range=(datetime.datetime.now()-datetime.timedelta(days=30), datetime.datetime.now() ))
        serialized = MnbSerializer(allData, many=True) 
        return Response(serialized.data)


@api_view(['GET'])
# frontend lekérdezése: az utolsó napi adatokat 
# ez a számolásokhoz, a kalkulációhoz kell
def restMNBValutaLast(request):
    if request.method == "GET":
        #megkeresi az utoldó nap dátumát
        last = mnb_deviza.objects.order_by("-date")[:1].values("date")
        #betölti az utolsó nap adatait
        allData = mnb_deviza.objects.filter(date = last )
        serialized = MnbSerializer(allData, many=True) 
        return Response(serialized.data)


@api_view(['GET'])
# frontend lekérdezése: az MNB által nyílvántartott devizanevek
def restMNBName(request):
    if request.method == "GET":
        allData = mnb_name.objects.all()
        serialized = MnbNameSerializer(allData, many=True) 
        return Response(serialized.data)


@api_view(['GET'])
# frontend lekérdezése: ez meghívja MNB frissítését 
# visszetér a bejelentkezési oldallal
def restMNBRefresh(request):
    if request.method == "GET":
        mnb_deviza_download.nmbLetolt()
        return redirect('login')
    
#-------------------------------------------------------------------------------------------------------------------------------------

#FELHASZNÁLÓ KEZELÉSHEZ SZÜKSÉGES METÓDUSOK:

def logout_user(request): #kijelentkezés
    logout(request)
    return redirect('login')

def login_page(request):#bejelentkezés
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Bejelentkezés sikertelen'
    return render(request, 'login.html', context={'form': form, 'message': message})

def signup_page(request): #regisztráció, illetve az épp regisztrált felhasználó automatikus bejelentkezése
    form = forms.SignupForm()
    hibauzenet=""
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request, user)
            return redirect('home')
        else:
            hibauzenet="Regisztráció sikertelen"
    return render(request, 'signup.html', context={'form': form, 'hibauzenet':hibauzenet})

@login_required # éppen bejelentkezett felhasználó törlése (superusert nem lehet így törölni)
def delete_user(request):
    user=request.user
    if user.is_superuser:
        return redirect('tranzakciok')
    else:
        Tranzakciok.objects.filter(felhasznalonev=user).delete() #Törli az adott felhasználó eddigi tranzakcióiz is az adatbázisból.
        User.delete(user)
    return redirect('login')