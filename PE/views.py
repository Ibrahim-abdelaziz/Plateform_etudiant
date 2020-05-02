from django.shortcuts import render, redirect
from .forms import PfeForm, LaureaForm
from PE.forms import AdherentForm, ChallpfeForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from forumestc.models import Departement
from tablib import Dataset
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from .models import Pfe


def index(request):
    titre = 'EST CASABLANCA'
    actualiteslist1 = actualité.objects.all().order_by('date').reverse()
    actualiteslist2 = actualité.objects.filter(id__gt=0).order_by('date')
    annonceslist1 = annonce.objects.all().order_by('date').reverse()
    return render(request, 'PE/index.html',
                  {'titre': titre, 'actualiteslist1': actualiteslist1, 'actualiteslist2': actualiteslist2,
                   'annonceslist1': annonceslist1})


def sinscrire1(request):
    return render(request, 'PE/sincrire.html')


def indexx(request):
    context = {}
    if request.method == "POST":
        if 'username' in request.POST:
            username = request.POST['username']
        else:
            username = False

        if 'password' in request.POST:
            password = request.POST['password']
        else:
            password = False

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context['error'] = "Provide valid credentialble"
            return render(request, 'PE/login.html', context)

    else:
        return render(request, 'PE/login.html', context)


def Etu_exist(request):
    if request.method == 'POST':
        form = PE.forms.etudiantF(request.POST)
        if form.is_valid():
            for e in etudiant.objects.all():
                if e.cne == form.cne:
                    return HttpResponse(form.cne)
    else:
        return render(request, 'PE/verifier_cne.html')


def success(request):
    return render(request, 'PE/success.html')


def motdudirecteur(request):
    titre = 'Mot Du Directeur'
    return render(request, 'PE/motdudirecteur.html', {'titre': titre})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('forumestc:forum_home')
    else:
        form = UserCreationForm()
    return render(request, 'forumestc/include/sign_up.html', {'form': form})


# ***************************************************************************
def activ_art(request):
    context = ''
    titre = 'activites'
    theme_arts = theme_art.objects.all()
    if request.method == "POST":
        form = AdherentForm(request.POST)
        if form.is_valid():

            for e1 in Adherent.objects.all():
                if e1.cne == form.cleaned_data['cne']:
                    if e1.theme == form.cleaned_data['theme']:
                        context = 'vous ete deja inscrit dans ce theme choisir un autre theme '
                        return render(request, 'PE/art_choix.html',
                                      {'form': form, 'titre': titre, 'theme_arts': theme_arts, 'context': context})

            for e in etudiant.objects.all():
                if e.cne == form.cleaned_data['cne']:
                    form.save()
                    adherent = Adherent()
                    adherent.nom = form.cleaned_data['nom']
                    adherent.prenom = form.cleaned_data['prenom']
                    adherent.cne = form.cleaned_data['cne']
                    adherent.theme = form.cleaned_data['theme']
                    request.session['adherent'] = form.cleaned_data
                    return render(request, 'PE/confirmer.html',
                                  {'adherent': adherent, 'titre': titre, 'theme_arts': theme_arts,
                                   'context': 'vous etes inscrit, si vous voulez vous pouvez s inscrire dans un voveau theme  '})
            return render(request, 'PE/art_choix.html',
                          {'form': form, 'titre': titre, 'theme_arts': theme_arts, 'context': 'ce cne n existe pas '})

    else:
        form = AdherentForm()

        return render(request, 'PE/art_choix.html', {'form': form, 'titre': titre, 'theme_arts': theme_arts})

    return render(request, 'PE/art_choix.html', {'form': form, 'titre': titre, 'theme_arts': theme_arts})


def confirmation(request):
    data = request.session.get('adherent')
    adherent = Adherent()
    adherent.nom = data['nom']
    adherent.prenom = data['prenom']
    adherent.cne = data['cne']
    adherent.theme = data['theme']
    adherent.save()
    insc = activ_art(adherent=adherent)
    insc.save()
    return render(request, 'PE/Succes.html', {'adherent': request.session.get('adherent')})


# *************************************************************


def inscription(request):
    if request.method == "POST":
        form = ChallpfeForm(request.POST)
        if form.is_valid():
            for e1 in Etu_estchalleng.objects.all():
                if e1.cne == form.cleaned_data['cne']:
                    context = 'vous ete deja inscrit  '
                    return render(request, 'PE/concourpfe.html', {'form': form, 'contextpfe': context})

            for e in etudiant.objects.all():
                if e.cne == form.cleaned_data['cne']:
                    form.save()
                    condidat = Etu_estchalleng()
                    condidat.nom = form.cleaned_data['nom']
                    condidat.prenom = form.cleaned_data['prenom']
                    condidat.cne = form.cleaned_data['cne']
                    condidat.sujet = form.cleaned_data['sujet']
                    condidat.filiere = form.cleaned_data['filiere']
                    condidat.nom_ancadrant = form.cleaned_data['nom_ancadrant']
                    condidat.rapport_pfe = form.cleaned_data['rapport_pfe']
                    request.session['condidat'] = form.cleaned_data
                    context = 'test existance d etudiant dans est casa'
                    return render(request, 'PE/confirmation2.html',
                                  {'condidat': condidat, 'form': form, 'contextpfe': context})
            return render(request, 'PE/concourpfe.html',
                          {'form': form, 'contextpfe': 'ce cne n existe pas '})

    else:
        form = ChallpfeForm()

        return render(request, 'PE/concourpfe.html', {'form': form, 'contextpfe': 'test1'})

    return render(request, 'PE/concourpfe.html', {'form': form, 'contextpfe': 'test2'})


def confirmation2(request):
    data = request.session.get('condidat')
    condidat = Etu_estchalleng()
    condidat.nom = data['nom']
    condidat.prenom = data['prenom']
    condidat.cne = data['cne']
    condidat.sujet = data['sujet']
    condidat.filiere = data['filiere']
    condidat.nom_ancadrant = data['nom_ancadrant']
    condidat.rapport_pfe = data['rapport_pfe']
    condidat.save()
    insc2 = concourpfe(condidat=condidat)
    insc2.save()
    return render(request, 'PE/Succes.html', {'condidat': request.session.get('condidat')})


# *************************************view evenements  ************************

def evenements(request):
    titre = 'Evenements'
    evenements = evenement.objects.all().order_by('date').reverse()
    return render(request, 'PE/evenements.html', {'titre': titre, 'evenements': evenements})


def addevent(request):
    titre = 'Evenements'
    if request.method == 'POST':
        titre = request.POST.get('titre')
        lieu = request.POST.get('lieu')
        Description = request.POST.get('description')
        club_recup = request.POST.get('club')
        club_id = club.objects.get(club=club_recup).id
        print(club_recup)
        print(club_id)
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        evenement.objects.create(titre=titre, lieu=lieu, description=Description, img=filename, club=club(club_id))
        return redirect('plateformetudiant:evenements')
    else:
        return redirect('plateformetudiant:evenements')
    return redirect('plateformetudiant:evenements')


def test(request):
    titre = 'test'
    return render(request, 'PE/test.html', {'titre': titre})


def vote(request):
    candidats = candidat_president.objects.all()
    titre = "Les elections de L'ecole"
    return render(request, 'PE/vote.html', {'titre': titre, 'candidats': candidats})


def vote_candidat(request, pk):
    candidat = candidat_president.objects.get(id=pk)
    Departements = Departement.objects.all()
    titre = candidat.candidat_allname
    return render(request, 'PE/voteprofile.html', {'titre': titre, 'candidat': candidat, 'Departements': Departements})


def addvote(request, pk):
    if request.method == 'POST':
        name = request.POST.get('electeur_allname')
        cin = request.POST.get('electeur_cin')
        candidat = candidat_president.objects.get(id=pk).id
        if etudiant.objects.filter(CIN=cin).exists():
            electeur.objects.create(electeur_allname=name, electeur_cin=cin, candidat=candidat_president(candidat))
            upvote = candidat_president.objects.get(id=pk).candidat_totalvote
            upvote = upvote + 1
            candidat_president.objects.filter(id=candidat).update(candidat_totalvote=upvote)
        return redirect('plateformetudiant:vote')
    else:
        return redirect('plateformetudiant:vote')


def admineventlogin(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('plateformetudiant:adminevent')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('plateformetudiant:adminevent')
    else:
        form = AuthenticationForm()
    return render(request, 'PE/admineventlogin.html', {'form': form})


def adminevent(request):
    if request.user.is_superuser or request.user.is_staff:
        clubs = club.objects.all()
        return render(request, 'PE/adminevent.html', {'clubs': clubs})
    else:
        return redirect('plateformetudiant:evenements')


# *************************adminpfe*********************


def adminpfe(request):
    condidatpfe = Etu_estchalleng.objects.all()
    return render(request, 'PE/adminpfe.html', {'condidatpfe': condidatpfe})


def Laureat_list(request):
    laureats = Laurea.objects.all()
    return render(request, 'PE/laurea_lst.html', {'laureats': laureats})


def Pfes_list(request):
    pfes = Pfe.objects.all()
    return render(request, 'PE/pfe_list.html', {'pfes': pfes})


def upload_pfe(request):
    if request.method == 'POST':
        form = PfeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plateformetudiant:upload_pfe')
    else:
        form = PfeForm()
    return render(request, 'PE/upload_pfe.html', {'form': form})


def Laurea_insc(request):
    if request.method == 'POST':
        form = LaureaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plateformetudiant:home')
    else:
        form = LaureaForm()
    return render(request, 'PE/adminact.html', {'form': form})


def loginpfe(request):
    user1 = 'admin_pfe'
    pass1 = 'admin_pfe'
    if request.method == 'POST':
        usern = request.POST.get('username')
        passw = request.POST.get('password')
        if user1 == usern and pass1 == passw:
            return redirect('plateformetudiant:Pfes_list')

    return render(request, 'PE/logamin.html')


def loginglob(request):
    user1 = 'admin'
    pass1 = 'admin'
    if request.method == 'POST':
        usern = request.POST.get('username')
        passw = request.POST.get('password')
        if user1 == usern and pass1 == passw:
            return redirect('plateformetudiant:adminglo')

    return render(request, 'PE/logiglo.html')

def loginlaueat(request):
    user1 = 'admin_laureat'
    pass1 = 'admin_laureat'
    if request.method == 'POST':
        usern = request.POST.get('username')
        passw = request.POST.get('password')
        if user1 == usern and pass1 == passw:
            return redirect('plateformetudiant:Laureat_list')

    return render(request, 'PE/loginadminlaureat.html')


def adminglo(request):
    events = evenement.objects.all()
    return render(request, 'PE/adminglo.html', {'events': events})


def admingloactu(request):
    actus = actualité.objects.all()
    return render(request, 'PE/adminactu.html', {'actus': actus})


def admingllaurea(request):
    laureas = Laurea.objects.all()
    if request.method == 'POST':
        filter = request.POST.get('filt')
        laurea = Laurea.objects.filter(filiere='DUT-GE2-RLI')
        return render(request, 'PE/adminglolaureat.html', {'laureas': laurea})
    return render(request, 'PE/adminglolaureat.html', {'laureas': laureas})


def adminannonce(request):
    annonces = annonce.objects.all()
    return render(request, 'PE/adminegloannonce.html', {'annonces': annonces})