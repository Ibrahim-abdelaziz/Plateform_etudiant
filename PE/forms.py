from . import models
from django import forms


class AdherentForm(forms.ModelForm):
    class Meta:
        model = models.Adherent
        fields = ['nom', 'prenom', 'cne', 'theme']


class ChallpfeForm(forms.ModelForm):
    class Meta:
        model = models.Etu_estchalleng
        fields = ['nom', 'prenom', 'cne', 'sujet', 'filiere', 'rapport_pfe', 'nom_ancadrant']


class PfeForm(forms.ModelForm):
    class Meta:
        model = models.Pfe
        fields = ('sujet', 'nom', 'prenom', 'filiere', 'nom_ancadrant', 'pdf')


class LaureaForm(forms.ModelForm):
    class Meta:
        model = models.Laurea
        fields = ('nom', 'prenom', 'filiere', 'email', 'annee_d_diplome', 'image', 'telefone', 'cin', 'paye', 'etablissement', 'Societe', 'poste')