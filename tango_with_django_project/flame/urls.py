from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('about/',views.about, name = 'about'),
    path('<int:question_id>/', views.deals, name = 'detail')
]

