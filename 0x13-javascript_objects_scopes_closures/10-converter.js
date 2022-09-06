#!/usr/bin/node
exports.converter = (function () {
  return function (base) {
    return function (number) {
      const result = number.toString(base);

      return result;
    };
  };
})();
