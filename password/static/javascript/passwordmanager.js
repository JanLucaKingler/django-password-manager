function togglePassword(id) {
    let passwordElement = document.getElementById("password-" + id);
    if (passwordElement.style.display === "none") {
        passwordElement.style.display = "inline";
    } else {
        passwordElement.style.display = "none";
    }
}

function togglePasswordForm() {
    let form = document.getElementById("password-form");
    form.style.display = form.style.display === "none" ? "block" : "none";
}
