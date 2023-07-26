#!/usr/bin/node
// Writes a string to a file

const fs = require('fs');
const argv = process.argv;

if (argv.length !== 4) {
  console.error('Usage: node script.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = argv[2];
const string = argv[3];

fs.writeFile(filePath, string, 'utf8', function (err) {
  if (err) {
    console.error('Error writing to file:', err);
  } else {
    console.log('String has been written to the file successfully.');
  }
});
