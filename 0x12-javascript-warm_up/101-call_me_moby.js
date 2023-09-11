#!/usr/bin/node
const callMeMoby = function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

module.exports = {
  callMeMoby
};
