from django.urls import path
from crudpapp import views

urlpatterns = [
   
    path('',views.home),
    path('display/',views.display),
    path('create/',views.add),
    path('create/insert/',views.insert),
    path('display/delete/<int:id>',views.delete),
    path('display/edit/<int:id>',views.edit),
    path('display/edit/update/',views.update),

]

