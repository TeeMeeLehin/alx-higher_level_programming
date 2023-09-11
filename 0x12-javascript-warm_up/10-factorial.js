#!/usr/bin/node
function fact (num) {
  num = parseInt(num);
  if (isNaN(num) || num === 0) {
    return 1;
  } else {
    return num * fact(num - 1);
  }
}
console.log(fact(process.argv[2]));
