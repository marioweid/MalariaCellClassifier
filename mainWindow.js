var python = require("python-shell");
var path = require("path");
let filePath;

if (window.FileReader) {
    var drop;

    addEventHandler(window, 'load', function () {
        drop = document.getElementById('drop');

        function cancel(e) {
            if (e.preventDefault) {
                e.preventDefault();
            }
            return false;
        }

        // Tells the browser that we *can* drop on this target
        addEventHandler(drop, 'dragover', cancel);
        addEventHandler(drop, 'dragenter', cancel);

        addEventHandler(drop, 'drop', function (e) {
            e = e || window.event; // get window.event if e argument missing (in IE)   
            if (e.preventDefault) {
                e.preventDefault();
            } // stops the browser from redirecting off to the image.

            var dt = e.dataTransfer;
            var files = dt.files;
            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                var reader = new FileReader();

                //attach event handlers here...

                reader.readAsDataURL(file);
                addEventHandler(reader, 'loadend', function (e, file) {
                    var bin = this.result;
                    var newFile = document.createElement('div');
                    newFile.innerHTML = 'Loaded : ' + file.name + ' size ' + file.size + ' B';
                    drop.appendChild(newFile);
                    drop.innerHTML = "";

                    var img = document.createElement("img");
                    img.file = file;
                    img.src = bin;
                    img.setAttribute("id", "uploaded_image");
                    if (drop.childElementCount == 0) {
                        drop.appendChild(img);
                    } else {
                        while (drop.firstChild) {
                            drop.removeChild(drop.firstChild);
                        }
                    }
                    /*
                    PARSES REGEX to get Base64 content but pretty much useless because the args is too long to pass it ti the python file
                    bas64RegEx = /(,)(.*)$/gm;
                    match = bas64RegEx.exec(bin);
                    base64String = match[2];

                    */
                    filePath = file["path"];
                }.bindToEventHandler(file));
            }
            return false;
        });
        Function.prototype.bindToEventHandler = function bindToEventHandler() {
            var handler = this;
            var boundParameters = Array.prototype.slice.call(arguments);
            console.log(boundParameters);
            //create closure
            return function (e) {
                e = e || window.event; // get window.event if e argument missing (in IE)   
                boundParameters.unshift(e);
                handler.apply(this, boundParameters);
            }
        };
    });
} else {
    document.getElementById('status').innerHTML = 'Your browser does not support the HTML5 FileReader.';
}

function addEventHandler(obj, evt, handler) {
    if (obj.addEventListener) {
        // W3C method
        obj.addEventListener(evt, handler, false);
    } else if (obj.attachEvent) {
        // IE method.
        obj.attachEvent('on' + evt, handler);
    } else {
        // Old school method.
        obj['on' + evt] = handler;
    }
}

function getPrediction() {
    let ps = require("python-shell");
    let textObj = document.getElementById("classification");

    let img_var = filePath;

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
        textObj.innerHTML = results[2];
        if (textObj.innerHTML == "Parasitized") {
            textObj.style.color = "red";
        } else if (textObj.innerHTML == "Uninfected") {
            textObj.style.color = "green";
        }
    });
}