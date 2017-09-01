var fallbackEnabled = false;

function gifFallback() {
    var qrcodes = document.getElementsByClassName('qrcode');
    var gif = document.getElementsByClassName('gif');
    var button = document.getElementById('fallbackButton');

    fallbackEnabled = !fallbackEnabled;
    if (fallbackEnabled) {
        button.innerText = 'Modo normal';
    } else {
        button.innerText = 'Modo manual';
    }

    gif[0].style.display = fallbackEnabled ? 'none' : 'block';
    for (var i = qrcodes.length - 1; i >= 0; i--)
    {
        qrcodes[i].style.display = fallbackEnabled ? 'block' : 'none';
    }
}
