#!/usr/bin/node
const argv = process.argv;
const subArray = argv.slice(2);
const number = Number(subArray[0]);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Math.floor(number));
}
