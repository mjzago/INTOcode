// log the value of the input on every input

// prevent default on button #submit click
// and change text of #output to „Der Button wurde geklickt!“

// log the message „500px erreicht“, when the user scrolls more than 500px

// const inputElement = document.getElementById('input')
const inputElement = document.querySelector('#input')
const headlineElement = document.querySelector('#headline')

// const inputElement = document.getElementById('input')

function onInput(event){
    console.log('Event', event.target.value)
    headlineElement.innerText = event.target.value
}

inputElement.addEventListener('click', onInput)
// document.body.addEventListener('mouseup',function(event){
//     console.log('mouseup', event)
// })
// document.body.addEventListener('keydown',function(event){
//     console.log('keydown', event)
// })
// document.body.addEventListener('mousedown',function(event){
//     console.log('mousedown', event)
// })
document.body.addEventListener('mousemove',function(event){
    console.log('mousemove', event)
})
/* 
-input
-change
-click
mousedown
-mouseup
-mousedown 
*/

u