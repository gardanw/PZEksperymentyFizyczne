odejmowanie = function (lista1, lista2) {
    var lista1 = $(lista1)
    var lista2 = $(lista2)
    if (lista1.length == lista2.length) {
        var nowa_lista = []
        for (let i = 0; i < lista1.length; i++) {
            nowa_lista.push(lista1[i] - lista2[i])
        }
        return nowa_lista
    }
}

dodawanie = function (lista1, lista2) {
    var lista1 = $(lista1)
    var lista2 = $(lista2)
    if (lista1.length === lista2.length) {
        var nowa_lista = []
        for (let i = 0; i < lista1.length; i++) {
            nowa_lista.push(lista1[i] + lista2[i])
        }
        return nowa_lista
    }
}

dzielenie = function (lista, dzielnik) {
    var lista = $(lista)
    var dzielnik = $(dzielnik)[0]
    var new_lista = []
    for (let i = 0; i < lista.length; i++) {
        new_lista.push(lista[i] / dzielnik)
    }
    return new_lista
}

potegowanie = function (lista) {
    var lista = $(lista)
    var new_lista = []
    for (let i = 0; i < lista.length; i++) {
        new_lista.push(lista[i] ** 2)
    }
    return new_lista
}

pierwiastek = function (lista) {
    var lista = $(lista)
    var new_lista = []
    for (let i = 0; i < lista.length; i++) {
        new_lista.push(lista[i] ** 0.5)
    }
    return new_lista
}

balistyczna = function (v0, theta) {
    var dt = 0.01;
    var g = 9.81;
    var alpha = 0.05;
    var v0 = parseFloat($(v0).val());
    var theta = parseFloat($(theta).val());
    $('#ig').text(`${g.toFixed(2)}`);
    $('#ialpha').text(`${alpha.toFixed(2)}`);
    $('#ithete').text(`${theta.toFixed(2)}`);
    $('#iv0').text(`${v0.toFixed(2)}`);
    var X = [0., dt * v0 * Math.cos(theta)];
    var Y = [0., dt * v0 * Math.sin(theta)];
    while (Y[Y.length - 1] >= 0) {
        X.push(((2 + alpha * dt) * X[X.length - 1] - X[X.length - 2]) / (1 + alpha * dt))
        Y.push(((2 + alpha * dt) * Y[Y.length - 1] - Y[Y.length - 2] - g * dt ** 2) / (1 + alpha * dt))

    }
    ;
    var t = [];
    for (let i = 0; i < X.length; i++) {
        t.push(dt * i)
    }
    ;
    var X1 = X.slice();
    var X2 = X.slice();
    var Y1 = Y.slice();
    var Y2 = Y.slice();
    X1.shift();
    X2.pop();
    Y1.shift()
    Y2.pop();
    ;
    var V = dzielenie(pierwiastek(dodawanie(potegowanie(odejmowanie(X1, X2)), potegowanie(odejmowanie(Y1, Y2)))), dt);
    V.push(0);

    $('#it').text(`${(dt * X.length).toFixed(2)}`);

    var baner_h = 27;
    var trace0 = {
        x: X,
        y: Y,
        mode: 'lines',
        type: 'scatter'
    };

    var data = [trace0];
    var layout = {
        title: {
            text: 'Krzywa balistyczna (tor ruchu pocisku)',
            font: {
                color: '#d3d3d3',
            }
        },
        xaxis: {
            title: {
                text: 'odległość [m]',
                font: {
                    color: '#d3d3d3',
                }
            },
            gridcolor: '#d3d3d3',
            zerolinecolor: '#d3d3d3',
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },
        },
        yaxis: {
            title: {
                text: 'wysokość [m]',
                font: {
                    color: '#d3d3d3',
                }
            },
            gridcolor: '#d3d3d3',
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },
        },
        height: (window.innerHeight / 3) - baner_h,
        margin: {'t': 35},
        paper_bgcolor: '#202020',
        plot_bgcolor: '#202020',
    };
    var config = {
        responsive: true,
        displayModeBar: false,
    }

    Plotly.newPlot('balistyczna', data, layout, config);

    var trace1 = {
        x: t,
        y: V,
        mode: 'lines',
        type: 'scatter'
    };

    var data = [trace1];
    var layout = {
        title: {
            text: 'Zależność prędkości od czasu',
            font: {
                color: '#d3d3d3',
            }
        },
        xaxis: {
            title: {
                text: 'czas [s]',
                font: {
                    color: '#d3d3d3',
                }
            },
            gridcolor: '#d3d3d3',
            zerolinecolor: '#d3d3d3',
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },
        },
        yaxis: {
            title: {
                text: 'prędkość [m/s]',
                font: {
                    color: '#d3d3d3',
                }
            },
            gridcolor: '#d3d3d3',
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },
        },
        height: (window.innerHeight / 3) - baner_h,
        margin: {'t': 35},
        paper_bgcolor: '#202020',
        plot_bgcolor: '#202020',
    };
    var config = {
        responsive: true,
        displayModeBar: false,
    }

    Plotly.newPlot('predkosc', data, layout, config);

    var trace2 = {
        x: t,
        y: Y,
        mode: 'lines',
        type: 'scatter'
    };

    var data = [trace2];
    var layout = {
        title: {
            text: 'Zależność wysokości od czasu',
            font: {
                color: '#d3d3d3',
            }
        },
        xaxis: {
            title: {
                text: 'czas [s]',
                font: {
                    color: '#d3d3d3',
                }
            },
            gridcolor: '#d3d3d3',
            zerolinecolor: '#d3d3d3',
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },
        },
        yaxis: {
            title: {
                text: 'wysokość [m]',
                font: {
                    color: '#d3d3d3',
                }
            },
            gridcolor: '#d3d3d3',
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },

        },
        height: (window.innerHeight / 3) - baner_h,
        margin: {'t': 35},
        paper_bgcolor: '#202020',
        plot_bgcolor: '#202020',
    };
    var config = {
        responsive: true,
        displayModeBar: false,
    }

    Plotly.newPlot('wysokosc', data, layout, config);

}

$(document).ready(function () {
    $('#theta').attr('min', Math.PI / 6);
    $('#theta').attr('max', Math.PI / 2);
    $('#theta').attr('value', ((Math.PI / 6) + (Math.PI / 2)) / 2);
    balistyczna($('#v0'), $('#theta'));
    $('input.slider').bind("input", function () {
        $(this).next('input.display').val(parseFloat($(this).val()).toFixed(2));
        balistyczna($('#v0'), $('#theta'));
    }).trigger('input');

    $('input.display').bind("input", function () {
        $(this).prev('input.slider').val($(this).val());
        balistyczna($('#v0'), $('#theta'));
    });
})