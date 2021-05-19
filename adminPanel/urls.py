from django.urls import path
from .import views
#from home.views import *



urlpatterns = [
    path('',views.admin),
    path('dashboard', views.dashboard),
    path('logout',views.logout),
    path('createCompetition', views.createCompetition),
    path('saveCompetition', views.saveCompetition),
    path('competition', views.showCompetition),
    path('showusers', views.showUsers),
    path('saveusers', views.saveUsers),
    path('addusers', views.addUsers),
    path('tickets', views.showTickets),
    path('draw', views.draw),
    path('winners', views.winners),
    path('editCompetition/<int:id>',views.editCompetition),
    path('editUser/<int:id>',views.editUser),
    path('updateCompetition/<int:id>',views.updateCompetition),
    path('updateUser/<int:id>',views.updateUser),
    path('deleteCompetition/<int:id>',views.deleteCompetition)

]
