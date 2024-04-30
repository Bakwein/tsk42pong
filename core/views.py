from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Gamers, Friends, Messages, Blocklist, GameHistory, Tournament, TournamentMatch, Notifications, Rps
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
import random
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import requests
import os



# Create your views here.

def index(request):
    gmr=Gamers.objects.all()
    context={
        'gmr':gmr
    }
    return render(request, 'index.html', context)
def game(request):
    gmr=Gamers.objects.all()
    context={
        'gmr':gmr
    }
    return render(request, 'game.html', context)
def gameai(request):
    gmr=Gamers.objects.all()
    context={
        'gmr':gmr
    }
    return render(request, 'gameai.html', context)

def tictactoe(request):
    gmr=Gamers.objects.all()
    context={
        'gmr':gmr
    }
    return render(request, 'tictactoe.html', context)
def login(request):
    return render(request, 'login.html', {'client_id': settings.API_42_UID, 'redirect_uri': settings.API_42_REDIRECT_URI, 'response_type': settings.API_42_CODE , 'scope': settings.API_42_SCOPE})
def infotournaments(request):
    return render(request, 'infotournaments.html')
def home(request):
    return render(request, 'home.html')
def friend(request):
    return render(request, 'friend.html')
def rps(request):
    return render(request, 'rps.html')
def notifications(request):
    return render(request, 'notifications.html')
def tournament(request):
    return render(request, 'tournament.html')
def userprofile(request):
    return render(request, 'userProfile.html')
def registerkey(request):
    return render(request, 'registerkey.html')
def login_key(request):
    return render(request, 'login_key.html')
def profile(request):
    return render(request, 'profile.html')
def chats(request):
    return render(request, 'chats.html')
def main(request):
    return render(request, 'main.html')

def tester(request):
    gmr=Gamers.objects.all()
    context={
        'gmr':gmr
    }
    return render(request, 'tester.html', context)
def register(request):
    gmr=Gamers.objects.all()
    context={
        'gmr':gmr
    }
    return render(request, "register.html", context)
def addform(request):
    gmr=Gamers.objects.all()
    context={
        'gmr':gmr
    }
    return render(request, "addform.html", context)

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashpassword = make_password(password)
        profile_pictures = ['1.png', '2.png','3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png']
        selected_picture = random.choice(profile_pictures)
        gamer = Gamers.objects.create(name=name, email=email, password=hashpassword, profile_picture=selected_picture)
        return JsonResponse({'success': True})
    return render(request, 'create_user.html')

@csrf_exempt
def create_gamer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        existing_users = Gamers.objects.filter(Q(name=name) | Q(email=email))
        if existing_users.exists():
            return JsonResponse({'success': False, 'message': 'Bu isim veya email zaten kullanımda.'})
        random_number = random.randint(100000, 999999)
        subject = 'Kayıt Kodu'
        message = 'Doğrulama kodunuz ' + str(random_number)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        return JsonResponse({'success': True, 'registerkey': random_number, 'name': name, 'email': email, 'password': password})
    return render(request, 'create_gamer.html')

def get_gamers(request):
    if request.method == 'GET':
        user_email = request.META.get('HTTP_AUTHORIZATION', '').split('Bearer ')[1]
        gamer = Gamers.objects.get(email=user_email)
        kullanici = gamer.name
        email = gamer.email
        profile_picture = gamer.profile_picture
        return JsonResponse({'success': True, 'name': kullanici, 'email': email, 'profile_picture': profile_picture})
    return JsonResponse({'success': False, 'error': 'Geçersiz metod'})



def get_all_gamers(request):
    gamers = Gamers.objects.all()
    data = [{'name': gamer.name, 'email': gamer.email, 'profile': gamer.profile_picture} for gamer in gamers]
    return JsonResponse(data, safe=False)

@csrf_exempt
def getNotifications(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        gamers = Notifications.objects.filter(receiver=name)
    data = [{'message': gamer.message, 'date': gamer.date} for gamer in gamers]
    return JsonResponse(data, safe=False)

@csrf_exempt
def notificationControl(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        latest_notification = Notifications.objects.filter(receiver=name).order_by('-id').first()
        if latest_notification:
            if latest_notification.status == "0":
                return JsonResponse({'success': False})
            else:
                return JsonResponse({'success': True})
        return JsonResponse({'success': False})


@csrf_exempt
def get_all_friend(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        gamers = Friends.objects.filter(follower=email)
        data = [{'name': gamer.name, 'email': gamer.following, 'profile': gamer.profile_picture,} for gamer in gamers]
        return JsonResponse(data, safe=False)

@csrf_exempt
def get_user(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        gamers = Gamers.objects.filter(name=email)
        data = [{'name': gamer.name, 'email': gamer.email, 'profile': gamer.profile_picture,} for gamer in gamers]
        return JsonResponse(data, safe=False)
   
@csrf_exempt
def get_message(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        sender = request.POST.get('sender')
        gamers = Messages.objects.filter(Q(sender=email, receiver=sender) | Q(sender=sender, receiver=email))
        data = [{'sender': gamer.sender, 'receiver': gamer.receiver, 'message': gamer.message, 'name' : gamer.name} for gamer in gamers]
        return JsonResponse(data, safe=False)

def check_credentials(email, password):
    gamers = Gamers.objects.all()
    gamer = Gamers.objects.filter(email=email).first()
    if gamer is not None:
        gamer = Gamers.objects.filter(email=email).first()
        if check_password(password, gamer.password):
            refresh = RefreshToken.for_user(gamer)
            return str(refresh.access_token)
    return 0

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email is None or password is None:
            return JsonResponse({'success': False, 'error': 'E-posta veya şifre eksik'})
        token = check_credentials(email, password)
        if token:
            random_num_for_login = random.randint(100000, 999999)
            subject = 'Giriş Kodu'
            message = 'Doğrulama kodunuz ' + str(random_num_for_login)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            return JsonResponse({'success': True, 'token': token, 'email':email, 'random_num_for_login': random_num_for_login})
        else:
            return JsonResponse({'success': False, 'error': 'Geçersiz kimlik bilgileri'})
    return JsonResponse({'success': False, 'error': 'Geçersiz metod'}, status=405)

def addfriend(request):
    if request.method == 'POST':
        following = request.POST.get('following')
        follower = request.POST.get('follower')
        picture = request.POST.get('picture')
        name = request.POST.get('name')
        name2 = request.POST.get('name2')
        image = request.POST.get('image')
        existing_block = Friends.objects.filter(follower=follower, following=following).first()
        existing_block2 = Friends.objects.filter(follower=following, following=follower).first()
        if existing_block:
            existing_block.delete()
            existing_block2.delete()
            return JsonResponse({'success': True, 'message': 'Varolan blok silindi.'})
        Friends.objects.create(following=following, follower=follower, profile_picture=picture,name=name)
        Friends.objects.create(following=follower, follower=following, profile_picture=image,name=name2)
        return JsonResponse({'success': True})  # Başarılı bir şekilde eklendiğinde JSON yanıtı döndürün
    return render(request, '#')

def addmessage(request):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        receiver = request.POST.get('receiver')
        message = request.POST.get('message')
        name = request.POST.get('name')
        Messages.objects.create(sender=sender, receiver=receiver, message=message,name=name)
        return JsonResponse({'success': True})  # Başarılı bir şekilde eklendiğinde JSON yanıtı döndürün
    return render(request, '#')


@csrf_exempt
def rpsattack(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        attack = request.POST.get('attack')
        control = Rps.objects.filter(id = id ).first()
        if control.user1 == name:
            control.user1_attack = attack
            control.save()
            return JsonResponse({'success': True, 'message': 'Saldırı başarılı bir şekilde kaydedildi.'})
        elif control.user2 == name:
            control.user2_attack = attack
            control.save()
            return JsonResponse({'success': True, 'message': 'Saldırı başarılı bir şekilde kaydedildi.'})
    return render(request, '#')

@csrf_exempt
def rpscreate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        empty_user2_rps = Rps.objects.filter(user2 = "").first()
        if empty_user2_rps:
            if empty_user2_rps.user1 != name:
                empty_user2_rps.user2 = name
                empty_user2_rps.save()
                return JsonResponse({'success': True, 'id' : empty_user2_rps.id}) 
            else:
                empty_user2_rps.user2 = "EXIT"
                new_rps = Rps.objects.create(user1=name)
                new_rps_id = new_rps.id
                return JsonResponse({'success': True, 'id' : new_rps_id}) 
        else:
            new_rps = Rps.objects.create(user1=name)
            new_rps_id = new_rps.id
            return JsonResponse({'success': True, 'id' : new_rps_id}) 
    return render(request, '#')

@csrf_exempt
def rpscontrol(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        rps = Rps.objects.filter(id=id).first()
        if rps.user1 != "" and rps.user2 != "":
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    return render(request, '#')


@csrf_exempt
def rpscomplete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        rps = Rps.objects.filter(id=id).first()

    if rps.user1_attack == "rock" and rps.user2_attack == "scissors":
        return JsonResponse({'success': True, 'message': rps.user1 ,'user1': rps.user1 ,'user2': rps.user2, 'user1_attack': rps.user1_attack, 'user2_attack': rps.user2_attack})
    elif rps.user1_attack == "rock" and rps.user2_attack == "paper":
        return JsonResponse({'success': True, 'message': rps.user2 ,'user1': rps.user1 ,'user2': rps.user2, 'user1_attack': rps.user1_attack, 'user2_attack': rps.user2_attack})
    elif rps.user1_attack == "rock" and rps.user2_attack == "rock":
        return JsonResponse({'success': True, 'message': 'Berabere'  ,'user1': rps.user1 ,'user2': rps.user2, 'user1_attack': rps.user1_attack, 'user2_attack': rps.user2_attack})
    
    elif rps.user1_attack == "scissors" and rps.user2_attack == "rock":
        return JsonResponse({'success': True, 'message': rps.user2  ,'user1': rps.user1 ,'user2': rps.user2, 'user1_attack': rps.user1_attack, 'user2_attack': rps.user2_attack})
    elif rps.user1_attack == "scissors" and rps.user2_attack == "paper":
        return JsonResponse({'success': True, 'message': rps.user1  ,'user1': rps.user1 ,'user2': rps.user2, 'user1_attack': rps.user1_attack, 'user2_attack': rps.user2_attack})
    elif rps.user1_attack == "scissors" and rps.user2_attack == "scissors":
        return JsonResponse({'success': True, 'message': 'Berabere'  ,'user1': rps.user1 ,'user2': rps.user2, 'user1_attack': rps.user1_attack, 'user2_attack': rps.user2_attack})
    
    elif rps.user1_attack == "paper" and rps.user2_attack == "rock":
        return JsonResponse({'success': True, 'message': rps.user1  ,'user1': rps.user1 ,'user2': rps.user2, 'user1_attack': rps.user1_attack, 'user2_attack': rps.user2_attack})
    elif rps.user1_attack == "paper" and rps.user2_attack == "scissors":
        return JsonResponse({'success': True, 'message': rps.user2  ,'user1': rps.user1 ,'user2': rps.user2, 'user1_attack': rps.user1_attack, 'user2_attack': rps.user2_attack})
    elif rps.user1_attack == "paper" and rps.user2_attack == "paper":
        return JsonResponse({'success': True, 'message': 'Berabere'  ,'user1': rps.user1 ,'user2': rps.user2, 'user1_attack': rps.user1_attack, 'user2_attack': rps.user2_attack})
    
    elif rps.user1_attack == "" and rps.user2_attack == "":
        return JsonResponse({'success': False, 'message': 'Berabere'  ,'user1': rps.user1 ,'user2': rps.user2, 'user1_attack': rps.user1_attack, 'user2_attack': rps.user2_attack})
    elif rps.user1_attack == "":
        return JsonResponse({'success': False, 'message': rps.user2  ,'user1': rps.user1 ,'user2': rps.user2, 'user1_attack': rps.user1_attack, 'user2_attack': rps.user2_attack})
    elif rps.user2_attack == "":
        return JsonResponse({'success': False, 'message': rps.user1  ,'user1': rps.user1 ,'user2': rps.user2, 'user1_attack': rps.user1_attack, 'user2_attack': rps.user2_attack})
    
    return render(request, '#')



@csrf_exempt
def block_chat(request):
    if request.method == 'POST':
        blocker = request.POST.get('blocker')
        blocked = request.POST.get('blocked')
        existing_block = Blocklist.objects.filter(blocker=blocker, blocked=blocked).first()
        if existing_block:
            existing_block.delete()
            return JsonResponse({'success': True, 'message': 'Varolan blok silindi.'})
        Blocklist.objects.create(blocker=blocker, blocked=blocked)
        return JsonResponse({'success': True, 'message': 'Yeni blok eklendi.'})
    
    return render(request, '#')


@csrf_exempt
def block_controls(request):
    if request.method == 'POST':
        blocker = request.POST.get('blocker')
        blocked = request.POST.get('blocked')
        gamers = Blocklist.objects.filter(Q(blocker=blocker, blocked=blocked) | Q(blocker=blocked, blocked=blocker))
        if gamers:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    return render(request, '#')

@csrf_exempt
def postMatchHistory(request):
    if request.method == 'POST':
        user1 = request.POST.get('user1')
        user2 = request.POST.get('user2')
        user1score = request.POST.get('user1score')
        user2score = request.POST.get('user2score')
        game = request.POST.get('game')
        GameHistory.objects.create(user1=user1, user2=user2,user1score=user1score,user2score=user2score,game=game)
        return JsonResponse({'success': True, 'message': 'Yeni blok eklendi.'})
    return render(request, '#')

@csrf_exempt
def getGameHistory(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        gamers = GameHistory.objects.filter(Q(user1=email) | Q(user2=email))
        data = [{'user1': gamer.user1, 'user2': gamer.user2, 'user1score': gamer.user1score,'user2score': gamer.user2score,'game': gamer.game,'date': gamer.date} for gamer in gamers]
        return JsonResponse(data, safe=False)
   

@csrf_exempt
def showmatch(request):
   if request.method == 'POST':
        email = request.POST.get('name')
        gamers = TournamentMatch.objects.filter(tournament=email)
        data = [{'user1': gamer.player1, 'user2': gamer.player2, 'status': gamer.status, 'score' : gamer.score} for gamer in gamers]
        return JsonResponse(data, safe=False)
@csrf_exempt
def createTournament(request):
    if request.method == 'POST':
        name = request.POST.get('turnuvadi')
        victory = ""
        existing_tour = Tournament.objects.filter(Q(name=name))
        if existing_tour.exists():
            return JsonResponse({'success': False, 'message': 'Bu isim zaten kullanımda.'})
        Tournament.objects.create(name=name, victory=victory)
        return JsonResponse({'success': True, 'message': 'Yeni blok eklendi.'})
    return render(request, '#')

@csrf_exempt
def addplayer(request):
    if request.method == 'POST':
        player_name = request.POST.get('name')
        tournament_name = request.POST.get('tournamentname')
        tournament = get_object_or_404(Tournament, name=tournament_name)
        tour_players = tournament.players.split('#')
        players = tournament.players if tournament.players else ""
        if player_name not in tour_players:
            if players:
                players += f"#{player_name}"
            else:
                players = player_name
        else :
            return JsonResponse({'success': False, 'message': 'Bu oyuncu zaten ekli.'})
        tournament.players = players
        tournament.save()
        return JsonResponse({'success': True, 'message': 'Yeni oyuncu başarıyla eklendi.'})
    

@csrf_exempt
def updateNoti(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Notifications.objects.filter(receiver=name).update(status=0)
        return JsonResponse({'success': True, 'message': 'Belirli koşulu sağlayan tüm veriler başarıyla güncellendi.'})



@csrf_exempt
def getTournaments(request):
    gamers = Tournament.objects.all()
    data = [{'name': gamer.name, 'victory': gamer.victory,'status' : gamer.status, 'date' :gamer.date} for gamer in gamers]
    return JsonResponse(data, safe=False)

def my_test(request):
    email = "example@example.com"
    return render(request, 'index.html', {'test': email})

@csrf_exempt
def get_all_player(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        gamers = Tournament.objects.filter(name=email)
        data = [{'name': gamer.name, 'players': gamer.players, 'victory': gamer.victory, 'status' : gamer.status} for gamer in gamers]
        return JsonResponse(data, safe=False)
   
@csrf_exempt
def create_match(request):
    if request.method == 'POST':
        player1 = request.POST.get('player1')
        player2 = request.POST.get('player2')
        name = request.POST.get('tournamentname')
        TournamentMatch.objects.create(player1=player1, player2=player2,tournament=name)
        return JsonResponse({'success': True, 'message': 'Yeni blok eklendi.'})
    return render(request, '#')

@csrf_exempt
def notificationsadd(request):
    if request.method == 'POST':
        receiver = request.POST.get('receiver')
        message = request.POST.get('message')
        status = "5"
        Notifications.objects.create(receiver=receiver, message=message, status=status)
        return JsonResponse({'success': True, 'message': 'Yeni blok eklendi.'})
    return render(request, '#')
   

@csrf_exempt
def starttournament(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        tournament_name = request.POST.get('tournamentname')
        tournament = get_object_or_404(Tournament, name=tournament_name)
        tournament.status = status
        tournament.save()
        return JsonResponse({'success': True, 'message': 'Yeni oyuncu başarıyla eklendi.'})
    


def oauth_callback(request):
    code = request.GET.get('code')
    if code:
        #kullanici yetkilendirme
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': settings.API_42_REDIRECT_URI,
            'client_id': settings.API_42_UID,
            'client_secret': settings.API_42_SECRET
        }

        response = requests.post(settings.API_42_TOKEN_URL, data=data)

        if response.status_code == 200:
            token = response.json().get('access_token')
            user_info_response = requests.get('https://api.intra.42.fr/v2/me', headers={'Authorization': f'Bearer {token}'})
            if(user_info_response.status_code == 200):
                user_info = user_info_response.json()
                email = user_info.get('email')
                name = user_info.get('login')
                profile_picture_url = user_info.get("image", {}).get("link")
                profile_picture_response = requests.get(profile_picture_url)
                selected_picture = None
                if(profile_picture_response.status_code == 200):
                    selected_picture = profile_picture_url
                else:
                     profile_pictures = ['1.png', '2.png','3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png']
                     selected_picture = random.choice(profile_pictures)
                existing_user = Gamers.objects.filter(email=email).first()
                if existing_user is not None:
                    random_num_for_login = random.randint(100000, 999999)
                    subject = 'Giriş Kodu'
                    message = 'Doğrulama kodunuz ' + str(random_num_for_login)
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email]
                    send_mail(subject, message, email_from, recipient_list)
                    token = RefreshToken.for_user(existing_user)
                    return render(request, 'index.html', {'mail': email, 'token': str(token.access_token), 'random_num_for_login': random_num_for_login})
                Gamers.objects.create(name=name, email=email, profile_picture=selected_picture)
                random_num_for_login = random.randint(100000, 999999)
                subject = 'Giriş Kodu'
                message = 'Doğrulama kodunuz ' + str(random_num_for_login)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list)
                existing_user = Gamers.objects.filter(email=email).first()
                token = RefreshToken.for_user(existing_user)
                return render(request, 'index.html', {'mail': email , 'token': str(token.access_token), 'random_num_for_login': random_num_for_login})
            else:
                return redirect('/index/')# hata durumu yonlendirme
        else:
            return redirect('/index/') # hata durumu yonlendirme
    return redirect('/index/') # hata durumu yonlendirme


@csrf_exempt
def updateMatchHistory(request):
    if request.method == 'POST':
        user1 = request.POST.get('user1')
        user2 = request.POST.get('user2')
        name = request.POST.get('name')
        score = request.POST.get('score')
        status =  1
        tournament = get_object_or_404(TournamentMatch, tournament=name, player1=user1, player2=user2)
        tournament.status = status
        tournament.score = score
        tournament.save()
        return JsonResponse({'success': True, 'message': 'Yeni blok eklendi.'})
    return render(request, '#')


@csrf_exempt
def addMatchHistory(request):
    if request.method == 'POST':
        user1 = request.POST.get('user1')
        user2 = request.POST.get('user2')
        user1score = request.POST.get('user1score')
        user2score = request.POST.get('user2score')
        game = request.POST.get('game')
        GameHistory.objects.create(user1=user1, user2=user2,user1score=user1score,user2score=user2score,game=game)
        return JsonResponse({'success': True, 'message': 'Yeni blok eklendi.'})
    return render(request, '#')

@csrf_exempt
def endtournament(request):
    if request.method == 'POST':
        victory = request.POST.get('victory')
        tournament_name = request.POST.get('name')
        tournament = get_object_or_404(Tournament, name=tournament_name)
        tournament.victory = victory
        tournament.save()
        return JsonResponse({'success': True, 'message': 'Yeni oyuncu başarıyla eklendi.'})
    return render(request, '#')

@csrf_exempt
def control_tournament(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gamers = Tournament.objects.filter(name=name)
        if gamers:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    return render(request, '#')


@csrf_exempt
def update_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        foto = request.FILES.get('foto')
        email = request.POST.get('email')
        gamer = Gamers.objects.filter(email=email).first()
        if foto is None:
            print("Fotoğraf seçilmedi.")
            foto = gamer.profile_picture
        else:
            file_path = os.path.join(settings.STATIC_ROOT, 'profile', foto.name)
            with open(file_path, 'wb') as f:
                for chunk in foto.chunks():
                    f.write(chunk)
            foto = foto.name
        if Gamers.objects.filter(name=username).exists():
            print("Bu isim zaten kullanımda.")
            return JsonResponse({'success': False, 'message': 'Bu isim zaten kullanımda.'}) 
        if gamer is not None:
            gamer.name = username
            gamer.profile_picture = foto
            gamer.save()
            return JsonResponse({'success': True, 'message': 'Profil güncellendi.', 'name': username,'profile_picture': foto})
        else:
            return JsonResponse({'success': False, 'message': 'Kullanıcı bulunamadı.'})
    else:
        # Geçersiz istek durumunda hata yanıtı döndür
        return JsonResponse({'success': False, 'message': 'Geçersiz istek.'})