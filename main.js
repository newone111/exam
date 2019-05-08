const express = require('express');
const { fork } = require('child_process');
const app = express();

app.get('/', (req, res) => res.send('Hello World!'));
app.get('/intense', (req, res) => {
    res.send('CPU Load test for 60 dec');
    var sys = require('sys');
    var exec = require('child_process').exec;

    function puts(error, stdout, stderr) { sys.puts(stdout) }
    exec("seq 1 | xargs -P0 -n1 timeout 60 yes > /dev/null", function(err, stdout, stderr) {
    console.log(stdout);
    });
});
app.listen(3000, () => console.log('Example app listening on port 3000!'));