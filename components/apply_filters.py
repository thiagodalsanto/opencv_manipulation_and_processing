import cv2
import numpy as np

class ApplyFilters:
    def __init__(self, main_instance):
        self.main_instance = main_instance

    def apply_filters(self, valor_gaussian, valor_bilateral):
        canais_de_cor = cv2.split(self.main_instance.imagem_capturada)
        self.main_instance.brilho_atual = valor_gaussian

        imagem_gaussian = cv2.GaussianBlur(canais_de_cor[0], (5, 5), valor_gaussian)

        imagem_bilateral = cv2.bilateralFilter(canais_de_cor[0], 25, valor_bilateral, valor_bilateral)
        imagem_resultante = cv2.addWeighted(imagem_gaussian, 0.7, imagem_bilateral, 0.3, 0)
        imagem_modificada = cv2.add(imagem_resultante, np.ones_like(canais_de_cor[0]) * self.main_instance.brilho_atual)

        cv2.imshow("Imagem Capturada", imagem_modificada)

    def gaussian_blur(self, valor):
        self.apply_filters(valor, self.main_instance.kernel_size_atual)

    def bilateral_blur(self, valor):
        self.apply_filters(self.main_instance.sigma_atual, valor)

    def change_upper_limiar(self, valor):
        self.main_instance.upper_limiar = valor
        self.main_instance.update_limiar_filter()

    def change_lower_limiar(self, valor):
        self.main_instance.lower_limiar = valor
        self.main_instance.update_limiar_filter()

    def apply_threshold(self, valor):
        if self.main_instance.imagem_capturada is not None:
            imagem_azul = self.main_instance.imagem_capturada[:, :, 0]  # Canal Azul (Blue)

            # Aplicar a conversão para 8 bits
            imagem_azul_8bits = cv2.convertScaleAbs(imagem_azul)

            _, imagem_binaria = cv2.threshold(imagem_azul_8bits, valor, 255, cv2.THRESH_BINARY)
            cv2.imshow("Imagem Capturada", imagem_binaria)


