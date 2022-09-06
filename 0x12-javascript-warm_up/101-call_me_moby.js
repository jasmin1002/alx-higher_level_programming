#!/usr/bin/node
exports.callMeMoby = (times, callback) => {
  for (let i = 1; i <= times; i++) callback();
};
