#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
// empty dictionary, keys will be userIds and values will be number of
// tasks completed
const dictCompleted = {};
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error', error.message);
    process.exit(1);
  } else {
    const taskData = JSON.parse(body);
    // parse JSON from API into JS object
    for (const index in taskData) {
      const task = taskData[index];
      if (task.completed === true) {
        if (dictCompleted[task.userId] === undefined) {
          // if user not yet defined in dictionary, make count 1
          dictCompleted[task.userId] = 1;
        } else {
          // add to count
          dictCompleted[task.userId]++;
        }
      }
    }
    console.log(dictCompleted);
  }
});
