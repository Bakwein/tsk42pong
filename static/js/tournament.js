        function getTournaments() {
            localStorage.removeItem('tournament');
            var email = localStorage.getItem('userName');
            var gamerNames = [];
            var combinedNames = "";
            $.ajax({
                url: '/getTournaments/',
                type: 'POST',
                data: {
                    'email': email
                },
                success: function (response) {
                    $('#youzify-groups-list').empty();
                    if (Array.isArray(response)) { // response bir dizi mi kontrolü
                        response.forEach(function (gamer) {
                            combinedNames = combinedNames + "#" + gamer.name;
                            if (gamer.victory == "") {
                                var renk = "background-color: #477195;";
                                var yazi = "Yakında başlayacak"
                                var yazi2 = "";
                            }
                            else {
                                var renk = "background-color: #818181cc;";
                                var yazi = "Turnuva Bitti"
                                var yazi2 = "Kazanan :  " + gamer.victory;
                            }
                            const dateObj = new Date(gamer.date);
                            const formattedDate = `${dateObj.getDate()} ${dateObj.getMonth() + 1} ${dateObj.getFullYear()}`;
                            const formattedTime = `${dateObj.getHours()}:${dateObj.getMinutes()}`;

                            var html = `
                                    <li style="width: 33%;list-style-type: none;" >
                                        <div class="stream-item" style="${renk}">
                                            <div class="stream-item__box">
                                                  
                                                <div class="stream-item__body">
                                                    <div class="stream-item__title" style="justify-content: center;display: flex;color:white">
                                                       Turnuva Adı :  <b>${gamer.name}</b>  
                                                    </div>
                                                    <div class="stream-item__time" style="justify-content: center;display: flex;color:white" >${formattedDate} - ${formattedTime} - ${yazi} </div>
                                                    <div class="stream-item__time" style="justify-content: center;display: flex;color:white"> <b> ${yazi2}</b>  </div>
                                        <div class="action" style="display: flex;justify-content: center;margin-top: 21px;">
                                            <div class="group-button public generic-button"><a  onclick="infoTournaments('${gamer.name}')" class="group-button leave-group">İncele</a></div>
                                        </div>
                                                </div>
                                                
                                            </div>
                                        </div>
                                    </li>
                                    `;
                            $('#youzify-groups-list').append(html);
                        });
                        localStorage.setItem('tournamentnames', combinedNames);
                    } else {
                        console.error("Sunucudan beklenen dizi yanıt alınamadı.");
                    }
                }
            });
        }
        function addplayer(name) {
            var playername = document.getElementById("name").value;
            $.ajax({
                url: 'addplayer',
                type: 'POST',
                data: {
                    'name': playername,
                    'tournamentname': name
                },
                success: function (response) {
                    if (response.success) {
                        document.getElementById("name").value = "";
                    } else {
                        alert(response.message);
                    }
                }
            });
            setTimeout(function () {
                playerlist(name);
            }, 2000)
        }


        function ekleUnique(winnerplayers, gamer) {
            if (!winnerplayers.includes(gamer)) {
                winnerplayers += gamer + "#";
            }


            return winnerplayers;
        }



        function filterCharacters(winnerplayer, loserplayer) {
            let winnerArray = winnerplayer.split('#');
            let loserArray = loserplayer.split('#');
            loserArray.forEach(loserChar => {
                winnerArray = winnerArray.filter(winnerChar => winnerChar !== loserChar);
            });
            let result = winnerArray.join('#');
            return result;
        }


        function showMatch(name) {
            var finals = 0;
            var sayac = 0;
            var winnerplayers = "";
            var loserplayers = "";
            var winner = "";
            $.ajax({
                url: '/showmatch/',
                type: 'POST',
                data: {
                    'name': name
                },
                success: function (response) {
                    $('#showmatch').empty();
                    if (Array.isArray(response)) { // response bir dizi mi kontrolü
                        response.forEach(function (gamer) {
                            //yapay zeka solda olmamali - isimler karismamasi icin


                            if (gamer.status == 1) {
                                finals = finals + 1;
                                var skor = gamer.score;

                                var numbers = skor.split("-"); // "-" işaretinden bölerek iki sayıya ayırma

                                if (numbers.length === 2) {
                                    var firstNumber = parseInt(numbers[0]); // İlk sayıyı al
                                    var secondNumber = parseInt(numbers[1]); // İkinci sayıyı al
                                    if (isNaN(firstNumber) || isNaN(secondNumber)) {
                                    } else {
                                        if (firstNumber > secondNumber) {
                                            winnerplayers = ekleUnique(winnerplayers, gamer.user1);
                                            loserplayers = ekleUnique(loserplayers, gamer.user2);
                                        } else if (firstNumber < secondNumber) {
                                            winnerplayers = ekleUnique(winnerplayers, gamer.user2);
                                            loserplayers = ekleUnique(loserplayers, gamer.user1);
                                        } else {
                                        }
                                    }
                                }
                                else {
                                }
                            }
                            if (gamer.user1score < gamer.user2score) {
                                var renk = "background-color: #f56464;";
                            }
                            else {
                                var renk = "background-color: #52b0c5;";
                            }
                            if (gamer.status == 0) {
                                var button = "Maçı Oyna";
                                if (gamer.user1 == "ai" || gamer.user2 == "ai")
                                    var control = "tournamentponggameai";
                                else
                                    var control = "tournamentponggame";
                            }
                            else {
                                var button = gamer.score;
                                var control = "controlnone";
                            }
                            //if(gamer.user1 === "ai")
                            //    gamer.user1 = "Yapay Zeka";
                            //if(gamer.user2 === "ai")
                            //    gamer.user2 = "Yapay Zeka";

                            const dateObj = new Date(gamer.date);
                            const formattedDate = `${dateObj.getDate()} ${dateObj.getMonth() + 1} ${dateObj.getFullYear()}`;
                            const formattedTime = `${dateObj.getHours()}:${dateObj.getMinutes()}`;
                            var html = `
                                    <li data-type="${gamer.game}" style="width: 33%;">
                                        <div class="stream-item" style="${renk}">
                                            <div class="stream-item__box">
                                                  
                                                <div class="stream-item__body">
                                                    <div class="stream-item__title" style="justify-content: center;display: flex;">
                                                        ${gamer.user1} - ${gamer.user2}
                                                    </div>
                                                    <div class="group-button public generic-button" style="
    display: flex;
    justify-content: center;
    background-color: white;
    border-radius: 11px;
    padding: 10px;
"><a onclick="${control}('${gamer.user1}','${gamer.user2}','${name}')" class="group-button leave-group">${button}</a>
</div>
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                    `;
                            $('#showmatch').append(html);
                            sayac = sayac + 1;
                        });
                    } else {
                        console.error("Sunucudan beklenen dizi yanıt alınamadı.");
                    }
                    if (finals != 0 && sayac != 0 && finals == sayac) {
                        let winner = filterCharacters(winnerplayers, loserplayers); // Değişiklik burada
                        winner = winner + "#";
                        looptournament(name, winner);
                    }

                }
            });
        }





        function playerlist(name) {
            $.ajax({
                url: '/get_all_player/',
                type: 'POST',
                data: {
                    'email': name
                },
                success: function (response) {
                    $('#player-list').empty();
                    if (Array.isArray(response)) { // response bir dizi mi kontrolü
                        response.forEach(function (gamer) {
                            if (gamer.status == 0) {
                                document.getElementById("addplayer").style.display = "flex";
                                document.getElementById("startournament").style.display = "flex";
                                document.getElementById("player-list").style.display = "flex";
                                document.getElementById("addplayertwo").style.display = "flex";
                                document.getElementById("headone").style.display = "flex";
                            }
                            else {
                                document.getElementById("addplayer").style.display = "none";
                                document.getElementById("startournament").style.display = "none";
                                document.getElementById("player-list").style.display = "none";
                                document.getElementById("addplayertwo").style.display = "none";
                                document.getElementById("headone").style.display = "none";
                            }
                            var playersArray = gamer.players.split("#");
                            for (var i = 0; i < playersArray.length; i++) {
                                var html = `<li style="
    width: 33%;
">
                                            <div class="user-item --active">
                                                <div class="user-item__desc">
                                                    <div class="user-item__name"><a >${playersArray[i]}</a></div>
                                                </div>
                                            </div>
                                        </li>`;
                                $('#player-list').append(html);
                            }

                        });
                    } else {
                        console.error("Sunucudan beklenen dizi yanıt alınamadı.");
                    }
                }
            });
        }


        function randomizePairs(playersArray) {
            playersArray = playersArray.sort(() => Math.random() - 0.5);
            let pairs = [];
            const numberOfPlayers = playersArray.length;
            for (let i = 0; i < numberOfPlayers; i += 2) {
                if (i === numberOfPlayers - 1) {
                    if (playersArray[i] !== "ai")
                        pairs.push([playersArray[i], 'ai']);
                } else {
                    pairs.push([playersArray[i], playersArray[i + 1]]);
                }
            }

            return pairs;
        }


        function startournament() {
            var name = localStorage.getItem('tournament');
            document.getElementById("startournament").style.display = "none";
            document.getElementById("addplayer").style.display = "none";
            document.getElementById("startournament").style.display = "none";
            document.getElementById("player-list").style.display = "none";
            document.getElementById("addplayertwo").style.display = "none";
            document.getElementById("headone").style.display = "none";
            var i = 0;
            var message = name + " adlı turnuva başladı! İyi şanslar!";
            $.ajax({
                url: '/starttournament/',
                type: 'POST',
                data: {
                    'status': '1',
                    'tournamentname': name
                },
                success: function (response) {
                    if (response.success) {
                    } else {
                    }
                }
            });

            $.ajax({
                url: '/get_all_player/',
                type: 'POST',
                data: {
                    'email': name
                },
                success: function (response) {
                    if (Array.isArray(response)) { // response bir dizi mi kontrolü
                        response.forEach(function (gamer) {
                            var playersArray = gamer.players.split("#");
                            var playersArraytwo = playersArray
                            playersArraytwo.forEach(gamer => {
                                $.ajax({
                                    url: '/notificationsadd/',
                                    type: 'POST',
                                    data: {
                                        'receiver': playersArraytwo[i],
                                        'message': message
                                    },
                                    success: function (response) {
                                        if (response.success) {

                                        } else {
                                        }
                                    }
                                });
                                i++;
                            });

                            const matches = randomizePairs(playersArray);
                            matches.forEach(match => {
                                if (match[0] === "ai") {
                                    match[0] = match[1];
                                    match[1] = "ai";
                                }
                                $.ajax({
                                    url: '/create_match/',
                                    type: 'POST',
                                    data: {
                                        'player1': match[0],
                                        'player2': match[1],
                                        'tournamentname': name
                                    },
                                    success: function (response) {
                                        if (response.success) {
                                            showMatch(name);
                                        } else {
                                        }
                                    }
                                });
                            });

                        });

                    } else {
                        console.error("Sunucudan beklenen dizi yanıt alınamadı.");
                    }
                }

            });



        }

        var winnerplayersTemp = "";

        function looptournament(name, winnerplayers) {
            if (winnerplayersTemp == winnerplayers) {
                return 0;
            } else {
                winnerplayersTemp = winnerplayers;
            }
            var yeniStr = winnerplayers.slice(0, -1);
            var playersArray = yeniStr.split("#");
            if (playersArray.length <= 1) {
                alert("Turnuva Bitti. Kazanan = " + playersArray[0]);
                $.ajax({
                    url: '/endtournament/',
                    type: 'POST',
                    data: {
                        'victory': playersArray[0],
                        'name': name
                    },
                    success: function (response) {
                        if (response.success) {
                        } else {
                        }
                    }
                });

                return 0;
            }
            const matches = randomizePairs(playersArray);
            matches.forEach(match => {
                if (match[0] === "ai") {
                    match[0] = match[1];
                    match[1] = "ai";
                }
                $.ajax({
                    url: '/create_match/',
                    type: 'POST',
                    data: {
                        'player1': match[0],
                        'player2': match[1],
                        'tournamentname': name
                    },
                    success: function (response) {
                        if (response.success) {
                        } else {
                        }
                    }
                });
            });
            setTimeout(function () {
                showMatch(name);
            }, 2000);
        }

        function infoTournaments(name) {
            localStorage.setItem('tournament', name);
            localStorage.setItem('lastPage', 'tournament');
            fetch('/infotournaments')
                .then(response => response.text())
                .then(html => {
                    document.getElementById("content").innerHTML = html;
                    var inputs = document.querySelectorAll(".uk-input");
                    inputs.forEach(function (input) {
                        input.addEventListener("keypress", function (event) {
                            if (event.keyCode === 13) {
                                event.preventDefault();
                            }
                        });
                    });
                    showMatch(name);
                    document.getElementById("startournament").addEventListener("click", startournament);
                    document.getElementById("addplayer").addEventListener("click", function () {
                        addplayer(name);
                    });
                    playerlist(name);
                })
                .catch(error => console.error('Hata:', error));
        }