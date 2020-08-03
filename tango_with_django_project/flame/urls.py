from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('about/',views.about, name = 'about'),
    path('<int:deal_id>/', views.deal, name = 'deals'),
    path('<int:deal_id>/detail/', views.details, name = 'detail'),
    path('store/<int:store_id>/', views.store, name = 'stores'),
    path('testview',views.testview, name = 'test')
]

