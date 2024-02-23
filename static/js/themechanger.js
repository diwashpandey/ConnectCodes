themeSelection = document.querySelector("#theme_selection")
moon = document.querySelector(".moon")
sun = document.querySelector(".sun")
body = document.querySelector('body')
themeBox = document.querySelector('.theme_box')

themeBox.addEventListener('click', (e)=>{
    if (themeSelection.checked){
        sun.classList.remove('active')
        moon.classList.add('active')
        body.classList.add('darktheme_appplied')
    }
    else{
        moon.classList.remove('active')
        sun.classList.add('active')
        body.classList.remove('darktheme_appplied')
    }
})

