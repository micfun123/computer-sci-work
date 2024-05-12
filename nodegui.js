require("@nodegui/nodegui");

const { QMainWindow } = require("@nodegui/nodegui");

const win = new QMainWindow();
win.show();

global.win = win; // To prevent win from being garbage collected.