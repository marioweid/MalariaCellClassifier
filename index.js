const electron = require("electron")
const url = require("url")
const path = require("path")

const {
    app,
    BrowserWindow,
    globalShortcut
} = electron;

// Set Env
// process.env.NODE_ENV = "production"

let mainWindow;

app.on("ready", function () {
    // Create new window
    mainWindow = new BrowserWindow({
        width: 600,
        height: 500,
        frame: false
    });
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, "mainWindow.html"),
        protocol: "file:",
        slashes: true
    }))
    globalShortcut.register('CommandOrControl+Q', () => {
        app.quit();
    })

    mainWindow.on("closed", function () {
        app.quit();
    })
    //mainWindow.setMenu(null);
})