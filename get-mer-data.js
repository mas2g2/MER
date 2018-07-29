var exec = require('child_process').exec;
var child;

//executes command 'pwd'

child = exec("python mer.py "+process.argv[2]+" "+process.argv[3],function (error, stdout, stderr){
        var result = "Result:"
        console.log('stdout : '+stdout);
        var data = stdout.slice(stdout.indexOf(result) + result.length);
        console.log('stderr : '+stderr);
        console.log(data)
        if(error != null){
                console.log('exec error : '+error);
        }
});