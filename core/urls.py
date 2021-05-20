from django.urls import path
from rooms import views as room_views

app_name = "core"

urlpatterns = [
    # path는 2번째 인자로 함수를 받는다. => HomeView에서 함수를 가져와야함
    path("", room_views.HomeView.as_view(), name="home"),
]
