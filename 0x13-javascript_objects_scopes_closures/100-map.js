#!/usr/bin/node
// Import data file
const list = require('./100-data').list;

// Transform each element of input array, list
// by multiplying each element with its index.
const nList = list.map((item, idx) => idx * item);

// Print both arrays.
console.log(list);
console.log(nList);
