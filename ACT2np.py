import numpy as np
import matplotlib.pyplot as plt

# Parámetros generales
fs = 1000  # Frecuencia de muestreo
t = np.arange(-1, 1, 1/fs)  # Tiempo de -1s a 1s

def plot_time_and_freq(signal, title):
    # FFT
    N = len(signal)
    fft_signal = np.fft.fft(signal)
    fft_freqs = np.fft.fftfreq(N, d=1/fs)
    fft_magnitude = np.abs(fft_signal)
    fft_phase = np.angle(fft_signal)

    # Reordenamos las frecuencias para visualización
    idx = np.fft.fftshift(np.arange(N))
    fft_freqs_shifted = np.fft.fftshift(fft_freqs)
    fft_magnitude_shifted = np.fft.fftshift(fft_magnitude)
    fft_phase_shifted = np.fft.fftshift(fft_phase)

    # Gráficas
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(t, signal)
    plt.title(f'{title} - Dominio del tiempo')
    plt.xlabel('Tiempo [s]')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(fft_freqs_shifted, fft_magnitude_shifted)
    plt.title('Espectro de Magnitud')
    plt.xlabel('Frecuencia [Hz]')
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(fft_freqs_shifted, fft_phase_shifted)
    plt.title('Espectro de Fase')
    plt.xlabel('Frecuencia [Hz]')
    plt.grid()

    plt.tight_layout()
    plt.show()

# Señal 1: Pulso rectangular
rect_pulse = np.where(np.abs(t) < 0.2, 1.0, 0.0)
plot_time_and_freq(rect_pulse, 'Pulso Rectangular')

# Señal 2: Escalón unitario
step = np.where(t >= 0, 1.0, 0.0)
plot_time_and_freq(step, 'Escalón Unitario')

# Señal 3: Senoidal
freq_sin = 50  # Hz
sine_wave = np.sin(2 * np.pi * freq_sin * t)
plot_time_and_freq(sine_wave, 'Onda Senoidal de 50 Hz')
