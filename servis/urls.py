from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('automobiliai/',views.automobiliai,name="automobiliai"),
    path('automobiliai/<int:automobilis_id>',views.automobilis,name="automobilis"),
    path('uzsakymai/',views.UzsakymasListView.as_view(),name="uzsakymai"),
    path('uzsakymai/<int:pk>',views.UzsakymasDetailView.as_view(),name="uzsakymas"),
    path('apiemus/',views.apiemus,name="apiemus"),
    path('search/', views.search, name='search'),
    path('myorders/',views.UzsStatusasPagalVartotoja.as_view(),name="mano-uzsakymai"),
    path('myorders/<int:pk>', views.UzsakymasByUserDetailView.as_view(), name='mano-uzsakymas'),
    path('myorders/new', views.UzsByUserCreateView.as_view(), name='my-order-new'),
    path('myorders/<int:pk>/update', views.UzsByUserUpdateView.as_view(), name='my-order-update'),
    path('myorders/<int:pk>/delete', views.UzsByUserDeleteView.as_view(), name='my-order-delete'),
    path('register/', views.register, name='register'),
    path('profilis/',views.profilis,name="profilis")
]