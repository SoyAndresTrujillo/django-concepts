from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Car, Profile


# Create your views here.
def my_view(request):
    car_list = Car.objects.all()
    context = {"car_list": car_list}
    return render(request, "my_first_app/car_list.html", context)


# the class never returns anything, it only passes the context to the template as view
class CarListView(TemplateView):
    # the template name is the name of the template file in the templates folder for use into html
    template_name = "my_first_app/car_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car_list"] = Car.objects.all()
        return context


def profile_view(request, id):
    profile = Profile.objects.get(author_id=id)
    return HttpResponse(
        f"Hello, this is the profile of {profile.author.first_name}, {profile.biography} and website is {profile.website}"
    )


def my_test_view(request, *args, **kwargs):
    # tupla ()
    print(args)
    # dictionary {}
    print(kwargs)
    return HttpResponse("Hello, World!, this is my first list")
