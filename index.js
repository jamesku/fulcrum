var PythonShell = require('python-shell');

var articleArray = new Array();
var options = {
  mode: 'text',
  pythonPath: '/usr/bin/python3',
};

var options2 = {
  mode: 'text',
  pythonPath: '/usr/bin/python',
};

//use python3
var getDataPython = new PythonShell('./python/main.py', options);

getDataPython.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);

    //console.log("starting article grouping")
    //grouping();

    console.log("starting article postive/negative analysis")
    posneg();
});

function grouping(){
  //use python 2
  var group = new PythonShell('./python/main.py', options2);
  group.on('message', function (message) {
    console.log(message);
  });


}

function posneg(){
  var posneg = new PythonShell('./usent/sentiment2.py', options2);
  posneg.on('message', function (message) {
    console.log(message);
  });
}
