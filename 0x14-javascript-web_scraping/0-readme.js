#!/usr/bin/node
// script that reads and prints the content of a file.

const argv = process.argv;
const fs = require('fs'); // Use const instead of let for fs
fs.readFile(argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
