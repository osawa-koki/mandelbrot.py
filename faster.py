import numpy as np
import matplotlib.pyplot as plt
import concurrent.futures

# 複素数を扱うためにnp.complex128型を使用する
def mandelbrot(c, maxiter):
    z = c
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return maxiter

# マンデルブロ集合を描写する範囲を指定する
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5

# マンデルブロ集合を計算するためのグリッドを作成する
xs = np.linspace(xmin, xmax, 1000)
ys = np.linspace(ymin, ymax, 1000)
zs = np.empty((len(xs), len(ys)))

with concurrent.futures.ThreadPoolExecutor() as executor:
    zs = list(executor.map(lambda xy: mandelbrot(xy[0], xy[1]), [(x + y*1j, 50) for x in xs for y in ys]))
zs = np.array(zs).reshape((len(xs), len(ys)))

# マンデルブロ集合を描写する
plt.imshow(zs.T, cmap='bone', extent=(xmin, xmax, ymin, ymax))
plt.savefig('mandelbrot.png')
