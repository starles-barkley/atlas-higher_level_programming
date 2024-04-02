#!/usr/bin/node

const { argv } = require('node:process');

request(`https://swapi-api.hbtn.io/api/films/${argv[2]}`, (err, res, body) => {
  if (err) {
    console.error(err);
});