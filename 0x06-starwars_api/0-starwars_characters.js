#!/usr/bin/node
const request = require('request');

const api_url = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
    const film_url =  api_url + '/films/' + process.argv[2];
    request.get(film_url, (error, res, body) => {
        if (error) {
            console.log("Error:", error.message);
            return;
        }

        body = JSON.parse(body);
        const characters = body['characters'];
        characters.forEach(character_url => {
            request.get(character_url, (error, res, body) => {
                if (error) {
                    console.log('Error:', error);
                    return;
                }

                body = JSON.parse(body);
                console.log(body['name']);
            });
            
        });
    })
} else {
    console.log('Usage: film id required');
    return;
}
