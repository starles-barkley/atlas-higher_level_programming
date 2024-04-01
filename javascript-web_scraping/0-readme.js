#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 3) {
  console.log('Usage: node read_file.js <file_path>');
  process.exit(1);
}
