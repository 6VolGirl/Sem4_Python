import numpy as np
from scipy.interpolate import interp1d
import os


class RefractiveIndex:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не найден.")

        wavelengths = []
        real_part = []
        imag_part = []

        with open(file_path, 'r') as f:
            for line in f:
                if line.strip() == '':
                    continue
                parts = line.strip().split('\t')
                if len(parts) != 3:
                    continue
                try:
                    wl = float(parts[0])
                    re = float(parts[1])
                    im = float(parts[2])
                    wavelengths.append(wl)
                    real_part.append(re)
                    imag_part.append(im)
                except ValueError:
                    continue

        self.wavelengths = np.array(wavelengths)
        self.real_part = np.array(real_part)
        self.imag_part = np.array(imag_part)

        self.real_interp = interp1d(self.wavelengths, self.real_part, kind='linear', fill_value="extrapolate")
        self.imag_interp = interp1d(self.wavelengths, self.imag_part, kind='linear', fill_value="extrapolate")

    def __call__(self, wavelength):
        """
        Возвращает комплексный показатель преломления для заданной длины волны.
        """
        real = self.real_interp(wavelength)
        imag = self.imag_interp(wavelength)
        return real + 1j * imag

    def get_range(self):
        return self.wavelengths.min(), self.wavelengths.max()

    def plot(self):
        """График показателя преломления от длины волны"""
        import matplotlib.pyplot as plt
        x = np.linspace(self.wavelengths.min(), self.wavelengths.max(), 500)
        y_real = self.real_interp(x)
        y_imag = self.imag_interp(x)

        plt.figure(figsize=(10, 6))
        plt.plot(x, y_real, label="Re(n)", color='blue')
        plt.plot(x, y_imag, label="Im(n)", color='red')
        plt.xlabel("Длина волны (нм)")
        plt.ylabel("Показатель преломления")
        plt.title("Комплексный показатель преломления TiO₂")
        plt.legend()
        plt.grid(True)
        plt.show()



ri = RefractiveIndex("TiO2.rfi")

wavelength = 500
n = ri(wavelength)
print(f"Показатель преломления при λ = {wavelength} нм: {n}")

wls = np.linspace(400, 700, 100)
ns = ri(wls)

ri.plot()