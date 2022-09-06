#!/usr/bin/node
exports.converter = (function () {
  return function (base) {
    return function (number) {
      return number.toString(base);
    };
  };
}());
