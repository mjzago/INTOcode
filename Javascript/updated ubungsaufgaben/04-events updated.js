// log the value of the input on every input
const input = document.getElementById('input')

input.addEventListener('input', function inputChange() {
  console.log(input.value)
});

// prevent default on button #submit click
// and change text of #output to „Der Button wurde geklickt!“
document.querySelector('#submit').addEventListener('click', function submit(event) {
  event.preventDefault()

  document.getElementById('output').textContent = 'Der Button wurde geklickt!'
});

// log the message „500px erreicht“, when the user scrolls more than 500px
window.addEventListener('scroll', function windowScroll(event) {
  if (window.scrollY >= 500) {
    console.log('500px erreicht')
  }
});



/* 
Example:
  The headline text will be updated by the input value if the user is typing
*/

const inputElement = document.querySelector('#input')
const headlineElement = document.querySelector('#headline')

function onInput(event) {
  console.log('Event', event.target.value)
  headlineElement.innerText = event.target.value
}

inputElement.addEventListener('input', onInput)


/* 
Possible events:
- input
- change
- click
- mousedown
- mouseup
- mousemove
- keydown
- keyup
…

*/



/* 
Example:
  The event "mousedown" is triggered if the user presses the mouse button down
  The event "mousemove" is triggered if the user moves the mouse over the element
  The event "mouseup" is triggered if the user releases the mouse button
*/

document.body.addEventListener('mousedown', function(event) {
  console.log('Mouse down', event)
})

document.body.addEventListener('mousemove', function(event) {
  console.log('Mouse move', event.clientX, event.clientY)
  const element = document.querySelector('#input')
  // const attributeValue = 'position: fixed; top: '+ event.clientY +'px; left: '+ event.clientX +'px'
  const attributeValue = `
    position: fixed;
    top: ${ event.clientY }px;
    left: ${ event.clientX }px
  `
  element.setAttribute('style', attributeValue)
})

document.body.addEventListener('mouseup', function(event) {
  console.log('Mouse up', event)
})