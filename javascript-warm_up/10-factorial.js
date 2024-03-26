#!/usr/bin/node

function computeFactorial(num) {
  if (isNaN(parseInt(num))) {
      return 1;
  } else if (parseInt(num) <= 1) {
      return 1;
  } else {
      return parseInt(num) * computeFactorial(parseInt(num) - 1);
  }
}

const input = process.argv[2];
console.log(computeFactorial(input));
