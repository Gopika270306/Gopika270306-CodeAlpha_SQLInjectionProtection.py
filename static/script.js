// =============================
// SQLGuard JavaScript
// =============================

// Display welcome message
window.onload = function () {
    console.log("SQLGuard System Loaded");
};


// -----------------------------
// Confirm Logout
// -----------------------------

function confirmLogout() {

    let result = confirm(
        "Are you sure you want to logout?"
    );

    if (result) {
        window.location.href = "/logout";
    }

}


// -----------------------------
// SQL Injection Input Checker
// -----------------------------

function checkInput() {

    let input = document.getElementById(
        "attackInput"
    );

    if (input == null) {
        return true;
    }

    let value = input.value.toLowerCase();

    let patterns = [

        "' or '1'='1",
        "union select",
        "drop table",
        "delete from",
        "insert into",
        "update ",
        "xp_cmdshell",
        "exec",
        "--",
        "#"

    ];

    for (let i = 0; i < patterns.length; i++) {

        if (value.includes(patterns[i])) {

            alert(
                "⚠ Potential SQL Injection Pattern Detected!"
            );

            return true;

        }

    }

    alert(
        "✓ Input appears safe."
    );

    return true;

}


// -----------------------------
// Card Hover Animation
// -----------------------------

document.addEventListener(
    "DOMContentLoaded",

    function () {

        let cards =
            document.querySelectorAll(".card");

        cards.forEach(function (card) {

            card.addEventListener(
                "mouseover",

                function () {

                    card.style.transform =
                        "scale(1.05)";

                    card.style.transition =
                        "0.3s";

                }

            );

            card.addEventListener(
                "mouseout",

                function () {

                    card.style.transform =
                        "scale(1)";

                }

            );

        });

    }

);


// -----------------------------
// Live Clock
// -----------------------------

function updateClock() {

    let clock =
        document.getElementById("clock");

    if (clock != null) {

        let now = new Date();

        clock.innerHTML =
            now.toLocaleString();

    }

}

setInterval(
    updateClock,
    1000
);


// -----------------------------
// Dashboard Greeting
// -----------------------------

function greeting() {

    let hour =
        new Date().getHours();

    let text = "";

    if (hour < 12) {

        text = "Good Morning";

    }

    else if (hour < 18) {

        text = "Good Afternoon";

    }

    else {

        text = "Good Evening";

    }

    let greet =
        document.getElementById(
            "greeting"
        );

    if (greet != null) {

        greet.innerHTML =
            text + ", Welcome to SQLGuard";

    }

}

greeting();
