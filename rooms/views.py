from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django.shortcuts import redirect, render
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"
    # page_kwarg = "potato"


class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room
    # pk_url_kwarg = "potato" => urls.py에서 <int:pk>에서 pk대신 tomato로 이름을 바꿈


""" def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", context={"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
        # return redirect(reverse("core:home"))
        # return redirect("/")
 """
