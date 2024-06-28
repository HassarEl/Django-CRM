from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('produit/', views.produit, name='produit'),
    path('produit/ajou_prod/', views.add_produit, name='add_produit'),
    path('categorie', views.categorie, name='categorie'),
    path('create_categorie', views.add_ctgr, name='crete_categorie'),
    path('commande/', views.commande, name='commande'),
    path('stock', views.stock, name="stock"),
    #path('test/', views.home, name='home')


]
