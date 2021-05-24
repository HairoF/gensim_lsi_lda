const Py = require('python-shell');

let options = {
  mode: 'text',
  pythonPath: '/home/fidan/Documents/pyProjects/venv/bin/python',
  pythonOptions: ['-u'], // get print results in real-time
  scriptPath: './',
  args: ['value1','value2']
};

let yahooo = [];
const ya = Py.PythonShell.run('main.py', options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
// yahooo.push(results);
});
   console.log(ya);