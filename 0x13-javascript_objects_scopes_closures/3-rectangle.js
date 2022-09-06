#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let cnt = 1;

    while (cnt <= this.height) {
      let shape = '';
      for (let i = 1; i <= this.width; i++) shape += 'X';
      console.log(shape);
      cnt += 1;
    }
  }
};
