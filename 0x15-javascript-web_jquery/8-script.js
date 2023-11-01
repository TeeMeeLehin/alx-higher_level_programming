$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    const results = data.results;

    for (let i = 0; i < results.length; i++) {
        const movieTitle = results[i].title;
        $('UL#list_movies').append('<li>' + movieTitle + '</li>');
    }
})
