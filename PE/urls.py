from django.urls import path, include

from . import views

app_name = 'plateformetudiant'

urlpatterns = [
    path('', views.index, name='home'),
    path('pfe/', views.inscription, name='pfe'),
    path('log/', views.indexx),
    path('uploadpfe/', views.upload_pfe, name='upload_pfe'),
    path('pfes/', views.Pfes_list, name='Pfes_list'),
    path('authentificationpfe/', views.loginpfe, name='adminpfe2'),
    path('authentificationlaureat/', views.loginlaueat, name='adminlaurea'),

    path('authentificationglobt/', views.loginglob, name='loginglob'),

    path('adminglob/', views.adminglo, name='adminglo'),
    path('adminactus/', views.admingloactu, name='adminactus'),
    path('adminglolaureats/', views.admingllaurea, name='admingllaureat'),
    path('admingloannonce/', views.adminannonce, name='adminanc'),
    path('confpfe/', views.confirmation2, name='conpfe'),
    path('administrationpfe/', views.adminpfe, name='adminpfe'),
    path('', include('forumestc.urls'), name='forum_home'),
    path('motdudirecteur/', views.motdudirecteur, name='motdudirecteur'),
    path('evenements/', views.evenements, name='evenements'),
    path('test/', views.test, name='test'),
    path('vote/', views.vote, name='vote'),
    path('evenements/art/', views.activ_art, name='art'),
    path('confirmer/', views.confirmation, name='confir'),
    path('vote_candidat/<int:pk>', views.vote_candidat, name='vote_candidat'),
    path('addvote/<int:pk>', views.addvote, name='addvote'),
    path('admineventlogin/', views.admineventlogin, name='admineventlogin'),
    path('adminevent/', views.adminevent, name='adminevent'),
    path('addevent/', views.addevent, name='addevent'),
    path('sinscrire/', views.sinscrire1, name="sincrire"),
    path('laureat/', views.Laurea_insc, name='laurea'),
    path('success/', views.success, name='user_success'),
    path('Laureat_list/', views.Laureat_list, name='Laureat_list')
]
