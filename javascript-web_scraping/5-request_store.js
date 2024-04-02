#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('node:fs');
const request = require('request');

request(`${argv[2]}`, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(argv[3], body, err => {
      if (err) {
        throw err;
      }
    });
  }
});
