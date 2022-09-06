#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let times = 0; // keep track of number of occurrence

  if (!searchElement || !list[0]) return -1;

  // Iterate over given list.
  list.forEach(item => {
    if (item === searchElement) times++;
  });

  // Return No. of occurrence.
  return times;
};
