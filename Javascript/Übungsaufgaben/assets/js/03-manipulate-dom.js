 /* // log text content from #headline
/* <script>
document.getElementById("headline").innerHTML = "Hello World!";
</script> */
// Select the element by its ID
// var element = document.getElementById('headline');

// Log the ID of the element
/* console.log(headline);

console.log(headline.textContent); */

// #headline = id="headline"
// .headline = class="headline"

// change the text from the headline to:
// „Cool, sie ist offen! :)“
// Select the element by its ID
// var element = document.getElementById('headline');

// Update the text content
// headline.textContent = '„Cool, sie ist offen! :)“';

// console.log(headline.textContent);
// set value of the input element #input to:
// „Hier steht Text“
// Select the input element by its ID
// var inputElement = document.getElementById('headline');

// Set the value of the input element
// inputElement.value = 'Hier steht Text';

// set the value of the input element #input
// as the innerHtml of the div #output
// Select the input element and the output div element by their IDs
/* var inputElement = document.getElementById('input');
var outputElement = document.getElementById('output');
console.log(inputElement.textContent); */

// Retrieve the value of the input element
/* var inputValue = inputElement.value;
console.log(inputElement.value); */

// Set the inner HTML of the output div element
// outputElement.innerHTML = inputElement.value;


// add the class bg-black to the body
// if there it doesn't got it already


// toggle the class border-red on the input

// multiply the data-number attribute by 3






// Answers from Christian


// log text content from #headline


// #headline = id="headline"
// .headline = class="headline"

// change the text from the headline to:
// „Cool, sie ist offen! :)“
const headlineElement = document.querySelector('#headline');

headlineElement.innerHTML = '„Cool, sie ist offen! :)“';

// set value of the input element #input to:
// „Hier steht Text“
const inputElement = document.querySelector('#input');

inputElement.value ='Hier steht text';


// set the value of the input element #input
// as the innerHtml of the div #output
const outputElement =document.querySelector('#output');
outputElement.innerHTML = inputElement.value

// add the class bg-black to the body
// if there it doesn't got it already
const bodyElement = document.querySelector('body');
console.log('body element', bodyElement);
bodyElement.classList.add('bg-black');

// toggle the class border-red on the input


inputElement.classList.toggle('border-red');

// multiply the data-number attribute by 3
// and update the value in the dom
const num = outputElement.getAttribute('data-number')
const result = num * 3;
outputElement.setAttribute('data-number',result)

// outputElement.dataset.number *= 3;