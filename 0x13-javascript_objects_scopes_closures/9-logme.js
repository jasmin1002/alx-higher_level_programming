#!/usr/bin/node
// Define Immediately Invoke Function Expression, IIFE
// IIFE returns another function expression for future execution
exports.logMe = (function () {
  // Define local variable for IIFE: closure obj.
  const closure = { n: 0, incr () { this.n++; } };

  return function (input) { // Return function from IIFE
    console.log(`${closure.n}: ${input}`);
    closure.incr(); // Increment n: property of closure local variable in IIFE
  };
})();
