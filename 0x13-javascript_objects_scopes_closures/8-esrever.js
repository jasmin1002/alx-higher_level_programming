#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;

  // Calculate number of iterations.
  const loop = Math.round(len / 2);

  for (let i = 0; i < loop; i++) {
    // Temporary cache ith element of a list
    const tmp = list[i];

    // Set index ith with (length - 1 - i)th value
    list[i] = list[len - 1 - i];

    // Set (length - 1 - i)th index with ith value.
    list[len - 1 - i] = tmp;
  }

  // Return reversed arr
  return list;
};
