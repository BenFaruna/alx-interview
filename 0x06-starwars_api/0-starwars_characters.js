#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  const filmUrl = apiUrl + '/films/' + process.argv[2];
  request.get(filmUrl, (error, res, body) => {
    if (error) {
      console.log('Error:', error.message);
      return;
    }

    body = JSON.parse(body);
    const characters = body.characters;
    characters.forEach(characterUrl => {
      request.get(characterUrl, (error, res, body) => {
        if (error) {
          console.log('Error:', error);
          return;
        }

        body = JSON.parse(body);
        console.log(body.name);
      });
    });
  });
} else {
  console.log('Usage: film id required');
}
