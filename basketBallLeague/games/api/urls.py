from django.urls import path, include
from games.api.views import GameOrderedList

urlpatterns = [
    path('ordered-list/', GameOrderedList.as_view(), name='game_list')
]
