import cv2
import numpy as np
import wmi
import time
import webview, os

def is_webcam_in_use():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if cap.isOpened():
        cap.release()
        return False
    return True

def capture_image():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    if not cap.isOpened():
        print("Cannot open webcam")

    time.sleep(2)
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()

    if not ret:
        print("Failed to capture image from webcam")

    return frame

def calculate_brightness(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray_image)
    return brightness

def set_brightness(level):
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(level, 0)

class Api:
    def __init__(self):
        self.current_brightness = 0

    def minimize(self):
        window.minimize()

    def fullscreen(self):
        window.toggle_fullscreen()

    def close(self):
        window.destroy()
        os._exit(0)

    def adjust_brightness(self, maximum_brightness, minimum_brightness, minimum_difference, brightness_offset):
        if not is_webcam_in_use():
            try:
                image = capture_image()
                brightness = calculate_brightness(image)

                # Normalize and adjust brightness with minimal difference check
                brightness_level = np.clip((brightness / 255) * 100, 0, 100)
                brightness_level += brightness_offset
                
                if brightness_level > maximum_brightness:
                    brightness_level = maximum_brightness
                elif brightness_level < minimum_brightness:
                    brightness_level = minimum_brightness

                if abs(brightness_level - self.current_brightness) > minimum_difference:
                    self.current_brightness = brightness_level
                    set_brightness(int(brightness_level))
            except Exception as e:
                print(f"An error occurred: {e}")

def on_closed():
  pass

def on_closing():
  pass

def on_shown():
  pass

def on_loaded():
  pass

#!FLAG-HTML

if __name__ == '__main__':
  api = Api()
  window = webview.create_window("{settings.app_name}", html=html, js_api=api, width={settings.app_proportions[0]}, height={settings.app_proportions[1]}, confirm_close={settings.app_confirm_close}, frameless={settings.app_frameless}, fullscreen={settings.app_fullscreen}, resizable={settings.app_resizable})
  window.events.closed += on_closed
  window.events.closing += on_closing
  window.events.shown += on_shown
  window.events.loaded += on_loaded
  webview.start(gui="{settings.app_web_engine}", debug={settings.app_allow_inspect})