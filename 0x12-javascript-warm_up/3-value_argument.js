#!usr/bin/node
// script that prints the first argument passed to it:
const myArg = process.argv[2];
if (myArg === undefined) {
  console.log('No argument');
} else {
  console.log(myArg);
}
