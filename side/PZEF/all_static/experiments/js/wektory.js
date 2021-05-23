len_vec = function (X, Y) {
    var l = Math.sqrt((X[0] - X[1]) ** 2 + (Y[0] - Y[1]) ** 2)
    return l
}

rysowanie_in = function (AB, CD, grot_vec1, grot_vec2) {
    var X_vec1 = AB[0]
    var Y_vec1 = AB[1]
    var X_vec2 = CD[0]
    var Y_vec2 = CD[1]
    var trace1 = {
        x: X_vec1,
        y: Y_vec1,
        name: 'Wektor AB',
        marker: {
            color: '#ee5959',
        },
        text: ['Punkt A', 'Punkt B'],
        type: 'scatter',
        line: {
            color: '#13d9ef'
        }
    };

    var trace2 = {
        x: X_vec2,
        y: Y_vec2,
        name: 'Wektor CD',
        marker: {
            color: '#13d9ef',

        },
        text: ['Punkt C', 'Punkt D'],
        type: 'scatter',
        line: {
            color: '#ee5959'
        }
    };

    var data = [trace1, trace2];
    var layout = {
        hovermode: 'closest',
        title: {
            text: 'Wektory wejściowe',
            font: {
                color: '#d3d3d3',
            }
        },
        xaxis: {
            title: {
                text: 'x',
                font: {
                    color: '#d3d3d3',
                }
            },
            gridcolor: '#323232',
            gridwidth: 0.5,
            zerolinecolor: '#d3d3d3',
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },
        },
        yaxis: {
            title: {
                text: 'y',
                font: {
                    color: '#d3d3d3',
                }
            },
            scaleanchor: "x",
            gridcolor: '#323232',
            gridwidth: 0.5,
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },
        },
        shapes: [
            {
                type: 'path',
                path: grot_vec1,
                fillcolor: '#13d9ef',
                line: {
                    color: '#13d9ef',
                }
            },
            {
                type: 'path',
                path: grot_vec2,
                fillcolor: '#ee5959',
                line: {
                    color: '#ee5959',
                }
            }
        ],
        showlegend: false,
        margin: {'t': 35},
        paper_bgcolor: '#202020',
        plot_bgcolor: '#202020',
    };

    var config = {
        responsive: true,
        displayModeBar: false,
    }

    Plotly.newPlot('input_vec', data, layout, config);
}

rysowanie_out = function (AB, CD, EF, grot_vec1, grot_vec2, grot_vec3, d) {
    var X_vec1 = AB[0]
    var Y_vec1 = AB[1]
    var X_vec2 = CD[0]
    var Y_vec2 = CD[1]
    var X_vec3 = EF[0]
    var Y_vec3 = EF[1]
    var X_dot1 = [AB[0][1], EF[0][1]]
    var Y_dot1 = [AB[1][1], EF[1][1]]
    var X_dot2 = [CD[0][1], EF[0][1]]
    var Y_dot2 = [CD[1][1], EF[1][1]]
    var trace1 = {
        x: X_vec1,
        y: Y_vec1,
        name: 'Wektor AB',
        marker: {
            color: '#ee5959',
        },
        text: ['Punkt A', 'Punkt B'],
        type: 'scatter',
        line: {
            color: '#13d9ef'
        }
    };

    var trace2 = {
        x: X_vec2,
        y: Y_vec2,
        name: 'Wektor CD',
        marker: {
            color: '#13d9ef',

        },
        text: ['Punkt C', 'Punkt D'],
        type: 'scatter',
        line: {
            color: '#ee5959'
        }
    };

    var trace3 = {
        x: X_vec3,
        y: Y_vec3,
        name: 'Wektor EF',
        marker: {
            color: '#6fee59',

        },
        text: ['Punkt E', 'Punkt F'],
        type: 'scatter',
        line: {
            color: '#efca13'
        }
    };

    var dot1 = {
        x: X_dot1,
        y: Y_dot1,
        mode: 'lines',
        line: {
            dash: 'dot',
            color: '#ee5959'
        }
    };
    if (d == 'dod') {
        var dot2 = {
            x: X_dot2,
            y: Y_dot2,
            mode: 'lines',
            line: {
                dash: 'dot',
                color: '#13d9ef'
            }
        };

        var data = [trace1, trace2, trace3, dot1, dot2];
    } else {
        var data = [trace1, trace2, trace3, dot1];
    }
    var layout = {
        hovermode: 'closest',
        title: {
            text: 'Wynik',
            font: {
                color: '#d3d3d3',
            }
        },
        xaxis: {
            title: {
                text: 'x',
                font: {
                    color: '#d3d3d3',
                }
            },
            gridcolor: '#323232',
            gridwidth: 0.5,
            zerolinecolor: '#d3d3d3',
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },
        },
        yaxis: {
            title: {
                text: 'y',
                font: {
                    color: '#d3d3d3',
                }
            },
            scaleanchor: "x",
            gridcolor: '#323232',
            gridwidth: 0.5,
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },
        },
        shapes: [
            {
                type: 'path',
                path: grot_vec1,
                fillcolor: '#13d9ef',
                line: {
                    color: '#13d9ef',
                }
            },
            {
                type: 'path',
                path: grot_vec2,
                fillcolor: '#ee5959',
                line: {
                    color: '#ee5959',
                }
            },
            {
                type: 'path',
                path: grot_vec3,
                fillcolor: '#efca13',
                line: {
                    color: '#efca13',
                }
            }
        ],
        showlegend: false,
        margin: {'t': 35},
        paper_bgcolor: '#202020',
        plot_bgcolor: '#202020',
    };

    var config = {
        responsive: true,
        displayModeBar: false,
    }

    Plotly.newPlot('output_vec', data, layout, config);
}

strzalka = function (X, Y) {
    var grot_l_x = X[1] + (X[0] - X[1]) * Math.cos(-Math.PI / 6) - (Y[0] - Y[1]) * Math.sin(-Math.PI / 6)
    var grot_l_y = Y[1] + (X[0] - X[1]) * Math.sin(-Math.PI / 6) + (Y[0] - Y[1]) * Math.cos(-Math.PI / 6)
    var grot_p_x = X[1] + (X[0] - X[1]) * Math.cos(Math.PI / 6) - (Y[0] - Y[1]) * Math.sin(Math.PI / 6)
    var grot_p_y = Y[1] + (X[0] - X[1]) * Math.sin(Math.PI / 6) + (Y[0] - Y[1]) * Math.cos(Math.PI / 6)

    var grot = [[], []]

    grot[0].push(X[1] + 0.1 * (grot_l_x - X[1]))
    grot[0].push(X[1])
    grot[0].push(X[1] + 0.1 * (grot_p_x - X[1]))

    grot[1].push(Y[1] + 0.1 * (grot_l_y - Y[1]))
    grot[1].push(Y[1])
    grot[1].push(Y[1] + 0.1 * (grot_p_y - Y[1]))

    return `M ${grot[0][0]} ${grot[1][0]} L ${grot[0][1]} ${grot[1][1]} L ${grot[0][2]} ${grot[1][2]} Z`
}

wejscie = function () {
    var Ax = parseFloat($('#Ax').val())
    if (isNaN(Ax)) {
        Ax = 0
    }
    var Ay = parseFloat($('#Ay').val())
    if (isNaN(Ay)) {
        Ay = 0
    }
    var Bx = parseFloat($('#Bx').val())
    if (isNaN(Bx)) {
        Bx = 0
    }
    var By = parseFloat($('#By').val())
    if (isNaN(By)) {
        By = 0
    }
    var Cx = parseFloat($('#Cx').val())
    if (isNaN(Cx)) {
        Cx = 0
    }
    var Cy = parseFloat($('#Cy').val())
    if (isNaN(Cy)) {
        Cy = 0
    }
    var Dx = parseFloat($('#Dx').val())
    if (isNaN(Dx)) {
        Dx = 0
    }
    var Dy = parseFloat($('#Dy').val())
    if (isNaN(Dy)) {
        Dy = 0
    }

    var X_vec1 = [Ax, Bx]
    var Y_vec1 = [Ay, By]
    var grot_vec1 = strzalka(X_vec1, Y_vec1)

    var X_vec2 = [Cx, Dx]
    var Y_vec2 = [Cy, Dy]
    var grot_vec2 = strzalka(X_vec2, Y_vec2)
    rysowanie_in([X_vec1, Y_vec1], [X_vec2, Y_vec2], grot_vec1, grot_vec2)
    $('.pAx').text(X_vec1[0])
    $('.pAy').text(Y_vec1[0])
    $('.pBx').text(X_vec1[1])
    $('.pBy').text(Y_vec1[1])
    $('.pCx').text(X_vec2[0])
    $('.pCy').text(Y_vec2[0])
    $('.pDx').text(X_vec2[1])
    $('.pDy').text(Y_vec2[1])
}

wyjscie = function (dzialanie) {
    var Ax = parseFloat($('#Ax').val())
    if (isNaN(Ax)) {
        Ax = 0
    }
    var Ay = parseFloat($('#Ay').val())
    if (isNaN(Ay)) {
        Ay = 0
    }
    var Bx = parseFloat($('#Bx').val())
    if (isNaN(Bx)) {
        Bx = 0
    }
    var By = parseFloat($('#By').val())
    if (isNaN(By)) {
        By = 0
    }
    var Cx = parseFloat($('#Cx').val())
    if (isNaN(Cx)) {
        Cx = 0
    }
    var Cy = parseFloat($('#Cy').val())
    if (isNaN(Cy)) {
        Cy = 0
    }
    var Dx = parseFloat($('#Dx').val())
    if (isNaN(Dx)) {
        Dx = 0
    }
    var Dy = parseFloat($('#Dy').val())
    if (isNaN(Dy)) {
        Dy = 0
    }
    var X_vec1 = [Ax, Bx]
    var Y_vec1 = [Ay, By]
    var grot_vec1 = strzalka(X_vec1, Y_vec1)

    var X_vec2 = [X_vec1[0], Dx - Cx + X_vec1[0]]
    var Y_vec2 = [Y_vec1[0], Dy - Cy + Y_vec1[0]]
    var grot_vec2 = strzalka(X_vec2, Y_vec2)
    if (dzialanie == 'Dodawanie (AB+CD)') {
        $('.formula2').hide()
        $('.formula1').show()
        $('.znak').text(' + ')
        var X_vec3 = [X_vec1[0], X_vec1[1] + X_vec2[1] - X_vec1[0]]
        var Y_vec3 = [Y_vec1[0], Y_vec1[1] + Y_vec2[1] - Y_vec1[0]]
        var grot_vec3 = strzalka(X_vec3, Y_vec3)

        rysowanie_out([X_vec1, Y_vec1], [X_vec2, Y_vec2], [X_vec3, Y_vec3], grot_vec1, grot_vec2, grot_vec3, 'dod')
    } else if (dzialanie == 'Odejmowanie (AB-CD)') {
        $('.formula2').hide()
        $('.formula1').show()
        $('.znak').text(' - ')
        var X_vec3 = [X_vec1[0], X_vec1[1] - X_vec2[1] + X_vec1[0]]
        var Y_vec3 = [Y_vec1[0], Y_vec1[1] - Y_vec2[1] + Y_vec1[0]]
        var grot_vec3 = strzalka(X_vec3, Y_vec3)

        rysowanie_out([X_vec1, Y_vec1], [X_vec2, Y_vec2], [X_vec3, Y_vec3], grot_vec1, grot_vec2, grot_vec3, 'ode')
    } else if (dzialanie == 'Lloczyn skalarny (AB∘CD)') {
        $('.formula1').hide()
        $('.formula2').show()
        $('.BAx').text(Bx - Ax)
        $('.BAy').text(By - Ay)
        $('.DCx').text(Dx - Cx)
        $('.DCy').text(Dy - Cy)
        $('#output_vec').empty()
    }
    if (dzialanie != 'Lloczyn skalarny (AB∘CD)') {
        $('#wynik').text(`(${X_vec3[0]}, ${Y_vec3[0]}), (${X_vec3[1]}, ${Y_vec3[1]})`)
        $('#dl_AB').text(len_vec(X_vec1, Y_vec1))
        $('#dl_CD').text(len_vec(X_vec2, Y_vec2))
        $('#dl_EF').text(len_vec(X_vec3, Y_vec3))
    } else {
        $('.wynik2').text((Bx - Ax) * (Dx - Cx) + (By - Ay) * (Dy - Cy))
    }
}

$(document).ready(function () {
    $('input.display').bind("input", function () {

        wejscie()
        wyjscie($('.operacje').val())

    }).trigger('input');
    $('.operacje').bind("input", function () {

        wejscie()
        wyjscie($('.operacje').val())

    }).trigger('input');
})
