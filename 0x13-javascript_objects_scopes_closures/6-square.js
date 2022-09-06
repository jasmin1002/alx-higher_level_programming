#!/usr/bin/node
// Import the base class: Square
const BaseSquare = require('./5-square');

// Create subclass: Square extends the base class
module.exports = class Square extends BaseSquare {
  // Square print method
  charPrint (pattern) {
    if (!pattern) {	// Use parent print method, if pattern === undefined
      super.print();
    } else {
      let incr = 1;
      while (incr <= this.height) {
        let shape = '';
        for (let i = 1; i <= this.width; i++) shape += pattern;
        console.log(shape);

        incr++;
      }
    }
  }
};
