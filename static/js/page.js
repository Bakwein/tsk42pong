        var contentChoice = 0;
        function contentUpdate() {
            contentChoice = 1;
            loadContent();
        }
        function contentUpdate2() {
            contentChoice = 0;
            loadContent();
        }
        function loadRegister() {
        localStorage.removeItem('registerkey');
            fetch('/register')
                .then(response => response.text())
                .then(html => {
                    document.getElementById("page").innerHTML = html;
                    document.getElementById("loginpage").addEventListener("click", loadContent);
                })
                .catch(error => console.error('Hata:', error));
        }
        function loadContent(status) {
            var userEmail = localStorage.getItem('token');
            var loginstatus= localStorage.getItem('loginstatus');
            if(loginstatus === 'true')
                contentChoice = 1;
            else
                contentChoice = 0;               
            if (contentChoice === 1) {
                fetch('/main')
                    .then(response => response.text())
                    .then(html => {
                        document.getElementById("page").innerHTML = html;
                        if(localStorage.getItem('lastPage') === 'friend') {
                            handleFriendClick();
                        }
                        else {
                            document.getElementById("friend").addEventListener("click", handleFriendClick);
                        }
                        if(localStorage.getItem('lastPage') === 'tournament') {
                            handleTournamentClick();
                        }
                        else {
                            document.getElementById("tournament").addEventListener("click", handleTournamentClick);
                        }
                        if(localStorage.getItem('lastPage') === 'notifications') {
                            handleNotificationsClick();
                        }
                        else {
                            document.getElementById("notifications").addEventListener("click", handleNotificationsClick);
                        }
                        if(localStorage.getItem('lastPage') === 'game') {
                            handleGameClick();
                        }
                        else {
                            document.getElementById("game").addEventListener("click", handleGameClick);
                        }
                        if(localStorage.getItem('lastPage') === 'chat') {
                            handleChatClick();
                        }
                        else {
                            document.getElementById("chats").addEventListener("click", handleChatClick);
                        }
                        if(localStorage.getItem('lastPage') === 'gameai') {
                            handleAIGameClick();
                        }
                        else {
                            document.getElementById("gameai").addEventListener("click", handleAIGameClick);
                        }
                        if(localStorage.getItem('lastPage') === 'tictactoe') {
                            handleTicTacToeGameClick();
                        }
                        else {
                            document.getElementById("game2").addEventListener("click", handleTicTacToeGameClick);
                        }
                        if(localStorage.getItem('lastPage') === 'profile') {
                            handleProfileClick();
                        }
                        else {
                            document.getElementById("profile").addEventListener("click", handleProfileClick);
                        }
                        document.getElementById("home").addEventListener("click", handleMainClick);
                        document.getElementById("logout").addEventListener("click", logout);
                        kullaniciVeri();
                    })
                    .catch(error => console.error('Hata:', error));
            } else if (contentChoice === 0) {
                var registerkey = localStorage.getItem('registerkey');
                var random_num_for_login = localStorage.getItem('random_num_for_login');
                if(random_num_for_login)
                {
                    fetch('login_key/')
                    .then(response => response.text())
                    .then(html => {
                        document.getElementById("page").innerHTML = html;
                        document.getElementById("keylogin").addEventListener("click", keylogincontrol);
                        document.getElementById("register").addEventListener("click", loadRegister);
                        //history.pushState({id: 'loginkey',html_text:html}, null, null);
                    })
                    .catch(error => console.error('Hata:', error));
                }
                else if(registerkey !== null)
                {
                    fetch('/registerkey/')
                    .then(response => response.text())
                    .then(html => {
                        document.getElementById("page").innerHTML = html;
                        document.getElementById("keyregister").addEventListener("click", keyregistercontrol);
                        document.getElementById("register").addEventListener("click", loadRegister);
                        //history.pushState({id: 'registerkey',html_text:html}, null, null);

                    })
                    .catch(error => console.error('Hata:', error));
                }
                else{
                fetch('/login')
                    .then(response => response.text())
                    .then(html => {
                        document.getElementById("page").innerHTML = html;
                        localStorage.removeItem('registerkey');
                        document.getElementById("register").addEventListener("click", loadRegister);
                        //history.pushState({id: 'login',html_text:html}, null, null);

                        if (status === "basarili") {
                        document.getElementById('success-message').innerHTML = 'Kayıt başarılı';
            }
                    })
                    .catch(error => console.error('Hata:', error));
                }
            }
        }
        function handleFriendClick() {
            localStorage.setItem('lastPage', 'friend');
                         fetch('/friend')
                            .then(response => response.text())
                            .then(html => {


                                document.getElementById("content").innerHTML = html;
                                history.pushState({id: 'friend',html_text:html}, null, null);
                            })
                            .catch(error => console.error('Hata:', error));
        }
        function handleNotificationsClick() {
            console.log('notifications');
            localStorage.setItem('lastPage', 'notifications');
                         fetch('/notifications')
                            .then(response => response.text())
                            .then(html => {
                                document.getElementById("content").innerHTML = html;
                                history.pushState({id: 'notifications',html_text:html}, null, null);
                                getNotifications();
                            })
                            .catch(error => console.error('Hata:', error));
        }


        
        function handleTournamentClick() {
            localStorage.setItem('lastPage', 'tournament');
                         fetch('/tournament')
                            .then(response => response.text())
                            .then(html => {
                                document.getElementById("content").innerHTML = html;
                                document.getElementById("tournamentcreate").addEventListener("click", tournamentcreate);
                                history.pushState({id: 'tournament',html_text:html}, null, null);

                                getTournaments();
    
                            })
                            .catch(error => console.error('Hata:', error));
        }
        function handleChatClick() {
            localStorage.setItem('lastPage', 'chat');
                         fetch('/chats')
                            .then(response => response.text())
                            .then(html => {
                                document.getElementById("content").innerHTML = html;
                                history.pushState({id: 'chats',html_text:html}, null, null);

                            })
                            .catch(error => console.error('Hata:', error));
        }
        function handleGameClick() {
            localStorage.setItem('lastPage', 'game');
                         fetch('/game')
                            .then(response => response.text())
                            .then(html => {
                                document.getElementById("content").innerHTML = html;
                                document.getElementById("gamesetting").addEventListener("click", ponggameform);
                                history.pushState({id: 'game',html_text:html}, null, null);

                            })
                            .catch(error => console.error('Hata:', error));
        }
        function handleAIGameClick(){
            localStorage.setItem('lastPage', 'gameai');
                         fetch('/gameai')
                            .then(response => response.text())
                            .then(html => {
                                document.getElementById("content").innerHTML = html;
                                document.getElementById("gamesettingtwo").addEventListener("click", ponggameformtwo);
                                history.pushState({id: 'gameai',html_text:html}, null, null);

                                
                            })
                            .catch(error => console.error('Hata:', error));
        }
        function handleTicTacToeGameClick(){
            localStorage.setItem('lastPage', 'tictactoe');
                         fetch('/tictactoe')
                            .then(response => response.text())
                            .then(html => {
                                document.getElementById("content").innerHTML = html;
                                history.pushState({id: 'tictactoe',html_text:html}, null, null);

                                tictactoe();
                            })
                            .catch(error => console.error('Hata:', error));
        }
        function handleProfileClick(){
            localStorage.setItem('lastPage', 'profile');
                         fetch('/profile')
                            .then(response => response.text())
                            .then(html => {
                                document.getElementById("content").innerHTML = html;
                                history.pushState({id: 'profile',html_text:html}, null, null);

                                userinfo();
                                getGameHistory();
                            })
                            .catch(error => console.error('Hata:', error));
        }
        function handleMainClick() {
            localStorage.setItem('lastPage', 'main');
            fetch('/home')
                .then(response => response.text())
                .then(html => {
                    document.getElementById("content").innerHTML = html;
                    history.pushState({id: 'home',html_text:html}, null, null);
                })
                .catch(error => console.error('Hata:', error));
            contentUpdate();
        }


        window.onpopstate = function(event) {
            if (event.state) {
              document.getElementById('content').innerHTML = event.state.html_text;
            }
          };