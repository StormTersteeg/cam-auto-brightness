# CaB - Cam Auto Brightness

![image](https://github.com/StormTersteeg/cam-auto-brightness/assets/42808385/bc93a81d-801d-4257-8223-573763dfba50)

CaB (Cam Auto Brightness) is a desktop application that dynamically adjusts your laptop's display brightness based on the ambient light detected by your webcam.
I created this project because I wanted to see if this concept would work, and it does, but I wouldn't call it a great solution.

### Features

- **Interval Time (seconds):** Set the time interval (in seconds) at which the app checks and adjusts the brightness.
- **Minimum Difference:** Define the minimum difference in brightness levels that triggers an adjustment.
- **Brightness Range:** Specify the minimum and maximum brightness levels for the display.
- **Start/Stop Control:** Easily start and stop the brightness adjustment process.

### Prerequisites

- Windows 10 or later
- Webcam (built-in or external)

### Usage

1. **Download the App:**
   Go to the [releases page](https://github.com/StormTersteeg/cam-auto-brightness/releases) of the repository and download the latest release.
2. **Launch the App:**
   Start the application to see the main interface (no installation required).
3. **Configure Settings:**
   - **Interval Time (seconds):** Enter the desired interval time for checking brightness.
   - **Minimum Difference:** Set the minimum brightness change that should trigger an adjustment.
   - **Brightness Range:** Adjust the sliders to set the minimum and maximum brightness levels.
4. **Start Monitoring:**
   Click the "START" button to begin the brightness adjustment process. The app will now monitor the ambient light using the webcam and adjust the screen brightness accordingly.

### Development

CaB - Cam Auto Brightness was built using the [Python Glide Framework](https://github.com/StormTersteeg/Python-Glide-Framework).
Glide provides a simple foundation for developing desktop applications with HTML, CSS and JavaScript.
