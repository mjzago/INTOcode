/**
 * SCROLL TO TOP BUTTON
 * 1. add the class "visible" to the element with the id "return-to-top", when the user scrolled at least the window height
 * 2. when the user clicks the button, scroll the page all the way up to the start
 * 
 */

/* 
const returnToTopElement = document.querySelector('#return-to-top')
function checkIfShowScrollToTop() {
    if (window.innerHeight < window.scrollY) {
        returnToTopElement.classList.add('visible')
    } else {
        returnToTopElement.classList.remove('visible')
    }
}

window.addEventListener('scroll', checkIfShowScrollToTop)
checkIfShowScrollToTop()
*/


const returnToTopElement = document.querySelector('#return-to-top')
window.addEventListener('scroll', function() {
  if (window.innerHeight < window.scrollY) {
      returnToTopElement.classList.add('visible')
  } else {
      returnToTopElement.classList.remove('visible')
  }
})