const commitBtn = document.querySelector(".commit_button");

const socket = new WebSocket("ws://127.0.0.1:8000/ws/account/commit/");

socket.onopen=()=>{
    console.log("Connection established with server Websocket...")
}

socket.onmessage=(e)=>{
    console.log("Message received from the server")
}

commitBtn.addEventListener("click", (e)=>{
    commitBtn.style.color="Black"    
});