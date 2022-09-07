#!/usr/bin/node
const list = require('./100-data').list;
const nList = list.map((item, idx) => idx * item);
console.log(`${list}\n${nList}`);
