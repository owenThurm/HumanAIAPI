const express = require('express');
const {PythonShell} = require('python-shell');


const app = express();
const port = 5000;

app.use(express.json({extended: false}));

app.get('/', (req, res) => {
  res.send('Welcome to the Human AI ChatBot API. \n\nSend a POST to "/humanresponse" to get a response!')
});


app.post('/humanresponse', (req, res) => {
  let options = {
    mode: 'text',
    pythonOptions: ['-u'], // get print results in real-time
      scriptPath: './AIResponse/', //If you are having python_test.py script in same folder, then it's optional.
    args: [req.body.msg] //An argument which can be accessed in the script using sys.argv[1]
  };

  PythonShell.run('bot.py', options, (err, result) => {
    if (err) throw err;
    // result is an array consisting of messages collected
    //during execution of script.
    console.log('result: ', result.toString());
    res.send(JSON.stringify({ msg:result.toString()}));
  });
});

app.listen(port, err => {
  if(err) console.log(err);
  else console.log('App listening on port: ' + port + '...');
});