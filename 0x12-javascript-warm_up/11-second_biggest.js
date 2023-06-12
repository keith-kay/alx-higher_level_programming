#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const listArg = process.argv.slice(2);
if (listArg.length === 0 || listArg.length === 1) {
  console.log(0);
} else {
  listArg.sort((a, b) => a - b);
  console.log(listArg[listArg.length - 2]);
}
