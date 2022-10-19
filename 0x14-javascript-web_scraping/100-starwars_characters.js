#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

if (!id) {
  console.log('url not found!');
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  if (response.statusCode === 200) {
    const { characters } = JSON.parse(body);
    characters.forEach(actor => {
      request.get(actor, (error, response, body) => {
        if (error) console.log(error);
        if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
