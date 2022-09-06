#!/usr/bin/node
exports.logMe = (function () {
  const closure = { n: 0, incr () { this.n++; } };

  return function (input) {
    console.log(`${closure.n}: ${input}`);
    closure.incr();
  };
})();
