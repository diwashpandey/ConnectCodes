const themeSelection = document.querySelector("#theme_selection");
const moon = document.querySelector(".moon");
const sun = document.querySelector(".sun");
const body = document.querySelector("body");
const themeBox = document.querySelector(".theme_box");

const theme = localStorage.getItem("theme");

function setDark() {
  sun.classList.remove("active");
  moon.classList.add("active");
  body.classList.add("darktheme_appplied");
  localStorage.setItem("theme", "dark");
}

function setLight() {
  moon.classList.remove("active");
  sun.classList.add("active");
  body.classList.remove("darktheme_appplied");
  localStorage.setItem("theme", "light");
}

themeBox.addEventListener("click", (e) => {
  if (themeSelection.checked) {
    setDark();
  } else {
    setLight();
  }
});

if (theme != null) {
  if (theme === "dark") {
    themeSelection.checked = true;
    setDark();
  }
}