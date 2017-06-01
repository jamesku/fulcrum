var PythonShell = require('python-shell');

var articleArray = new Array();
var options = {
  mode: 'text',
  pythonPath: '/usr/bin/python3',
};

var getDataPython = new PythonShell('./python/main.py', options);
// getDataPython.run;
// getDataPython.end(function(){
//   console.log("hello");
// });


getDataPython.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);

    console.log("starting article grouping")
    grouping();

    console.log("starting article postive/negative analysis")
    posneg();
});

function grouping(){
  var group = new PythonShell('./python/main.py', options);

}

function posneg(){
  var posneg = new PythonShell('./python/main.py', options);

}
