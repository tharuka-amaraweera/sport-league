from django.urls import path, include
from users.api.views import PlayerList, PlayerDetail, PlayerScoreList, PlayerPersonalDetail, FindnintyPercentilePlayers

urlpatterns = [
    path('list/', PlayerList.as_view(), name='player_list'),
    path('list/<int:pk>', PlayerDetail.as_view(), name='player_detail'),
    path('averagescore-list/', PlayerScoreList.as_view(),
         name='player_averagescore_list'),
    path('personal-detail-list/<int:pk>', PlayerPersonalDetail.as_view(),
         name='player_personal_detail_list'),
    path('percentile/', FindnintyPercentilePlayers.as_view(), name='percentile'),
]
