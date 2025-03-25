/**
 *  Schaltet die Sichtbarkeit eines Passworts ein oder aus.
 *  Diese Funktion zeigt das Passwort an, wenn es derzeit verborgen ist, und verbirgt es, wenn es angezeigt wird.
 *  Sie ändert den `display`-Stil des Passwort-Elements.
 *
 *  @param id  Die eindeutige ID des Passwort-Elements, das angezeigt oder verborgen werden soll.
 */
function togglePassword(id) {
    let passwordElement = document.getElementById("password-" + id);
    if (passwordElement.style.display === "none") {
        passwordElement.style.display = "inline";
    } else {
        passwordElement.style.display = "none";
    }
}

/**
 * Schaltet die Sichtbarkeit eines Formulars ein oder aus.
 * Diese Funktion zeigt oder verbirgt das Formular, je nachdem, ob es derzeit sichtbar oder verborgen ist.
 * Sie ändert den `display`-Stil des Formulars.
 */
function togglePasswordForm() {
    let form = document.getElementById("password-form");
    form.style.display = form.style.display === "none" ? "block" : "none";
}
