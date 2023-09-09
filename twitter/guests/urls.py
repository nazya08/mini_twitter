from django.urls import path
from .views import guest_list, guest_detail


urlpatterns = [
    path('', guest_list, name="guest_list"),
    path('<str:guest_id>', guest_detail, name="guest_detail")
]
