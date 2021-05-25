const {PythonShell} = require('python-shell');

let options = {
  mode: 'text',
  pythonPath: '/home/fidan/Documents/pyProjects/venv/bin/python',
  pythonOptions: ['-u'], // get print results in real-time
  scriptPath: './',
  args: ['Верстка сайта. Javascript. Frontend разработчик']
};
const a = []

async function runPython() {
    const results = await (new Promise((resolve,reject)=> {
        PythonShell.run('hello_2.py',options, function(err,results) {
        if(err) reject(err)

        resolve(results)
        })
    }))
    return results
}

async function pyGet() {
    const data = await runPython()
    console.log(data)
    return data
}
pyGet()
