import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Probabilidades de pasar por cada lugar
P_L = [0.2, 0.1, 0.5, 0.2]

# Probabilidad de multa dado que pasa por cada lugar
P_M_dado_L = [0.4, 0.3, 0.2, 0.3]

lugares = ['L1', 'L2', 'L3', 'L4']

fig, ax = plt.subplots(figsize=(10, 5))

x = 0

for i in range(4):

    ancho = P_L[i]
    altura_multa = P_M_dado_L[i]

    # Región completa correspondiente a Li
    rect_lugar = Rectangle(
        (x, 0),
        ancho,
        1,
        fill=False,
        linewidth=2
    )
    ax.add_patch(rect_lugar)

    # Región donde ocurre la multa
    rect_multa = Rectangle(
        (x, 0),
        ancho,
        altura_multa,
        alpha=0.4
    )
    ax.add_patch(rect_multa)

    # Probabilidad conjunta
    conjunta = P_L[i] * P_M_dado_L[i]

    # Nombre del lugar
    ax.text(
        x + ancho/2,
        0.85,
        f'{lugares[i]}\nP={P_L[i]}',
        ha='center',
        va='center',
        fontsize=12
    )

    # Probabilidad de multa
    ax.text(
        x + ancho/2,
        altura_multa/2,
        f'M ∩ {lugares[i]}\n{conjunta:.2f}',
        ha='center',
        va='center',
        fontsize=11
    )

    x += ancho


ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

ax.set_xlabel('Probabilidad de pasar por cada lugar')
ax.set_ylabel('Probabilidad de que el radar esté operando')

ax.set_title('Diagrama de áreas del problema de los radares')

plt.tight_layout()
plt.show()
