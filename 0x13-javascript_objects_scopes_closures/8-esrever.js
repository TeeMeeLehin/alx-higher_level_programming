#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const len = list.length;
  for (let i = len; i > 0; i--) {
    newList.push(list[i - 1]);
  }
  return newList;
};
