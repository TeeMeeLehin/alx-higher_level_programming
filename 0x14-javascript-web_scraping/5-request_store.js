#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, response.body, err => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
