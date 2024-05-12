const { app, BrowserWindow } = require('electron');

function createWindow() {
   // Create the browser window
   const mainWindow = new BrowserWindow({
      width: 800,
      height: 600,
      webPreferences: {
         nodeIntegration: true,
      },
   });

   // Load the index.html file
   mainWindow.loadFile('index.html');
}

// When Electron has finished initialising and is ready to create browser windows
app.whenReady().then(() => {
   createWindow();

   app.on('activate', function () {
      if (BrowserWindow.getAllWindows().length === 0) createWindow();
   });
});

// Quit the application when all windows are closed
app.on('window-all-closed', function () {
   if (process.platform !== 'darwin') app.quit();
});