#!/usr/bin/node
// 0. Star Wars Characters

const request = require('request');
const film = process.argv[2];
const api = 'https://swapi-api.hbtn.io/api/';
const url = api + 'films/' + film + '/';
request.get({ url }, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    order(characters);
  }
});

function order (characters) {
  if (characters.length > 0) {
    request.get({ url: characters.shift() }, function (error, response, body) {
      if (!error) {
        console.log(JSON.parse(body).name);
        order(characters);
      }
    });
  }
}
