#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

function countS (strings) {
  let count = 0;
  for (let i = 0; i < strings.length; i++) {
    if (strings[i].endsWith('/18/')) {
      count++;
    }
  }
  return count;
}

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode !== 200) {
    console.error(`code; ${response.statusCode}`);
  } else {
    let count = 0;
    const filmsData = JSON.parse(response.body).results;
    for (let i = 0; i < filmsData.length; i++) {
      count += countS(filmsData[i].characters);
    }

    console.log(count);
  }
});
