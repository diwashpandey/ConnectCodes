const photoUpload = document.getElementById("photo_upload")
const photo = document.querySelector(".content__avatar>img")

console.log("hello")

photoUpload.addEventListener("change", (e)=>{
    const file = photoUpload.files[0]
    src = URL.createObjectURL(file)
    photo.src = src
})