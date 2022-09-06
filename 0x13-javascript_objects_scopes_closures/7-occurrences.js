#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  let times = 0; // keep track of number of occurrence

  if (!searchElement || !list[0]) return -1;

  // Iterate over given list.
  list.forEach(item => {
    if (item === searchElement) times += 1;
  });

  // Return No. of occurrence.
  return times;
};
