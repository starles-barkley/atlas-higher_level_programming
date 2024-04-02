#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${argv[2]}`, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
