/**
 * CSS-ANIMATIONS
 * Toggle the class "hidden" from the element with the id "menu", when the user clicks on the element with the id "menu-btn"
 * 
*/

const menuElement = document.querySelector('#menu')
const menuButtonElement = document.querySelector('#menu-btn')

menuButtonElement.addEventListener('click', function() {
  menuElement.classList.toggle('hidden')
})
