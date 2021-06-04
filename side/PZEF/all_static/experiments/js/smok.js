function gen_smok(n, s = [nj.array([0, 0]), nj.array([1, 0])]) {
    const translate_move = {
        'array([ 1, 0])': nj.array([0, 1]), 'array([-1, 0])': nj.array([0, -1]),
        'array([ 0, 1])': nj.array([-1, 0]), 'array([ 0,-1])': nj.array([1, 0])
    }
    let smok = s
    if (smok.length < 2 ** n + 1) {
        while (smok.length < 2 ** n + 1) {
            let new_p = [smok[smok.length - 1].add(translate_move[(smok[smok.length - 1].subtract(smok[smok.length - 2])).toString()])]
            for (let j = 2; j < smok.length; j++) {
                new_p.push(new_p[new_p.length - 1].add(translate_move[(smok[smok.length - j].subtract(smok[smok.length - j - 1])).toString()]))
            }
            smok = smok.concat(new_p)
        }
    } else if (smok.length > 2 ** n + 1) {
        while (smok.length !== 2 ** n + 1) {
            smok.pop()
        }
    }
    return smok
}

function get_xy(s) {
    let x = []
    let y = []
    for (let i = 0; i < s.length; i++) {
        let p = s[i].tolist()
        x.push(p[0])
        y.push(p[1])
    }
    return [x, y]
}

function plot_smok(xy) {
    var trace0 = {
        x: xy[0],
        y: xy[1],
        mode: 'lines',
        type: 'scatter',
        line: {
            width: 5,
            color: '#04AA6D'
        }
    };

    var data = [trace0];
    var layout = {
        hovermode: 'closest',
        title: {
            text: '',
            font: {
                color: '#d3d3d3',
            }
        },
        xaxis: {
            title: {
                text: '',
                font: {
                    color: '#d3d3d3',
                }
            },
            autorange: true,
            showgrid: false,
            zeroline: false,
            showline: false,
            showticklabels: false,
            gridwidth: 0.5,
            zerolinecolor: '#d3d3d3',
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },
        },
        yaxis: {
            title: {
                text: '',
                font: {
                    color: '#d3d3d3',
                }
            },
            autorange: true,
            showgrid: false,
            zeroline: false,
            showline: false,
            showticklabels: false,
            scaleanchor: "x",
            gridwidth: 0.5,
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },
        },
        showlegend: false,
        height: window.innerHeight - 100,
        margin: {'t': 35},
        paper_bgcolor: '#202020',
        plot_bgcolor: '#202020',
    };
    var config = {
        responsive: true,
    }

    Plotly.newPlot('smok', data, layout, config);
}

function anim_plot(t_xy, p_xy, t, p) {
    let f1
    let f2
    if (p < t) {
        let new_x = [...t_xy[0]]
        let new_y = [...t_xy[1]]
        let temp_x = new_x.slice(0, new_x.length / 2 + 1).concat(new_x.slice(0, new_x.length / 2).reverse())
        let temp_y = new_y.slice(0, new_y.length / 2 + 1).concat(new_y.slice(0, new_y.length / 2).reverse())
        f1 = [{x: temp_x, y: temp_y}]
        f2 = [{x: new_x, y: new_y}]

    } else {
        let new_x = [...p_xy[0]]
        let new_y = [...p_xy[1]]
        let temp_x = new_x.slice(0, new_x.length / 2 + 1).concat(new_x.slice(0, new_x.length / 2).reverse())
        let temp_y = new_y.slice(0, new_y.length / 2 + 1).concat(new_y.slice(0, new_y.length / 2).reverse())
        f1 = [{x: new_x, y: new_y}]
        f2 = [{x: temp_x, y: temp_y}]

    }
    Plotly.addFrames('smok', [
        {
            data: f1,
            name: 'frame1',
            layout: {
                xaxis: {autorange: true,},
                yaxis: {autorange: true,}
            }
        }, {
            data: f2,
            name: 'frame2',
            layout: {
                xaxis: {autorange: true,},
                yaxis: {autorange: true,}
            }
        }
    ]);
    Plotly.animate('smok', ['frame1', 'frame2'], {
        frame: [
            {duration: 0},
            {duration: 500},
        ],
        transition: [
            {duration: 8000, easing: 'elastic-in'},
            {duration: 1000, easing: 'cubic-in'},
        ],
        mode: 'afterall',
        layout: {
            xaxis: {autorange: true,},
            yaxis: {autorange: true,}
        }
    })
}

var itt = 0

function rl() {

    setTimeout(function () {
        Plotly.relayout('smok', {
            'xaxis.autorange': true,
            'yaxis.autorange': true,
            'yaxix.scaleanchor': 'x',
        })
        itt++
        if (itt < 50) {
            rl()
        }
    }, 250)
}

$(document).ready(function () {
    var s = gen_smok(0)
    var p_xy = get_xy(s)
    var p_value = 0
    plot_smok(p_xy)
    $('input.slider').bind("input", function () {
        let t_value = parseInt($(this).val())
        s = gen_smok(t_value, s)
        let t_xy = get_xy(s)
        anim_plot(t_xy, p_xy, t_value, p_value)
        setTimeout(rl, 500);
        p_value = t_value
        p_xy = t_xy
    }).trigger('input');
})