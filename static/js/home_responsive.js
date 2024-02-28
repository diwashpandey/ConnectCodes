topicsBox = document.querySelector(".topics_box")
revealer = document.querySelector(".revealer")

function revealBox() {
    revealer.classList.toggle("reveal_active")
    topicsBox.classList.toggle("topics_box_opened")
}