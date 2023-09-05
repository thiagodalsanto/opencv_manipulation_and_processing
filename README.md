## OpenCV Manipulation and Processing
Projeto com uma aplicação simples de interface gráfica (GUI) desenvolvida utilizando a biblioteca Tkinter do Python para Manipulação e Processamento da captura de um frame de um vídeo. A aplicação permite aos usuários capturar um frame de um vídeo e realizar várias manipulações Filtros Passa-Baixa, Passa-Alta, Limiar e Threshold, utilizando OpenCV.

## Sobre o trabalho:

* Disciplina: OP63I-CC8 - Processamento De Imagens E Reconhecimento De Padrões	
* Turma: 2023/2 - 8º Período
* Docente: Pedro Luiz de Paula Filho

## Recursos 
- **Captura de Frame do Vído:** Ao clicar no botão "Capturar", um frame do vídeo é capturado em formato PNG e enviado para a tela de manipulação.
- **Manipulações:** O sistema conta com manipulações de filtro passa-baixa *Gaussian Blur*, *Bilateral Blur*, Limiares Inferior e Superior e controle de *Threshold*.
- **Binarização Automática:** Binatização é feita automáticamente no frame escolhido, fazendo com que a imagem, sempre seja binarizada.
- **Conversão para uma Banda:** A captura de frame sempre estará em 8-bits, já que ela sempre trabalhará no Canal 0 (Blue).
- **Visualização do Canal RGB de um Ponto:** Ao clicar em alguma parte da imagem, ela mostrará em console a cor do local, no vídeo original, sem edições, em formato RGB.

## Dependências
Siga essa ordem de instalação para ambos os sistemas operacionais, para garantir que não exista conflito de versões:

### Para o Linux:
1. Python 3 `pip install python3`
2. NumPy `pip install numpy`
3. OpenCV (cv2) `pip install opencv-python`
4. Tkinter (`sudo apt-get install python3-tk`)

### Para o Windows:
1. Python 3.11.5 ([Instalador 64-bit](https://www.python.org/downloads/windows/))
2. NumPy `pip install numpy`
3. OpenCV `pip install opencv-python`

Obs.: Tkinter já vem instalado junto com o Python, para versões no Windows.

## Como Utilizar

1. Clone o repositório do GitHub: `git clone https://github.com/thiagodalsanto/opencv_manipulation_and_processing.git`
2. Instale as [dependências](#dependências) utilizadas.
3. Execute o aplicativo em uma IDE com o comando `python3 main.py`

## Imagens do Programa

Imagem 1 - Tela inicial da Aplicação, com um vídeo rodando e a opção de capturar o Frame atual do vídeo.
![Imagem1](https://i.imgur.com/HZdwTvv.png)

Imagem 2 - Após clicar em "Capturar". Apenas com filtros passa-baixa aplicados (*Gaussian Blur* e *Bilateral Blur*).
![Imagem2](https://i.imgur.com/VxZDEci.png)  

Imagem 3 - Manipulação com filtros passa-baixa aplicados (*Gaussian Blur* e *Bilateral Blur*) e Limiares (*Upper Limiar* e *Lower Limiar*).
![Imagem3](https://i.imgur.com/E1KxJMp.png)  

Imagem 4 - Manipulação apenas com o *Threshold* ativado, sempre para o Canal 0 (*Blue*).
![Imagem4](https://i.imgur.com/Mdilr9R.png)  
