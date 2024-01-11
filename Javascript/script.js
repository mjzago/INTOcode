// Variablen für Aufgabe 1 & 2

let a = 1;
let b = 3;
let c = 5;
let d = 7;
let e = 9;


// 1. Berechne das Ergebnis

// A: d + a =
// B: d - e =
// C: e % b =
// D: (a + b) - (c * a) =
// E: e / b + c =

console.log('*********************1. Berechne das Ergebnis');
console.log('d + a =', d + a);
console.log('d - e =', d - e);
console.log('e % b =', e % b);
console.log('(a + b) - (c * a) =', (a + b) - (c * a));
console.log('e / b + c =', e / b + c);

// 2. Ergebnis der logischen Operatoren
// A: a > b =
// B: c < a =
// C: c == d - (2 * a) =
// D: e != b + (e / 3) =
// E: (c * 3) >= (b * 5) =


console.log('*********************2. Ergebnis der logischen Operatoren');

console.log('a > b =', a > b);
console.log('c < a =', c < a);
console.log('c == d - (2 * a) =', c == d - (2 * a));
console.log('e != b + (e / 3) =', e != b + (e / 3));
console.log('(c * 3) >= (b * 5) =', (c * 3) >= (b * 5));

// 3. Welchen Wert hat die Variable „visible“ ?

console.log('*********************3. Welchen Wert hat die Variable „visible“ ?');

let visible = false;

window.scrollY = 642;
window.innerHeight = 677;

if (window.scrollY > window.innerHeight) {
    visible = true;
} else {
    visible = false;
}

console.log('A-visible =', visible);

// B
window.scrollY = 768;
window.innerHeight = 768;

if (window.scrollY > window.innerHeight) {
    visible = true;
} else {
    visible = false;
}

console.log('B-visible =', visible);

// C

window.scrollY = 1283;
window.innerHeight = 1024;

if (window.scrollY > window.innerHeight) {
    visible = true;
} else {
    visible = false;
}

console.log('C-visible =', visible);


// 4. Arbeiten mit Arrays
console.log('*********************4. Arbeiten mit Arrays');
// 4.1 Elemente selektieren
console.log('*********************4.1 Elemente selektieren');

let days = [ 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'];

// A: days[3] =
// B: days[7] =
// C: days.indexOf('Samstag') =
// D: days.indexOf('Montag') =
// E: days.indexOf('Sontag') =

console.log("days[3] =", days[3]);
console.log("days[7] =", days[7]);
console.log("days.indexOf('Samstag') =", days.indexOf('Samstag'));
console.log("days.indexOf('Montag') =", days.indexOf('Montag'));
console.log("days.indexOf('Sontag') =", days.indexOf('Sontag'));

// 4.2 Elemente hinzufügen/entfernen
console.log('*********************4.2 Elemente hinzufügen/entfernen')

// A: Wie fügt man "Duck" dem Array hinzu?
console.log('*********************A: Wie fügt man "Duck" dem Array hinzu?');
var animals = [ "Pig", "Goat", "Cow", "Chicken", "Sheep", "Horse"];
console.log(animals)
console.log('animals.add = "Duck"');
animals.add = "Duck";
console.log(animals);


console.log("animals.push('Duck')");
animals.push('Duck');
console.log(animals);

console.log('animals.unshift("Duck");');
animals.unshift("Duck");
console.log(animals);


// B: Wie entfernt man "Sheep" und "Horse" aus dem Array?
console.log('*********************B: Wie entfernt man "Sheep" und "Horse" aus dem Array?')
var animals = [ "Pig", "Goat", "Cow", "Chicken", "Sheep", "Horse"];
console.log(animals);

console.log('animals.splice(5, 1);');
animals.splice(5, 1);
console.log(animals);

var animals = [ "Pig", "Goat", "Cow", "Chicken", "Sheep", "Horse"];
console.log('animals.splice(4, 2);')
animals.splice(4, 2);
console.log(animals);

var animals = [ "Pig", "Goat", "Cow", "Chicken", "Sheep", "Horse"];
console.log('animals.splice(5, 2);')
animals.splice(5, 2);
console.log(animals);

// 5. Arbeiten mit Objekten
console.log('*********************5. Arbeiten mit Objekten');
var languages = { 'DE': true, 'EN': false, 'FR': false, 'ES': false};
console.log(languages)

console.log('*********************A: Markiere alle Wege, um "EN" auf den Wert true zu setzen')
console.log('languages.EN = true;');
languages.EN = true;
console.log(languages)

// languages("EN", true);

var languages = { 'DE': true, 'EN': false, 'FR': false, 'ES': false};
console.log('languages["EN"] = true;')
languages["EN"] = true;
console.log(languages);

console.log('*********************B: Markiere alle Wege, um "FR" aus dem Objekt zu entfernen');
var languages = { 'DE': true, 'EN': false, 'FR': false, 'ES': false};
// remove languages[FR];
// remove languages.FR;
console.log('delete languages.FR;');
delete languages.FR;
console.log(languages);

// 6. For-Schleife
console.log('*********************6. For-Schleife');
let data = [true, false, true, false, true, false];
console.log(data)

for (let i = 0; i < data.length; i++) {
    if (data[i]) {
        data[i] = false;
    } else {
        data[i] = true;
    }
}

console.log('*********************A: Welche Werte hat das Array nach der For-Schleife?')
console.log(data)

// 7. Funktionen
console.log('*********************7. Funktionen');

let day = 20;
let dayName = 'Monday';

function makeDate(day, dayName) {
    return day + " (" + dayName + ")";
}

let date = makeDate(day, dayName);

console.log('*********************A: Welchen Wert hat die Variable „date“?');
console.log('date =', date);


// 8. HTML DOM
console.log('*********************8. HTML DOM')
console.log('*********************Selektiere die genannten Elemente:');

console.log('*********************A: Das Element mit der ID „footer“');
console.log(document.querySelector('#footer'))

console.log('*********************B: Alle Elemente mit der Klasse „link“');
console.log(document.querySelectorAll('.link'))

console.log('*********************C: Alle Elemente mit der Klasse „link“ innerhalb der Klasse "meta"');
console.log(document.querySelectorAll('.meta .link'))

console.log('*********************D: Das Element mit der Klasse „link“ und „active“');
console.log(document.querySelectorAll('.link.active'))

console.log('*********************E: Alle Elemente mit dem Tag „li“');
console.log(document.querySelectorAll('li'))

// 9. ClassList
console.log('*********************9. ClassList')




