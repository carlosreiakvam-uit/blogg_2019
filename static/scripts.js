// Denne koden er ikke i bruk. Kun laget for testing av JS

// document.getElementById("jsTest").onclick = testy();
// document.getElementById("jsTest").style.backgroundColor = "red";
document.getElementById("jsTest").addEventListener("click", testy)
document.getElementById("navLink").addEventListener("click", lastClicked)


function lastClicked(event) {
    // event.preventDefault();
    // document.getElementById("navLink").style.backgroundColor = "ghostwhite";
    // document.getElementById("navLink").style.color = "black";
    // window.location = this.href;
}

function testy(event) {
    document.getElementById("jsTest").style.backgroundColor = "red";
}