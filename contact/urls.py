from django.urls import path

from contact import views

urlpatterns = [
    path('', views.ContactListAPIView.as_view()),
    path('contact/create/', views.ContactCreateAPIView.as_view()),
    path('contact-details/<int:pk>/', views.ContactDetailsAPIView.as_view()),
    path('contact/delete/<int:pk>', views.ContactDeleteAPIView.as_view())
]