function generateUsername() {
    let addNumber = document.getElementById("addNumber").checked;
    let addSpecial = document.getElementById("addSpecial").checked;

    fetch("/generate", {
        method: "POST",
        body: JSON.stringify({ addNumber: addNumber, addSpecial: addSpecial }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        let resultElement = document.getElementById("result");
        resultElement.innerText = "⭐ " + data.username + " ⭐";
        resultElement.classList.add("show");

        // Remove animation class after 1 second so it can reapply next time
        setTimeout(() => {
            resultElement.classList.remove("show");
        }, 1000);
    })
    .catch(error => console.error("Error:", error));
}
