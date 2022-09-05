#!/usr/bin/node
const argv = process.argv;
const subArray = argv.slice(2);

if (subArray[0] === undefined) {
  console.log('No argument');
} else {
  console.log(subArray[0]);
}
