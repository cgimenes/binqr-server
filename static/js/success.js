var fallbackEnabled = false;

function gifFallback() {
    var qrcodes = document.getElementById("qrcodes");
    var gif = document.getElementById("gif");
    var buttonText = document.getElementById("fallback-button-text");
    var buttonIcon = document.getElementById("fallback-button-icon");

    fallbackEnabled = !fallbackEnabled;
    if (fallbackEnabled) {
        buttonText.innerText = "Modo normal";
        gif.classList.add("is-hidden");
        qrcodes.classList.remove("is-hidden");
        buttonIcon.classList.remove("fa-thumbs-down");
        buttonIcon.classList.add("fa-thumbs-up");
    } else {
        buttonText.innerText = "Modo manual";
        gif.classList.remove("is-hidden");
        qrcodes.classList.add("is-hidden");
        buttonIcon.classList.remove("fa-thumbs-up");
        buttonIcon.classList.add("fa-thumbs-down");
    }
}
