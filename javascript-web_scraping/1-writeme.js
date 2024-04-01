#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 4) {
  console.log('Usage: node write_file.js <file_path> <content>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
