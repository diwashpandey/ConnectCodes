const commitForm = document.querySelector(".form");
const commitBtn = document.querySelector(".commit_button")

const socket = new WebSocket("ws://127.0.0.1:8000/ws/account/commit/");

socket.onopen=()=>{
    console.log("Connection established with server Websocket...")
}

socket.onmessage=(e)=>{
    console.log("Message received from the server")
}

commitForm.addEventListener("submit", (e)=>{
    e.preventDefault()
    let commits = commitBtn.value
    commits = commits.split(" ")
    let commit = JSON.stringify(
        {
            "username":commits[0],
            "commit":commits[1]
        })
    socket.send(commit)
});


