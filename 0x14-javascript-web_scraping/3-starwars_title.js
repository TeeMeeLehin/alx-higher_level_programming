#!/usr/bin/node

const request = require('request');
const ep = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ep}`;

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(response.body).title);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
