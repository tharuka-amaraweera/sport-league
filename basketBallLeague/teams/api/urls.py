from django.urls import path, include
from teams.api.views import TeamList, TeamDetail, TeamOrderedList

urlpatterns = [
    path('list/', TeamList.as_view(), name='team_list'),
    path('list/<int:pk>', TeamDetail.as_view(), name='team_list'),
    path('ordered-list/', TeamOrderedList.as_view(), name='team_ordered_list'),
]
