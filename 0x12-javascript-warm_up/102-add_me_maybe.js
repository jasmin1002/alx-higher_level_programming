#!/usr/bin/node
exports.addMeMaybe = (number, callback) => {
  number += 1;
  callback(number);
};
