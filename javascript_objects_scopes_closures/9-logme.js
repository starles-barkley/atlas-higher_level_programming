#!/usr/bin/node

const count = 0;

exports.logMe = function(item) {
    count++;

    console.log(count - 1 + ': ' + item);
};
