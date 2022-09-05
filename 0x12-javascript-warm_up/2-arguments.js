#!/usr/bin/node
const argv = process.argv;
const subArray = argv.slice(2);

if (subArray.length === 0) {
  console.log('No argument');
} else if (subArray.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
