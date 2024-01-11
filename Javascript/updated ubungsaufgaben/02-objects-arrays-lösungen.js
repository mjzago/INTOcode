/**
 * OBJECTS
 */
let books = {
  book1: '1984',
  book2: 'Faust',
  book3: 'Fantastic Mr. Fox'
};

const arr = ['A', 'B', 'C', 'D'];



// for (const [key, value] of Object.entries(books)) {
//   console.log(key, value);
// }


let keys = Object.keys(books);

keys.forEach(
  function(key, index) {
    console.log(index, books[key])
  }
)

for (var i = 0; i < keys.length; i++) {
  const key = keys[i];
  const book = books[key]
  console.log(i, book);
}

for (const [key, value] of Object.entries(books)) {
  console.log(key, value);
}



// add a new book to the books object
// using dot notation
books.book4 = 'Harry Potter';

// using square bracket notation
books['book4'] = 'Harry Potter';

// remove an book from the books object
delete books.book2;
// delete books['book3'];

// log the third book
console.log(books.book3)

// iterate over the books and log every single one

/**
 * ARRAYS
 */
let movies = [
  'Pulp Fiction', 
  'Inception', 
  'Call me by your name', 
  'Batman'
];

// add a new movie to the array
movies.push('Superman');
movies.unshift('Titanic');

// remove the movie „Call me by your name“ from the movies object
movies.splice(2, 1); // 2 = Index, 1 = Anzahl

// log the first movie
console.log(movies[0]);

// iterate over the movies and log every single one 
for (let movie of movies) {
  console.log(movie);
}

movies.forEach(function(movie, index) {
  console.log(index, movie);
})

