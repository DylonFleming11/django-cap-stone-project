from django.urls import path
from .views.player_views import Players, PlayerDetail
from .views.gamelog_views import GameLogs, GameLogDetail
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('gamelogs/', GameLogs.as_view(), name='gamelogs'),
    path('gamelogs/<int:pk>/', GameLogDetail.as_view(), name='gamelogdetail'),
    path('players/', Players.as_view(), name='players'),
    path('players/<int:pk>/', PlayerDetail.as_view(), name='player_detail'),
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
