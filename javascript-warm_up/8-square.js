#!/usr/bin/node

const size = process.argv[2];

if (isNaN(parseInt(size))) {
    console.log("Missing size");
} else {
