const python = require('python-shell');


// let options = {
//   mode: 'text',
//   pythonPath: 'python',
//   pythonOptions: ['-u'], // get print results in real-time
//   scriptPath: './',
//   args: ['value1']
// };
//  python.PythonShell.run('test.py', options, function (err, results) {
//   if (err) throw err;
//   // results is an array consisting of messages collected during execution
//   console.log('results: %j', results);
// });


let pyshell = new python.PythonShell('test.py');
 
// sends a message to the Python script via stdin

pyshell.send('0312195516');
 
pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});
 
// end the input stream and allow the process to exit
pyshell.end(function (err,code,signal) {
  if (err) throw err;
  // console.log('The exit code was: ' + code);
  // console.log('The exit signal was: ' + signal);
  // console.log('finished');
  // console.log('finished');
});