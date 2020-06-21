from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('about/',views.about, name = 'about'),
    path('<int:deal_id>/', views.deal, name = 'deal'),
    path('<int:deal_id>/detail/', views.details, name = 'detail')
]

