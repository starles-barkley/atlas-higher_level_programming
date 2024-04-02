#!/usr/bin/node

const fs = require('fs');
const { argv } = require('node:process');

fs.writeFile(argv[2], argv[3], err => {
  if (err) {
    throw err;
  }
});
