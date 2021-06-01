function zeros(dim) {
    let new_vec = []
    for (let i = 0; i < dim; i++) {
        new_vec.push(0)
    }
    return new Vector(new_vec)
}

function calc_mas_center(l_body) {
    let sum_m = 0
    let sum_mpos = zeros(l_body[0].f.dim)
    for (let i = 0; i < l_body.length; i++) {
        sum_m = sum_m + l_body[i].m
        sum_mpos = sum_mpos.add(l_body[i].pos[l_body[i].pos.length - 1].mul_as_num(l_body[i].m))
    }
    return sum_mpos.div_as_num(sum_m)
}

function correction_v(l_body) {
    let sum_m = 0
    let sum_mv = zeros(l_body[0].f.dim)
    for (let i = 0; i < l_body.length; i++) {
        sum_m = sum_m + l_body[i].m
        sum_mv = sum_mv.add(l_body[i].v[l_body[i].v.length - 1].mul_as_num(l_body[i].m))
    }
    for (let i = 0; i < l_body.length; i++) {
        l_body[i].v[l_body[i].v.length - 1] = l_body[i].v[l_body[i].v.length - 1].sub(sum_mv.div_as_num(sum_m))
    }
}

function calc_versor(b1, b2) {
    return (b1.pos[b1.pos.length - 1].sub(b2.pos[b2.pos.length - 1])).div_as_num(calc_distance(b1, b2))
}

function calc_distance(b1, b2) {
    return Math.sqrt(b1.pos[b1.pos.length - 1].sub(b2.pos[b2.pos.length - 1]).len ** 2 + 0.1 ** 2)
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function gen_body(N) {
    let l = []
    let m_min = parseFloat($('#m_min').val())
    let m_max = parseFloat($('#m_max').val())
    let xy_min = parseFloat($('#p_min').val())
    let xy_max = parseFloat($('#p_max').val())
    let v_min = parseFloat($('#v_min').val())
    let v_max = parseFloat($('#v_max').val())
    for (let i = 0; i < N; i++) {
        let m = getRandomInt(m_min, m_max)
        let p_x = getRandomInt(xy_min, xy_max)
        let p_y = getRandomInt(xy_min, xy_max)
        let v_x = getRandomInt(v_min, v_max)
        let v_y = getRandomInt(v_min, v_max)
        let color = '#' + Math.floor(Math.random() * 16777215).toString(16)
        l.push(new Body(m, new Vector([p_x, p_y]), new Vector([v_x, v_y]), 6, color))
    }
    return l
}

function body_plot(list_body) {
    let x = [];
    let marker_x = [];
    let y = [];
    let marker_y = [];
    for (let i = 0; i < list_body.length; i++) {
        x.push([])
        marker_x.push([])
        y.push([])
        marker_y.push([])
    }

    for (let i = 0; i < list_body.length; i++) {
        x[i].push(list_body[i].pos[0].coordinate[0])
        marker_x[i].push(list_body[i].pos[list_body[i].pos.length - 1].coordinate[0])
        y[i].push(list_body[i].pos[0].coordinate[1])
        marker_y[i].push(list_body[i].pos[list_body[i].pos.length - 1].coordinate[1])
    }

    let plot_body = []
    for (let i = 0; i < list_body.length; i++) {
        plot_body.push({
            x: x[i],
            y: y[i],
            mode: 'line',
            line: {
                color: list_body[i].color
            }
        })
        plot_body.push({
            x: marker_x[i],
            y: marker_y[i],
            mode: 'markers',
            marker: {
                color: list_body[i].color,
                size: list_body[i].r,
            }
        })
    }
    return [plot_body, x, y]
}

function next_step(s, re_x, re_y) {
    let x = re_x
    let y = re_y
    let marker_x
    let marker_y
    s.run(1)
    if ($('#trajectory')[0].checked === false) {
        x = []
        y = []
        for (let i = 0; i < s.l_body.length; i++) {
            x.push([])
            y.push([])
        }
    }
    marker_x = []
    marker_y = []
    for (let i = 0; i < s.l_body.length; i++) {
        marker_x.push([])
        marker_y.push([])
    }
    for (let i = 0; i < s.l_body.length; i++) {
        x[i].push(s.l_body[i].pos[s.l_body[i].pos.length - 1].coordinate[0])
        marker_x[i].push(s.l_body[i].pos[s.l_body[i].pos.length - 1].coordinate[0])
        y[i].push(s.l_body[i].pos[s.l_body[i].pos.length - 1].coordinate[1])
        marker_y[i].push(s.l_body[i].pos[s.l_body[i].pos.length - 1].coordinate[1])

        if (x[i].length > 1000) {
            x[i].shift()
            y[i].shift()
        }
    }
    let compute_plot_body = []
    for (let i = 0; i < s.l_body.length; i++) {
        compute_plot_body.push({
            x: x[i],
            y: y[i],
        })
        compute_plot_body.push({
            x: marker_x[i],
            y: marker_y[i],
        })
    }
    return [compute_plot_body, x, y]
}

function update_plot() {
    let compute_plot_body = next_step();
    Plotly.animate('myDiv', {
        data: compute_plot_body
    }, {
        transition: {
            duration: 0
        },
        frame: {
            duration: 0,
            redraw: false
        }
    });
    requestAnimationFrame(update_plot);
}

class Vector {
    constructor(coordinate) {
        this.coordinate = coordinate;
    }

    get len() {
        let sum = 0
        for (let i = 0; i < this.dim; i++) {
            sum += this.coordinate[i] ** 2
        }
        return Math.sqrt(sum)
    }

    get dim() {
        return this.coordinate.length
    }

    sub(other) {
        let new_vec = []
        for (let i = 0; i < this.dim; i++) {
            new_vec.push(this.coordinate[i] - other.coordinate[i])
        }
        return new Vector(new_vec)
    }

    add(other) {
        let new_vec = []
        for (let i = 0; i < this.dim; i++) {
            new_vec.push(this.coordinate[i] + other.coordinate[i])
        }
        return new Vector(new_vec)
    }

    mul_as_num(num) {
        let new_vec = []
        for (let i = 0; i < this.dim; i++) {
            new_vec.push(this.coordinate[i] * num)
        }
        return new Vector(new_vec)
    }

    div_as_num(num) {
        let new_vec = []
        for (let i = 0; i < this.dim; i++) {
            new_vec.push(this.coordinate[i] / num)
        }
        return new Vector(new_vec)
    }
}

class Body {
    constructor(m, pos, v, r = 6, c = 'blue') {
        this.m = m;
        this.r = r;
        this.pos = [pos,];
        this.v = [v,];
        this.f = zeros(pos.dim)
        this.color = c
    }
}

class Simulation {
    constructor(l_body, dt, G) {
        this.l_body = l_body
        this.dt = dt
        this.G = G
        this.dimension = l_body[0].f.dim
        this.mc = [calc_mas_center(l_body)]
        correction_v(l_body)
        this.start = false
    }

    leap_frog() {
        for (let i = 0; i < this.l_body.length; i++) {
            this.l_body[i].v.push(this.l_body[i].v[this.l_body[i].v.length - 1].add(this.l_body[i].f.mul_as_num(this.dt).div_as_num(this.l_body[i].m)))
            this.l_body[i].pos.push(this.l_body[i].pos[this.l_body[i].pos.length - 1].add(this.l_body[i].v[this.l_body[i].v.length - 1].mul_as_num(this.dt)))
        }
    }

    calc_f() {
        for (let i = 0; i < this.l_body.length; i++) {
            let f = zeros(this.dimension)
            for (let j = 0; j < this.l_body.length; j++) {
                if (this.l_body[i] !== this.l_body[j]) {
                    f = f.add(calc_versor(this.l_body[j], this.l_body[i]).mul_as_num(this.G * this.l_body[i].m * this.l_body[j].m / calc_distance(this.l_body[i], this.l_body[j]) ** 2))
                }
            }
            this.l_body[i].f = f
        }
    }

    run(n) {
        for (let i = 0; i < n; i++) {
            this.calc_f()
            this.leap_frog()
            this.mc.push(calc_mas_center(this.l_body))
        }
    }
}

$(document).ready(function () {
    var body1 = new Body(1, new Vector([-2.8, -1.0]), new Vector([0., 0.]), 6, 'red')
    var body2 = new Body(1, new Vector([1.8, -2.5]), new Vector([0., 0.]), 6, 'green')
    var body3 = new Body(1, new Vector([2.0, 2.8]), new Vector([0., 0.]), 6, 'blue')
    var G = 1
    var dt = 0.01
    var list_body = [body1, body2, body3]
    var s = new Simulation(list_body, dt, G);
    var plot_body = body_plot(list_body)
    var re_x = plot_body[1]
    var re_y = plot_body[2]

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
                text: 'x',
                font: {
                    color: '#d3d3d3',
                }
            },
            autorange: true,
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
            autorange: true,
            scaleanchor: "x",
            gridcolor: '#323232',
            gridwidth: 0.5,
            linecolor: '#d3d3d3',
            tickfont: {
                color: 'lightgrey'
            },
        },
        showlegend: false,
        margin: {'t': 35},
        paper_bgcolor: '#202020',
        plot_bgcolor: '#202020',
    }

    Plotly.newPlot('myDiv', plot_body[0], layout)

    $('.ukl').on('change', function () {
        if ($(this).prop('checked')) {
            switch ($(this).attr('id')) {
                case 'szk':
                    $('.castom').hide()
                    var slonce = new Body(1.989 * 10 ** 30, new Vector([0.0, 0.0]), new Vector([0., 0.]), 33, 'yellow');
                    var ziemia = new Body(5.972 * 10 ** 24, new Vector([1.496 * 10 ** 8, 0.0]), new Vector([0., 107.0 * 10 ** 3.95]), 1, 'green');
                    var ksiezyc = new Body(7.347 * 10 ** 22, new Vector([1.496 * 10 ** 8, 3.844 * 10 ** 5]), new Vector([-3.682 * 10 ** 3.95, 107.0 * 10 ** 3.95]), 0.25, 'gray');
                    G = 6.6743e-11;
                    dt = 0.1;
                    list_body = [slonce, ziemia, ksiezyc];
                    s = new Simulation(list_body, dt, G);
                    plot_body = body_plot(list_body)
                    re_x = plot_body[1]
                    re_y = plot_body[2]
                    Plotly.purge('myDiv')
                    Plotly.newPlot('myDiv', plot_body[0], layout)
                    break;

                case 'zk':
                    $('.castom').hide()
                    var planeta = new Body(5.972 * 10 ** 24, new Vector([0.0, 0.0]), new Vector([0., 107.0 * 10 ** 3.95]), 100, 'green');
                    var satelita = new Body(7.347 * 10 ** 22, new Vector([0.0, 3.844 * 10 ** 5]), new Vector([-3.682 * 10 ** 3.95, 107.0 * 10 ** 3.95]), 25, 'gray');
                    G = 6.6743e-11;
                    dt = 0.1;
                    list_body = [planeta, satelita];
                    s = new Simulation(list_body, dt, G);
                    plot_body = body_plot(list_body)
                    re_x = plot_body[1]
                    re_y = plot_body[2]
                    Plotly.purge('myDiv')
                    Plotly.newPlot('myDiv', plot_body[0], layout)
                    break;

                case '3b':
                    $('.castom').hide()
                    var body1 = new Body(1, new Vector([-2.8, -1.0]), new Vector([0., 0.]), 6, 'red')
                    var body2 = new Body(1, new Vector([1.8, -2.5]), new Vector([0., 0.]), 6, 'green')
                    var body3 = new Body(1, new Vector([2.0, 2.8]), new Vector([0., 0.]), 6, 'blue')
                    G = 1
                    dt = 0.01
                    list_body = [body1, body2, body3]
                    s = new Simulation(list_body, dt, G);
                    plot_body = body_plot(list_body)
                    re_x = plot_body[1]
                    re_y = plot_body[2]
                    Plotly.purge('myDiv')
                    Plotly.newPlot('myDiv', plot_body[0], layout)
                    break;

                case 'randomN':
                    $('.castom').show()
                    break;
                default:
                    console.log('pass');
            }
        }
    })

    $('#generuj').on('click', function () {
        G = parseFloat($('#G').val())
        dt = parseFloat($('#dt').val())
        list_body = gen_body(parseInt($('#l_cial').val()))
        s = new Simulation(list_body, dt, G);
        plot_body = body_plot(list_body)
        re_x = plot_body[1]
        re_y = plot_body[2]
        Plotly.purge('myDiv')
        Plotly.newPlot('myDiv', plot_body[0], layout)
    })

    $('#start').on('click', function () {
        function update_plot() {
            let compute_plot_body = next_step(s, re_x, re_y);
            re_x = compute_plot_body[1]
            re_y = compute_plot_body[2]
            Plotly.animate('myDiv', {
                data: compute_plot_body[0]
            }, {
                transition: {
                    duration: 0
                },
                frame: {
                    duration: 0,
                    redraw: false
                }
            });
            if ($('#osie')[0].checked === false) {
                Plotly.relayout('myDiv', {
                    'xaxis.autorange': true,
                    'yaxis.autorange': true,
                    'yaxix.scaleanchor': 'x',
                });
            } else {
                Plotly.relayout('myDiv', {
                    'xaxis.autorange': false,
                    'yaxis.autorange': false,
                });
            }
            Plotly.relayout('myDiv', {})
            if (s.start === false) {
                return 0
            }
            requestAnimationFrame(update_plot);
        }

        if (s.start === false) {
            requestAnimationFrame(update_plot)
            s.start = true
        }
    })
    $('#stop').on('click', function () {
        s.start = false
    })
});
