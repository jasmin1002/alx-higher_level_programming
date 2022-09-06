#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  let times = 0; // keep track of number of occurrence

  if (!searchElement || !list[0]) return -1;

  // Iterate over given list.
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) times++;
  }

  // Return No. of occurrence.
  return times;
};
