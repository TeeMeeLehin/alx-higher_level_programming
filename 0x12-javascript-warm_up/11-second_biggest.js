#!/usr/bin/node
let arr = process.argv;
if (arr.length <= 3) {
  console.log(0);
} else {
  for (let i = 0; i < arr.length; i++) {
    arr[i] = parseInt(arr[i]);
  }
  arr = arr.slice(2);
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
