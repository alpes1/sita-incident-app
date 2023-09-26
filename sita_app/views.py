from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login 
from django.http import HttpResponse
from sita_app.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
from .models import *
from .form import TicketForm,SiteForm,UserForm
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Count
from datetime import date
import calendar

def administrateur(request):
    return render(request, 'administrateur.html')

def help_desk(request):
    return render(request, 'help_desk.html')

def consulteur (request):
    return render(request, 'consulteur.html')

def home(request):
    error=''
    if request.method == "POST":
        username=request.POST['username']
        password =request.POST['password']
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            print(f"Authenticated user: {user.username}")
            if user.is_administrateur:
                return redirect('administrateur')
            elif user.is_help_desk:
                return redirect('help_desk')
            else :
                return redirect('consulteur')
        else : 
            error ='password or username incorrect'
    return render(request,'login.html',{'error':error})

def register(request):
    form = UserForm(request.POST)
    if request.method == "POST":
        
        form =UserForm (data = request.POST )
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request , 'register.html',{'form':form})


def updateShort(request):
    if request.method == 'POST':
        tick = Ticket.objects.get(id_ticket=request.POST.get('id'))
        tick.etat = request.POST.get('action')
        if tick.etat == 'f' : 
            tick.probleme   = request.POST.get('probleme')
            tick.solution   = request.POST.get('solution')
            tick.closed_at  = timezone.now()
        
        tick.save()
    return JsonResponse({'status':200})
    

def creationticket (request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/acceuil')  # Use the correct URL name here
        else : 
            form_errors = form.errors.as_text()
            return HttpResponse(form_errors, status=400)
    else:
        form = TicketForm()
    context = {'form': form ,'title': 'Creer un ticket'}
    return render(request, 'creationticket.html', context)
    

def gestioncomposants(request):
    return render(request,'gestioncomposants.html')

def acceuil(request):
    nbr_ouvert=Ticket.objects.filter(etat='o').count()
    nbr_ferme=Ticket.objects.filter(etat='f').count()
    nbr_annule=Ticket.objects.filter(etat='a').count()

    problemes = Ticket.objects.filter(etat='f').values('probleme').annotate(nbr=Count('probleme'))

    months = []

    for i in range(1,13) :
        current_year = timezone.now().year

        _, last_day = calendar.monthrange(current_year, i)
        start_date = date(current_year, i, 1)  # Replace with your desired start date
        end_date = date(current_year, i, last_day)  # Replace with your desired end date

        months.append(
            Ticket.objects.filter(created_at__gte=start_date, created_at__lte=end_date).count()
        )


    return render(request,'acceuil.html',{
        'nbr_ouvert': nbr_ouvert,
        'nbr_annule': nbr_annule,
        'nbr_ferme' : nbr_ferme ,
        'months'    : months ,
        'problemes' : problemes
    })

def gererticket(request):
    Tickets = Ticket.objects.order_by('-created_at')
    return render(request,'gererticket.html',{'Tickets':Tickets})






def add_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/acceuil')  # Use the correct URL name here
    else:
        form = TicketForm()
    context = {'form': form}
    return render(request ,'gestioncomposants.html',context)

def updateTicket(request, pk ):
    Ticket_instance=Ticket.objects.get(id_ticket=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=Ticket_instance)
        if form.is_valid():
            # Save the updated form data
            form.save()
            # Redirect to a success page or return a JSON response, etc.
            return HttpResponse('Ticket updated successfully')
        else :
            return HttpResponse('There is an error in fields')
    else:
        # Initialize the form with the instance data
        form = TicketForm(instance=Ticket_instance)
        context = {'form': form,'title': 'Modifier un ticket'}
        return render(request ,'creationticket.html',context)