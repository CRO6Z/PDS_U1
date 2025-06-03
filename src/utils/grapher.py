import matplotlib.pyplot as plt

def plot_signals(t_cont, t_disc, signals_cont, signals_disc, titles):
    """
    Grafica señales continuas y discretas.
    - t_cont: vector tiempo continuo (puede estar vacío si no hay señales continuas).
    - t_disc: vector tiempo discreto (puede estar vacío si no hay señales discretas).
    - signals_cont: lista de señales continuas (vacía si no aplica).
    - signals_disc: lista de señales discretas (vacía si no aplica).
    - titles: lista de títulos para cada señal.
    """
    import numpy as np

    n = max(len(signals_cont), len(signals_disc))
    fig, axs = plt.subplots(n, 1, figsize=(12, 4 * n))
    if n == 1:
        axs = [axs]

    for i in range(n):
        if signals_cont and len(signals_cont) > i and len(t_cont) > 0:
            axs[i].plot(t_cont, signals_cont[i], label='Continua')
        if signals_disc and len(signals_disc) > i and len(t_disc) > 0:
            axs[i].plot(t_disc, signals_disc[i], 'ro', markersize=3, label='Muestras (Ts=0.01s)')
        axs[i].set_title(titles[i])
        axs[i].grid(True)
        axs[i].legend()

    plt.tight_layout()
    plt.show()
