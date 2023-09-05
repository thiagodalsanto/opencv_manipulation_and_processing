import cv2

class CaptureImage:
    def __init__(self, main_instance):
        self.main_instance = main_instance

    def capturar_cor(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cor_pixel = self.main_instance.imagem_capturada[y, x]
            print(f"Cor RGB: {cor_pixel}")
