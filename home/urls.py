from django.urls import path
from .import views




urlpatterns = [
    path('', views.index, name='home-index'),
    path('login', views.login, name='home-login'),
    path('how', views.how_to, name='home-how_to'),
    path('ticket', views.ticket, name='home-ticket'),
    path('register', views.register, name='home-register'),
    path('winners', views.winners, name='home-winners'),
    path('draws',views.draws,name="home-draw"),
    path('competitions',views.competitions,name="home-competition"),
    path('logout',views.logout,name='logout'),
    path('<slug:slug>/',views.PostDetail.as_view(),name='PostDetail'),
    #cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

 
]
