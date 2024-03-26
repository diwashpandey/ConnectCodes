const registrationForm = document.getElementById("registration_form");
const CSRFTOKEN = document.querySelector(
  "#registration_form>input:first-child"
).value;
const sumbitURL = registrationForm.getAttribute("data-url");
const registerContainer = document.querySelector(".register-container");
const messageBox = document.querySelector(".messages");
console.log("DIwash");

registrationForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const nameInput = document.getElementById("name_input");
  const newUsername = document.getElementById("new_username");
  const newPassword = document.getElementById("new_password");
  const confirmPassword = document.getElementById("confirm_password");

  const options = {
    method: "POST",
    headers: {
      "X-CSRFTOKEN": CSRFTOKEN,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      new_username: newUsername.value,
      new_password: newPassword.value,
      confirm_password: confirmPassword.value,
      full_name: nameInput.value,
    }),
  };

  let response = await fetch(sumbitURL, options);
  var data = await response.json();

  let li = document.createElement("li");

  if (data.success == true) {
    li.classList.add("center", "success");
    li.innerHTML = data.message;
    window.location.href = data["redirect-url"];
  } else {
    li.classList.add("center", "error");
    li.innerHTML = data.message;
  }

  messageBox.innerHTML = "";
  messageBox.appendChild(li);
  console.log(messageBox.innerHTML);
});
