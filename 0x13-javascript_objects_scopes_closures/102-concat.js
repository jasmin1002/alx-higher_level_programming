#!/usr/bin/node
const argv = process.argv.slice(2);
const fs = require('fs');
try {
  argv[0] = fs.readFileSync(argv[0], 'utf8');
  argv[1] = fs.readFileSync(argv[1], 'utf8');
  fs.writeFileSync(argv[2], argv[0] + argv[1]);
} catch (err) {
  console.log('Path cannot be undefined');
}
