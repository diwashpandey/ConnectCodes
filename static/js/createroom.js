const firstBox = document.querySelector(".topics_selection");
const secondBox = document.querySelector(".subtopics");

firstBox.addEventListener("change", (e) => {
  secondBox.innerHTML = "";
  var selectedOption = firstBox.value;

  var secondOptions = [];
  if (selectedOption === "Python") {
    secondOptions = ["OOPs", "Functions", "Variables"];
  } else if (selectedOption === "JavaScript") {
    secondOptions = ["OOPs", "Functions", "Variables"];
  } else if (selectedOption === "WebDevelopment") {
    secondOptions = ["Front-end", "Back-end", "Full-stack"];
  } else if (selectedOption === "DSA") {
    secondOptions = ["dsa"];
  }

  secondOptions.forEach((option) => {
    var optionElement = document.createElement("option");
    optionElement.textContent = option;
    optionElement.value = option;
    secondBox.appendChild(optionElement);
  });
});
