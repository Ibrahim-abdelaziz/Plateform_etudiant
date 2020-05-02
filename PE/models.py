from django.db import models
from forumestc.models import *
from django.utils import timezone


# *** TABLE actualité ********************************************************************

class actualité(models.Model):
    titre = models.CharField(max_length=100)
    image = models.ImageField(default='default.png')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


# *** TABLE annonce ********************************************************************

class annonce(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


# *** TABLE club ********************************************************************
class club(models.Model):
    club = models.CharField(max_length=40)

    def __str__(self):
        return self.club


# *** table de theme_art***********************************

class theme_art(models.Model):
    titre = models.CharField(max_length=20)
    img = models.ImageField(default='default.png')
    description = models.TextField(default='defaultText')

    def __str__(self):
        return self.titre


# ****** table adherent*****************
GENRE_CHOICES = (
    ('Dance', 'dance'),
    ('Music', 'music'),
    ('Theatre', 'theatre'),
    ('Dessin', 'dessin')
)


class Adherent(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    cne = models.CharField(max_length=10)
    theme = models.CharField(max_length=100, choices=GENRE_CHOICES)

    def __str__(self):
        return self.nom


# ****************************************
class activ_art(models.Model):
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.adherent)


# *********class que je veux remplire des etudiant inscrit dans estchallenge **********
filiere_CHOICES1 = (
    ('DUT-FC2', 'DUT-FC2'),
    ('DUT-GE2-EEI', 'DUT-GE2-EEI'),
    ('DUT-GE2-EII', 'DUT-GE2-EII'),
    ('DUT-GE2-RLI', 'DUT-GE2-RLI'),
    ('DUT-GEA2', 'DUT-GEA2'),
    ('DUT-GI2', 'DUT-GI2'),
    ('DUT-GM2', 'DUT-GM2'),
    ('DUT-TC2', 'DUT-TC2'),
    ('DUT-GP2', 'DUT-GP2')
)


class Etu_estchalleng(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    cne = models.CharField(max_length=30)
    sujet = models.CharField(max_length=200)
    filiere = models.CharField(max_length=100, choices=filiere_CHOICES1)
    nom_ancadrant = models.CharField(max_length=30)
    rapport_pfe = models.FileField()

    def __str__(self):
        return self.sujet


class concourpfe(models.Model):
    adherent = models.ForeignKey(Etu_estchalleng, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.adherent)


# *** TABLE evenement ********************************************************************


class evenement(models.Model):
    titre = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    img = models.ImageField(default='default.png')
    lieu = models.CharField(max_length=50)
    club = models.ForeignKey(club, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(default='defaultText')

    def __str__(self):
        return self.titre


# *** TABLE elecetion ********************************************************************
class candidat_president(models.Model):
    candidat_allname = models.CharField(max_length=40)
    candidat_departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    candidat_totalvote = models.IntegerField(default=0)
    candidat_img = models.ImageField()

    def __str__(self):
        return self.candidat_allname


# *** TABLE electeur********************************************************************
class electeur(models.Model):
    electeur_allname = models.CharField(max_length=40)
    electeur_cin = models.CharField(max_length=50, unique=1)
    candidat = models.ForeignKey(candidat_president, on_delete=models.CASCADE)

    def __str__(self):
        return self.electeur_allname


# *** TABLE anonypme********************************************************************

class etudiant(models.Model):
    Code_apogee = models.CharField(max_length=8, default=0)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    CIN = models.CharField(max_length=10)
    Filiere = models.CharField(max_length=80, default=0)
    cne = models.CharField(max_length=10)
    # Les Champs Optionnel De Le Remplir
    # img = models.ImageField(default='can1.jpg')
    # email = models.CharField(max_length=10, default='email')
    # annedenaissance = models.DateField(default=now)
    complete = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


# *** TABLE anonypme********************************************************************

class etudianttest(models.Model):
    Code_apogee = models.CharField(max_length=8, default=0)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    CIN = models.CharField(max_length=10)
    Filiere = models.CharField(max_length=80, default=0)
    cne = models.CharField(max_length=10)
    # Les Champs Optionnel De Le Remplir
    # img = models.ImageField(default='can1.jpg')
    # email = models.CharField(max_length=10, default='email')
    # annedenaissance = models.DateField(default=now)
    complete = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


# *************************testBOOK***********************


filiere_CHOICES2 = (
    ('DUT-FC2', 'DUT-FC2'),
    ('DUT-GE2-EEI', 'DUT-GE2-EEI'),
    ('DUT-GE2-EII', 'DUT-GE2-EII'),
    ('DUT-GE2-RLI', 'DUT-GE2-RLI'),
    ('DUT-GEA2', 'DUT-GEA2'),
    ('DUT-GI2', 'DUT-GI2'),
    ('DUT-GM2', 'DUT-GM2'),
    ('DUT-TC2', 'DUT-TC2'),
    ('DUT-GP2', 'DUT-GP2')
)


class Pfe(models.Model):
    sujet = models.CharField(max_length=99)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    filiere = models.CharField(max_length=100, choices=filiere_CHOICES2)
    nom_ancadrant = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='Pfes/pdfs/')

    def __str__(self):
        return self.sujet


filiere_CHOICES3 = (
    ('DUT-FC2', 'DUT-FC2'),
    ('DUT-GE2-EEI', 'DUT-GE2-EEI'),
    ('DUT-GE2-EII', 'DUT-GE2-EII'),
    ('DUT-GE2-RLI', 'DUT-GE2-RLI'),
    ('DUT-GEA2', 'DUT-GEA2'),
    ('DUT-GI2', 'DUT-GI2'),
    ('DUT-GM2', 'DUT-GM2'),
    ('DUT-TC2', 'DUT-TC2'),
    ('DUT-GP2', 'DUT-GP2'),
    ('LP-GLAASRI', 'LP-GLAASRI'),
    ('LP-CFA', 'LP-CFA'),
    ('LP-GIL', 'LP-GIL'),
    ('LP-GLAASRI', 'LP-GLAASRI'),
    ('LP-LPMECA', 'LP-LPMECA'),
    ('LP-MECA', 'LP-MECA'),
    ('LP-MV', 'LP-MV'),
)

Anne_CHOICES = (

    ('1986', '1986'),
    ('1987', '1987'),
    ('1988', '1988'),
    ('1989', '1989'),
    ('1990', '1990'),
    ('1991', '1991'),
    ('1992', '1992'),
    ('1993', '1993'),
    ('1994', '1994'),
    ('1995', '1995'),
    ('1996', '1996'),
    ('1997', '1997'),
    ('1998', '1999'),
    ('1999', '1999'),
    ('2001', '2001'),
    ('2002', '2002'),
    ('2003', '2003'),
    ('2004', '2004'),
    ('2005', '2005'),
    ('2006', '2006'),
    ('2007', '2007'),
    ('2008', '2008'),
    ('2009', '2009'),
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025'),
    ('2026', '2026'),
    ('2027', '2027'),
    ('2028', '2028'),
    ('2029', '2029'),
    ('2030', '2030'),
    ('2031', '2031'),
    ('2032', '2032'),
    ('2033', '2033'),
    ('2034', '2034'),
    ('2035', '2035'),
    ('2036', '2036'),
    ('2037', '2037'),
    ('2038', '2038'),
    ('2039', '2039'),
)


class Laurea(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    filiere = models.CharField(max_length=60, choices=filiere_CHOICES3)
    email = models.EmailField()
    annee_d_diplome = models.CharField(max_length=60, choices=Anne_CHOICES)
    # image = models.ImageField()
    image =  models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    telefone = models.CharField(max_length=50)
    cin = models.CharField(max_length=20)
    paye = models.CharField(max_length=20)
    etablissement = models.CharField(default='Null', max_length=100)
    Societe = models.CharField(default='Null', max_length=100)
    poste = models.CharField(default='null', max_length=100)

    def __str__(self):
        return self.nom
