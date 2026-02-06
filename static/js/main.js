let btn = document.querySelector("button");

btn.addEventListener("click", async () => {
    let input = document.querySelector("#input-text").value;

    let request = await fetch("/api/test", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: input
        })
    });

    let response = await request.json();
    document.querySelector("p").innerHTML = response.reply;
})