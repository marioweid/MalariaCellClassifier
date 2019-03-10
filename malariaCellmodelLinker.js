function getPrediction() {
    let ps = require("python-shell");

    let img_var = document.getElementById("uploaded_image").src;

    let options = {
        mode: "text",
        scriptPath: "python/",
        pythonPath: "D:/Programme/Anaconda/envs/tf3.6/python.exe",
        args: [img_var]
    };

    // sends a message to the Python script via stdin
    ps.PythonShell.run('predict.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
    });

}