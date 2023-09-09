from django.shortcuts import render, get_object_or_404
from guests.models import Guest


def guest_list(request):
    guests = Guest.objects.all()
    context = {'guests': guests, 'title': 'List of users'}
    return render(request, 'guests/all_about_guests.html', context)


def guest_detail(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    context = {
        'guest': guest
    }
    return render(request, 'guests/guest_detail.html', context)
