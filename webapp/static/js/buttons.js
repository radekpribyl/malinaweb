$(document).ready(function () {
    var malina = io.connect('http://' + document.domain + ':' + location.port + '/malina');

    malina.on('speed_change', function (data) {
        console.log(data);
        $("#srychlost").html(data.rychlost);
    })

    malina.on('sensors', function (data) {
        console.log(data);
        $("#" + data.sensor).html(data.value);
    })

    $("#bdopredu").click(function () {
        malina.emit('steering', { akce: 'dopredu' });
    })
    $("#bstop").click(function () {
        malina.emit('steering', { akce: 'stop' });
    })

    $("#bdozadu").click(function () {
        malina.emit('steering', { akce: 'dozadu' });
    })

    $("#brotujedoleva").click(function () {
        malina.emit('steering', { akce: 'rotujvlevo' });
    })

    $("#brotujdoprava").click(function () {
        malina.emit('steering', { akce: 'rotujvpravo' });
    })

    $("#bvpredvlevo").click(function () {
        malina.emit('steering', { akce: 'zatocvpredvlevo' });
    })

    $("#bvredvpravo").click(function () {
        malina.emit('steering', { akce: 'zatocvpredvpravo' });
    })

    $("#bvzadvlevo").click(function () {
        malina.emit('steering', { akce: 'zatocvzadvlevo' });
    })

    $("#bvzadvpravo").click(function () {
        malina.emit('steering', { akce: 'zatocvzadvpravo' });
    })

    $("#bzrychli").click(function () {
        malina.emit('rychlost', { akce: 'zrychli' }, function(data) {
            console.log(data);
        });
    })

    $("#bzpomal").click(function () {
        malina.emit('rychlost', { akce: 'zpomal' });
    })
})