// const url = 'http://api.myanimelist.net/v2/users/TomPy/animelist'
// const options = {
//   headers: {'X-MAL-CLIENT-ID': '32ef86fd993671eb0a7281d3031f0be4'}
// }

// console.log($.ajax({
//   url: url,
//   type: 'GET',
//   dataType: 'json',
//   headers : {'X-MAL-CLIENT-ID': '32ef86fd993671eb0a7281d3031f0be4'}
// }))

// // let xhr = new XMLHttpRequest();
// // xhr.open('GET',  url)
// // xhr.setRequestHeader('X-MAL-CLIENT-ID', '32ef86fd993671eb0a7281d3031f0be4')
// // xhr.send()
let output = ''
let result = '';

function runPy() {
  const {spawn} = require('child_process')

  const childPython = spawn('python', ['docs/test.py'], result)
  childPython.stdout.on('data', (data) => {
    result += data.toString()
  })
  childPython.on('close', (code) => {
    return result
  })
}

runPy()
console.log(result)