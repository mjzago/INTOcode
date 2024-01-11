// log the value of the input on every input
let input = document.getElementById("input");

input.addEventListener("input", () => {
  console.log(input.value);
});

// prevent default on button #submit click
// and change text of #output to „Der Button wurde geklickt!“
let submit = document.getElementById("submit");
submit.addEventListener("click", (event) => {
  event.preventDefault();

  let output = document.getElementById("output");
  output.innerText = "Der Button wurde geklickt!";
});

// log the message „500px erreicht“, when the user scrolls more than 500px
window.addEventListener("scroll", (event) => {
  if (window.scrollY > 500) {
    console.log("500px erreicht");
  }
});