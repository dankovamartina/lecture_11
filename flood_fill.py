import matplotlib.pyplot as plt
import numpy as np


def flood_fill(obraz, x, y):
    """
    :param obraz: array cisel, pixely popredi (tam budeme rozsirovat) maji hodnotu 1, pixely zabrany hodnotu 0 a prebarvene pixely hodnotu 2
    :param x: x souradnice pozice aktualniho pixelu
    :param y: y souradnice pozice aktualniho pixelu
    :return: novy obraz
    """
    # pokud je obarvovany pixel mimo obraz
    x_max, y_max = obraz.shape
    if x > x_max -1 or y>y_max -1 or x<0 or y<0:
        return obraz
    elif obraz[x, y] == 0 or obraz[x, y] == 2:
        return obraz
    elif obraz[x, y] == 1:
        obraz[x, y] = 2
        plt.imshow(obraz, cmap="gray")
        plt.show(block=False)
        plt.pause(0.0003)
        plt.clf()
        obraz = flood_fill(obraz, x+1, y)
        obraz = flood_fill(obraz, x - 1, y)
        obraz = flood_fill(obraz, x, y+1)
        obraz = flood_fill(obraz, x, y-1)
        return obraz

def main():
    #img = plt.imread("files/img0.png")[:, :, 0]
    img = plt.imread("files/img1.png")[:, :, 0]
    #img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
