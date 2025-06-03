import numpy as np
from scipy import signal
from src.utils.grapher import plot_signals

# Parámetros globales
f = 2
Ts = 0.01
t_cont = np.linspace(-1, 5, 5000)
t_disc = np.arange(-1, 5 + Ts, Ts)

def actividad_1():
    """Calcula y grafica las 4 señales continuas y discretas superpuestas."""
    # Definición de las señales
    def x1(t):
        return np.sin(2 * np.pi * f * t)

    def x2(t):
        u = (t >= 0).astype(float)
        return np.exp(-2 * t) * u

    def x3(t):
        return signal.sawtooth(2 * np.pi * f * t, width=0.5)

    def x4(t):
        return signal.square(2 * np.pi * f * t)

    # Cálculo señales continuas
    x1_cont = x1(t_cont)
    x2_cont = x2(t_cont)
    x3_cont = x3(t_cont)
    x4_cont = x4(t_cont)

    # Cálculo señales discretas
    x1_disc = x1(t_disc)
    x2_disc = x2(t_disc)
    x3_disc = x3(t_disc)
    x4_disc = x4(t_disc)

    titles = [
        'Señal sinusoidal (f=2 Hz)',
        'Señal exponencial amortiguada',
        'Señal triangular (f=2 Hz)',
        'Señal cuadrada (f=2 Hz)'
    ]

    plot_signals(
        t_cont, t_disc,
        [x1_cont, x2_cont, x3_cont, x4_cont],
        [x1_disc, x2_disc, x3_disc, x4_disc],
        titles
    )
