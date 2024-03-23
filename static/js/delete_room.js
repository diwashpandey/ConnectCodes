const deleteButtonForms = document.querySelectorAll(".delete_button_form");
// This will select all the delete buttons if there is any


// Using for loop to apply the event listner for each delete button
for (let deleteButtonForm of deleteButtonForms) {
    
  // Applying the event listner for each delete button
  deleteButtonForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    // getting the url from the target/element of the event
    let url = e.target.getAttribute("data-url");

    // getting the csrf token from the first child of the target/element of the event 
    let CSRFToken = e.target[0].value; 

    let option = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFTOKEN": CSRFToken,
      },
    };

    let data = await fetch(url, option);
    let response = await data.json()

    // if server sends the success=ture in the response
    if (response.success) {
      // Deleting the data from the html if server sends the success result
      e.target.parentElement.parentElement.remove()
    }
    else{
        alert("Sorry, couldn't delete the room")
    }
  });
}
