function movieParser(input) {
  let movies = [];

  for (const line of input) {
    let command = line.split(" ");
    if (line.includes("addMovie")) {
      movieName = command.slice(1).join(" ");
      addMovie(movieName);
    } else if (line.includes("directedBy")) {
      let indexOfCommand = command.indexOf('directedBy');
      let movieName = command.slice(0, indexOfCommand).join(' ');
      let director = command.slice(indexOfCommand + 1).join(' ');
      addDirector(movieName, director);
    } else {
        let indexOfCommand = command.indexOf('onDate');
        let movieName = command.slice(0, indexOfCommand).join(' ');
        let date = command.slice(indexOfCommand + 1).join(' ');
        addDate(movieName, date)
    }
  }

  for (const movie of movies) {
    if (movie.hasOwnProperty('name') && movie.hasOwnProperty('date') && movie.hasOwnProperty('director')){
        console.log(JSON.stringify(movie));
    }

  } 

  function addMovie(name) {
    movies.push( {name} );
  }

  function addDirector(name, director) {
    let movie = movies.find((m) => m.name === name);
    if (movie) {
      movie.director = director;
    }
  }

  function addDate(name, date) {
    let movie = movies.find((m) => m.name === name);
    if (movie) {
      movie.date = date;
    }
  }
}