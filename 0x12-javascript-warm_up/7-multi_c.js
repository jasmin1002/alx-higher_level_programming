#!/usr/bin/node
const input = process.argv[2];

if (!input) {
  console.log('Missing number of occurrences');
} else {
  let counter = 1;

  while (counter <= input) {
    console.log('C is fun');
    counter++;
  }
}
