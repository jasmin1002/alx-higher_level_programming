#!/usr/bin/node
const size = Number(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let cnt = 1;

  while (cnt <= size) {
    let tmp = '';
    for (let i = 1; i <= size; i++) tmp += 'X';

    console.log(tmp);
    cnt++;
  }
}
