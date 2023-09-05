import cv2
import numpy as np

class ApplyFilters:
    def __init__(self, main_instance):
        self.main_instance = main_instance

    def apply_filters(self, gaussian_value, bilateral_value):
        color_channels = cv2.split(self.main_instance.imagem_capturada)
        self.main_instance.brightness_now = gaussian_value

        gaussian_image = cv2.GaussianBlur(color_channels[0], (5, 5), gaussian_value)

        bilateral_image = cv2.bilateralFilter(color_channels[0], 25, bilateral_value, bilateral_value)
        result_image = cv2.addWeighted(gaussian_image, 0.7, bilateral_image, 0.3, 0)
        mod_image = cv2.add(result_image, np.ones_like(color_channels[0]) * self.main_instance.brightness_now)

        cv2.imshow("Captured", mod_image)

    def gaussian_blur(self, value):
        self.apply_filters(value, self.main_instance.actual_kernel_size)

    def bilateral_blur(self, value):
        self.apply_filters(self.main_instance.actual_sigma, value)

    def change_upper_limiar(self, value):
        self.main_instance.upper_limiar = value
        self.main_instance.update_limiar_filter()

    def change_lower_limiar(self, value):
        self.main_instance.lower_limiar = value
        self.main_instance.update_limiar_filter()

    def apply_threshold(self, value):
        if self.main_instance.imagem_capturada is not None:
            imagem_azul = self.main_instance.imagem_capturada[:, :, 0]

            blue_image_8bits = cv2.convertScaleAbs(imagem_azul)

            _, binary_image = cv2.threshold(blue_image_8bits, value, 255, cv2.THRESH_BINARY)
            cv2.imshow("Captured", binary_image)


