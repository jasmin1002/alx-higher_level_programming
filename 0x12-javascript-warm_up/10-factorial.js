#!/usr/bin/node
const num = Number(process.argv[2]);

function factorial (input) {
  if (isNaN(input) || input === 0) {
    return 1;
  } else {
    return input * factorial(input - 1);
  }
}

console.log(factorial(num));
