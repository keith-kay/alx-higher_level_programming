#!/usr/bin/node
// 5-square.js
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
