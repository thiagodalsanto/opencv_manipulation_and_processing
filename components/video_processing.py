import cv2
import tkinter as tk
from tkinter import ttk
import threading

from components.apply_filters import ApplyFilters
from components.capture_image import CaptureImage

class Main:
    def __init__(self, video_filename):
        self.video_filename = video_filename
        self.imagem_capturada = None
        self.apply_filters = ApplyFilters(self)
        self.capture_image = CaptureImage(self)
        self.brilho_atual = 0
        self.sigma_atual = 0
        self.kernel_size_atual = 1
        self.lower_limiar = 1
        self.upper_limiar = 1
        self.threshold = 1
        self.capture_button_pressed = False

    def load_video(self):
        video = cv2.VideoCapture(self.video_filename)
        cv2.namedWindow('Video', cv2.WINDOW_AUTOSIZE)
        tecla = 0

        def create_capture_window():
            root = tk.Tk()
            root.title("Capturar")
            root.geometry("200x100")

            def capture_image():
                self.capture_button_pressed = True

            capture_button = ttk.Button(root, text="Capturar", command=capture_image)
            capture_button.pack(pady=20)

            root.mainloop()

        # Cria a thread para a janela do botão "Capturar"
        capture_thread = threading.Thread(target=create_capture_window)
        capture_thread.daemon = True
        capture_thread.start()

        while tecla != 27:
            ret, frame_video = video.read()

            if not ret:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            cv2.imshow("Video", frame_video)
            tecla = cv2.waitKey(1) & 0xFF

            if self.capture_button_pressed:
                cv2.destroyWindow("Imagem Capturada")
                self.imagem_capturada = frame_video.copy()
                self.imagem_capturada = cv2.cvtColor(self.imagem_capturada, cv2.COLOR_BGR2RGB)
                cv2.imshow("Imagem Capturada", self.imagem_capturada)
                cv2.imwrite("captura_do_frame.png", self.imagem_capturada)

                cv2.setMouseCallback("Imagem Capturada", self.capture_image.capturar_cor)

                cv2.createTrackbar("Gaussian Blur", "Imagem Capturada", self.sigma_atual, 255, self.apply_filters.gaussian_blur)
                cv2.createTrackbar("Bilateral Blur", "Imagem Capturada", self.kernel_size_atual, 255, self.apply_filters.bilateral_blur)
                cv2.createTrackbar("Lower Limiar", "Imagem Capturada", self.lower_limiar, 255, self.apply_filters.change_lower_limiar)
                cv2.createTrackbar("Upper Limiar", "Imagem Capturada", self.upper_limiar, 255, self.apply_filters.change_upper_limiar)
                cv2.createTrackbar("Threshold", "Imagem Capturada", self.threshold, 255, self.apply_filters.apply_threshold)

                self.capture_button_pressed = False

        video.release()
        cv2.destroyAllWindows()

    def update_limiar_filter(self):
        edges = cv2.Canny(self.imagem_capturada, self.lower_limiar, self.upper_limiar, apertureSize=3, L2gradient=False)
        cv2.imshow("Imagem Capturada", edges)
