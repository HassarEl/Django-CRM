from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('produit/', views.produit, name='produit'),
    path('affectation/', views.affectation, name='affectation'),
    path('categorie', views.categorie, name='categorie'),
    path('create_categorie', views.add_ctgr, name='crete_categorie')


]
