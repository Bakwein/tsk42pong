from django.contrib import admin
from .models import Gamers, Friends, Messages, Blocklist, GameHistory , Tournament, TournamentMatch , Notifications, Rps

admin.site.register(Gamers)
admin.site.register(Friends)
admin.site.register(Messages)
admin.site.register(Blocklist)
admin.site.register(GameHistory)
admin.site.register(Tournament)
admin.site.register(TournamentMatch)
admin.site.register(Notifications)
admin.site.register(Rps)

