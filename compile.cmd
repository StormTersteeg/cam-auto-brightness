cd bin
py -m PyInstaller app.pyw --onefile --icon ../resources/icon.ico --clean --collect-binaries clr_loader
cd ..