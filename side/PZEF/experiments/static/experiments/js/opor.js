update_path = function (nL, nA, nro) {
    var nL = parseFloat($(nL).val());
    var nA = parseFloat($(nA).val());
    var nro = parseFloat($(nro).val());

    var L = nL + 5;
    var A = (nA + 1) * 17.5;
    var ro = nro;

    var s_x = 400;
    var s_y = 300;
    var o_path;
    var t_path;
    var c;

    var r = 200;
    var g = parseInt(255 - 255 * ro);
    var b = 0;

    var res = nro * nL / nA;

    o_path = `M ${s_x - L} ${s_y - A} L ${s_x + L} ${s_y - A} A 10 5 90 0 1 ${s_x + L} ${s_y + A} L ${s_x - L} ${s_y + A} A 10 5 90 0 1 ${s_x - L} ${s_y - A} Z`;
    t_path = `M ${s_x - L} ${s_y + A} A 10 5 90 0 1 ${s_x - L} ${s_y - A} A 10 5 90 0 1 ${s_x - L} ${s_y + A} Z`;
    c = `#${r.toString(16)}${g.toString(16)}${b}${b}`;
    $('#o_path').attr('d', o_path).css({fill: c});
    $('#t_path').attr('d', t_path).css({fill: c});
    $('.R').css({font: `italic ${200 * (ro * L) / A}px serif`});
    $('.ro').css({font: `italic ${ro * 200}px serif`});
    $('.L').css({font: `italic ${L}px serif`});
    $('.A').css({font: `italic ${A}px serif`});
    $('#num').text(res.toFixed(2));

}

$(document).ready(function () {
    update_path('#L_input', '#A_input', '#ro_input');


    $('input.slider').bind("input", function () {
        $(this).next('input.display').val($(this).val());
        update_path('#L_input', '#A_input', '#ro_input');
    }).trigger('input');

    $('input.display').bind("input", function () {
        $(this).prev('input.slider').val($(this).val());
        update_path('#L_input', '#A_input', '#ro_input');
    });

});