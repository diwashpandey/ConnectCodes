const url = "ws://127.0.0.1:8000/ws/chat/diwash/"
const socket = new WebSocket(url)

// It's just making and overlay for now... main work will be done later...

console.log("Running..")

socket.onopen = (e)=>{
    console.log("Connection established with server...")
}

socket.onclose=(e)=>{
    console.log("Connestion lost with server...")
}

socket.onmessage=(e)=>{
    console.log("Received messege from the server")
}