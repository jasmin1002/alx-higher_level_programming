#!/usr/bin/node
module.exports = class Rectangle {
  // Init the instance field: width and height.
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Prints shape of a rectangle
  print () {
    let cnt = 1;
    while (cnt <= this.height) {
      let shape = '';
      for (let i = 1; i <= this.width; i++) shape += 'X';
      console.log(shape);

      cnt++;
    }
  }

  // Swaps the shape's dimensions
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // Double shape's dimensions by 2
  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
};
