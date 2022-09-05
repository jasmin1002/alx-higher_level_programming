#!/usr/bin/node
const argv = process.argv;
const inputs = argv.slice(2);

function add (a, b) {
  return a + b;
}

if (!inputs.length) {
  console.log(Number(inputs[0]));
} else {
  const sum = add(Number(inputs[0]), Number(inputs[1]));
  console.log(sum);
}
