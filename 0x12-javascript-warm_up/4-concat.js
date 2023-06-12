#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: “ is ”
const myArgs = process.argv.slice(2);
if (myArgs[0] && myArgs[1]) {
  console.log(`${myArgs[0]}` + ' is ' + `${myArgs[1]}`);
} else if (myArgs[0] && !myArgs[1]) {
  console.log(`${myArgs[0]}` + ' is ' + 'undefined');
} else {
  console.log('undefined is undefined');
}
