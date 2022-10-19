#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.log('url not found!');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  if (response.statusCode === 200) {
    let count = 0;
    const { results } = JSON.parse(body);
    results.forEach(film => {
      const { characters } = film;
      characters.forEach(actor => {
        if (actor.includes('18')) count++;
      });
    });
    console.log(count);
  }
});
