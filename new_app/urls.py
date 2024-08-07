from django.urls import path

from new_app import views

urlpatterns = [
    path("home",views.home,name="home"),
    path('',views.index,name="index"),
    path('dash',views.dash,name="dash"),
    path('submit', views.submit,name="submit"),
    path('Furniture_view',views.Furniture_view,name="Furniture_view"),
    path('Furniture_delete/<int:id>/',views.Furniture_delete,name="Furniture_delete"),
    path('Furniture_update/<int:id>/',views.Furniture_update, name="Furniture_update")
]
