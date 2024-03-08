const commitForm = document.querySelector(".form");
const commitBtn = document.querySelector(".commit_button")

const socket = new WebSocket("ws://127.0.0.1:8000/ws/account/commit/");

socket.onopen=()=>{
    console.log("Connection established with server Websocket...")
}

socket.onmessage=(e)=>{
    console.log("Message received from the server", e)
    data = JSON.parse(e.data)
    console.log(data)
    if (data.new_commit == "Unfollow"){
        commitBtn.style.backgroundColor =  "var(--button-background)"
        commitBtn.innerHTML = data.new_commit
        commitBtn.value = `${data.new_commit} ${data.username}`
    }
    else if(data.new_commit == "Follow"){
        commitBtn.style.backgroundColor = "var(--button-background)"
        commitBtn.innerHTML = data.new_commit
        commitBtn.value = `${data.new_commit} ${data.username}`
    }
    else{
        alert("Sorry! Someting error happend!")
    }
}

commitForm.addEventListener("submit", (e)=>{
    commitBtn.style.backgroundColor = "grey"
    e.preventDefault()
    let commits = commitBtn.value
    commits = commits.split(" ")

    let commit = JSON.stringify(
        {
            "username":commits[1],
            "commit":commits[0]
        })
    socket.send(commit)

});


