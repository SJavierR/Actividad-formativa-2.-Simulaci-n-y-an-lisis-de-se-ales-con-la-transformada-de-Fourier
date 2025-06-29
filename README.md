# Análisis de Señales en el Tiempo y Frecuencia

Este proyecto muestra cómo representar señales básicas en el dominio del tiempo y su transformación al dominio de la frecuencia usando la Transformada de Fourier con Python.

## Requisitos
- Python 3.x
- NumPy
- Matplotlib

## Señales Analizadas
- Pulso rectangular
- Escalón unitario
- Onda senoidal

## Pasos realizados
1. Se generan las señales en el dominio del tiempo.
2. Se aplica la Transformada Rápida de Fourier (`np.fft.fft()`).
3. Se grafican la magnitud y fase del espectro.
4. Se analizan propiedades como simetría, linealidad y efectos del desplazamiento y escalado.

## Ejecución
```bash
python fourier_analysis.py
