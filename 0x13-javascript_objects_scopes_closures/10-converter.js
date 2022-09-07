#!/usr/bin/node
// Define Immediately Invoked Function Expression, IIFE
// that returns function for future execution.
exports.converter = (function () {
  // Returned function expression close
  // around local variable, base (closure)
  return function (base) {
    // Another function expression defines
    // number to be converted.
    return function (number) {
      // Returns conversion result to the caller
      return number.toString(base);
    };
  };
}());
