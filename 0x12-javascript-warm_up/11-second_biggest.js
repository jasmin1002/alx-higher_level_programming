#!/usr/bin/node
const inputs = process.argv.slice(2);

if (!inputs.length || inputs.length === 1) {
  console.log(0);
} else {
  const numArr = inputs.map(input => Number(input));
  console.log(numArr.sort()[numArr.length - 2]);
}
