#!/usr/bin/node
const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
	console.log(`Expect (${2} parameters), got ${process.argv.length - 2}`)
	process.exit(1)
}
const parameters = process.argv.splice(2, 2);

request
	.get(parameters[0])
	.on('error', err => console.error(err))
	.on('response', response => {
		if (response.statusCode === 200) 'Good to go...';
	})
	.pipe(fs.createWriteStream(parameters[1]))
