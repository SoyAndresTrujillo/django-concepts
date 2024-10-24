from django.shortcuts import render
from django.http import HttpResponse

from .models import Car, Profile


# Create your views here.
def my_view(request):
    car_list = Car.objects.all()
    context = {"car_list": car_list}
    return render(request, "my_first_app/car_list.html", context)


def profile_view(request, id):
    profile = Profile.objects.get(author_id=id)
    return HttpResponse(
        f"Hello, this is the profile of {profile.author.first_name}, {profile.biography} and website is {profile.website}"
    )
