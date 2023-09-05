import cv2

class CaptureImage:
    def __init__(self, main_instance):
        self.main_instance = main_instance

    def color_capture(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel_color = self.main_instance.captured_image[y, x]
            print(f"Cor RGB: {pixel_color}")
