plansza = function (k) {
    var kratki = parseInt($(k).val());
    var bok = parseFloat(600 / kratki);
    for (let i = 0; i < kratki; i++) {
        for (let j = 0; j < kratki; j++) {
            let newRect = document.createElementNS('http://www.w3.org/2000/svg', "rect");
            newRect.setAttribute("x", `${i * bok}`);
            newRect.setAttribute("y", `${j * bok}`);
            newRect.setAttribute("width", `${bok}`);
            newRect.setAttribute("height", `${bok}`);
            newRect.setAttribute("fill", "black");
            newRect.setAttribute("stroke", "black");
            newRect.setAttribute("stroke-width", "1");
            newRect.setAttribute("id", `${i}-${j}`);
            newRect.setAttribute("class", 'rect');
            newRect.setAttribute("kolor", 'black');
            document.getElementById('pole').appendChild(newRect)
        }
    }
    return ''
}


$(document).ready(function () {
    plansza($('.display'))
    var kratki = $('.display').val()

    var zmiana_ruchu = {
        "R": {'(0, -1)': [-1, 0], '(-1, 0)': [0, 1], '(0, 1)': [1, 0], '(1, 0)': [0, -1]},
        "L": {'(0, -1)': [1, 0], '(1, 0)': [0, 1], '(0, 1)': [-1, 0], '(-1, 0)': [0, -1]},
    }
    var pos = []
    var kierunek_ruchu = []
    var kolor = ['white', 'blue', 'red', 'green', 'yellow']


    ruch = function () {
        for (let i = 0; i < pos.length; i++) {
            if (document.getElementById(`${pos[i][0]}-${pos[i][1]}`).getAttribute("fill") === 'black') {
                document.getElementById(`${pos[i][0]}-${pos[i][1]}`).setAttribute("fill", kolor[i]);
                document.getElementById(`${pos[i][0]}-${pos[i][1]}`).setAttribute("kolor", kolor[i]);
                kierunek_ruchu[i] = zmiana_ruchu["R"][`(${kierunek_ruchu[i][0]}, ${kierunek_ruchu[i][1]})`];
                pos[i][0] = pos[i][0] + kierunek_ruchu[i][0];
                pos[i][1] = pos[i][1] + kierunek_ruchu[i][1];
            } else {
                document.getElementById(`${pos[i][0]}-${pos[i][1]}`).setAttribute("fill", "black");
                document.getElementById(`${pos[i][0]}-${pos[i][1]}`).setAttribute("fill", "black");
                kierunek_ruchu[i] = zmiana_ruchu["L"][`(${kierunek_ruchu[i][0]}, ${kierunek_ruchu[i][1]})`];
                pos[i][0] = pos[i][0] + kierunek_ruchu[i][0];
                pos[i][1] = pos[i][1] + kierunek_ruchu[i][1];
            }
            if (pos[i][0] == -1) {
                pos[i][0] = kratki - 1
            }
            if (pos[i][0] == kratki) {
                pos[i][0] = 0
            }
            if (pos[i][1] == -1) {
                pos[i][1] = kratki - 1
            }
            if (pos[i][1] == kratki) {
                pos[i][1] = 0
            }
        }

    }

    var intervalId;
    $('#start').on('click', function () {
        $('#stop').click()
        intervalId = setInterval(ruch, 1000 / $('#predkosc').val());
    });

    $('#stop').on('click', function () {
        clearInterval(intervalId);
        intervalId = false
    })

    $('#reset').on('click', function () {
        location.reload()
    });

    $('#predkosc').bind("input", function () {
        if (intervalId) {
            $('#start').click()
        }

    })
    $('.rect').on('click', function () {
        console.log(pos)
        if (pos.length < kolor.length) {
            var rec_pos = $(this).attr('id').split('-')
            $(this).attr('fill', kolor[pos.length])
            pos.push([parseInt(rec_pos[0]), parseInt(rec_pos[1])])
            kierunek_ruchu.push([0, 1])

        }
    }).hover(function () {
        $(this).attr('stroke', kolor[pos.length])
    }, function () {
        $(this).attr('stroke', 'black')
    })

    $('#rozmiar').on('change', function () {
        $('#stop').click()
        $('#pole').empty();
        $("#pole").load(window.location.href + plansza($(this)));
        kratki = $(this).val()
        while (pos.length > 0) {
            pos.pop()
            kierunek_ruchu.pop()
        }
    })

})

