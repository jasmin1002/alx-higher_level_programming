$(function () {
  const ul = $('UL#list_movies');
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (response) {
      const films = response.results;
      $.each(films, (index, film) => {
        ul.append('<li>' + film.title + '</li>');
      });
    }
  });
});
