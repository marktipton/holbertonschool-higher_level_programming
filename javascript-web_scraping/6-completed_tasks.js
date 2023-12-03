#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const dictCompleted = {};
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error', error.message);
    process.exit(1);
  } else {
    const taskData = JSON.parse(body);
    // console.log(taskData);
    for (const index in taskData) {
      const task = taskData[index];
      if (task.completed === true) {
        if (dictCompleted[task.userId] === undefined) {
          dictCompleted[task.userId] = 1;
        } else {
          dictCompleted[task.userId]++;
        }
      }
    }
    console.log(dictCompleted);
  }
});
