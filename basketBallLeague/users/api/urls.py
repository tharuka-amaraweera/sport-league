from django.urls import path, include
from users.api.views import PlayerList, PlayerPersonalDetail, FindnintyPercentilePlayers

urlpatterns = [
    path('list/', PlayerList.as_view(), name='player_list'),
    path('personal-detail-list/<int:pk>', PlayerPersonalDetail.as_view(),
         name='player_personal_detail_list'),
    path('percentile/', FindnintyPercentilePlayers.as_view(), name='percentile'),
]
