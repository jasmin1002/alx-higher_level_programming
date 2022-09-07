#!/usr/bin/node
const dict = require('./101-data').dict;
const sorted = {};
const values = Object.values(dict);
const len = values.length;

for (let i = 0; i < len; i++) {
  let tmp;

  for (key in dict) {
    if (dict.key === values[i]) break;
  }

  if (!(String(values[i]) in sorted)) {
    sorted[values[i]] = [];
    sorted[values[i]].push(String(key));
  } else {
    sorted[values[i]].push(String(key));
  }
}
console.log(sorted);
