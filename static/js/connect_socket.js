const roomId = JSON.parse(document.getElementById("room_id").text)
const form = document.querySelector("#form")
const messageBox = document.querySelector(".message_box")
const chats = document.querySelector(".chats")

const url = `ws://127.0.0.1:8000/ws/chat/${roomId}/`

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

    //Data unpacking
    let data = JSON.parse(e.data)
    

    // Creates a list-item to be filled with data and pushed into ul(.chats)
    let li = document.createElement("li")


    // Creates the first div section for list-item
    let div1 = document.createElement("div")
    div1.classList.add("section_1")
    //Creates the img tag for profile picture and puts the source link
    let img = document.createElement("img")
    img.src = `/media/${data.profile_pic}/`
    img.classList.add("profile_pic")

    div1.appendChild(img) //Finally append the well created img element inside the div
    

    // Create the second dic section for list-item
    let div2 = document.createElement("div")
    div2.classList.add("section_2")
    // Create the anchor-point for username along with the username in it
    let a = document.createElement("a")
    a.href = `/profile/?profile=${data.username}` //Will add the link here
    a.innerHTML = `@${data.username}`
    // Create the p tag and add the reveived messege to it.
    let p = document.createElement("p")
    p.innerHTML = data.message


    //Append username and messege inside the section_2 div 
    div2.appendChild(a)
    div2.appendChild(p)


    //Add both sections(div) into the li
    li.appendChild(div1)
    li.appendChild(div2)

    //Finally add the li to the .chats
    chats.appendChild(li)

}

form.addEventListener("submit",(e)=>{
    e.preventDefault()
    socket.send(messageBox.value)
})