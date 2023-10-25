#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const stars = JSON.parse(response.body).characters;

    stars.forEach(star => {
      request(star, (err, response) => {
        if (err) {
          console.log(err);
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(response.body).name);
        } else {
          console.log(`code: ${response.statusCode}`);
        }
      });
    });
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
