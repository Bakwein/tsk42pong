from django.db import models

# Create your models here.
class Gamers(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    profile_picture = models.TextField()
    date = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Friends(models.Model):
    id=models.AutoField(primary_key=True)
    following=models.CharField(max_length=100)
    follower=models.CharField(max_length=100)
    profile_picture=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return f"Following: {self.following}, Follower: {self.follower}"

class Messages(models.Model):
    id=models.AutoField(primary_key=True)
    sender=models.CharField(max_length=100)
    receiver=models.CharField(max_length=100)
    message=models.TextField()
    name=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return f"Sender: {self.sender}, Receiver: {self.receiver}"

class Blocklist(models.Model):
    id=models.AutoField(primary_key=True)
    blocker=models.CharField(max_length=100)
    blocked=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return f"Blocker: {self.blocker}, Blocked: {self.blocked}"

class GameHistory(models.Model):
    id=models.AutoField(primary_key=True)
    user1=models.CharField(max_length=100)
    user2=models.CharField(max_length=100)
    user1score=models.CharField(max_length=100)
    user2score=models.CharField(max_length=100)
    game=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return f"Winner: {self.winner}, Loser: {self.loser}, Type: {self.type}"

class Tournament(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    players=models.CharField(max_length=1500)
    victory=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return f"Name: {self.name}, Victory: {self.victory}"

class TournamentMatch(models.Model):
    id=models.AutoField(primary_key=True)
    tournament=models.CharField(max_length=100)
    player1=models.CharField(max_length=100)
    player2=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    score=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return f"Player1: {self.player1}, Player2: {self.player2}, Status: {self.status}"

class Notifications(models.Model):
    id=models.AutoField(primary_key=True)
    receiver=models.CharField(max_length=100)
    message=models.TextField()
    status=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return f"Sender: {self.sender}, Receiver: {self.receiver}"

class Rps(models.Model):
    id = models.AutoField(primary_key=True)
    user1 = models.CharField(max_length=100)
    user2 = models.CharField(max_length=100)
    user1_attack = models.CharField(max_length=100)
    user2_attack = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"User1: {self.user1}, User2: {self.user2}, Status: {self.status}"
