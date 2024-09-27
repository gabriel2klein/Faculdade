import numpy as np
import matplotlib.pyplot as plt

# Definindo o vetor inicial
v = np.array([[1.2], [0.8]])  # Vetor (1.2, 0.8)

# Função para desenhar os vetores 
def plot_vector(ax, v, color='purple', label=None):
    ax.quiver(0, 0, v[0, 0], v[1, 0], angles='xy', scale_units='xy', scale=1, color=color, label=label)

# Funções de Transformações Lineares
def expand_u(v):
    return 3 * v  # Expansão  ao longo do vetor u

def contract_u(v):
    return 0.6 * v  # Contração  ao longo do vetor u

def expand_x(v):
    return np.array([[2.5 * v[0, 0]], [v[1, 0]]])  # Expansão  na direção do eixo x

def contract_x(v):
    return np.array([[0.8 * v[0, 0]], [v[1, 0]]])  # Contração na direção do eixo x

def reflect_x(v):
    return np.array([[v[0, 0]], [-v[1, 0]]])  # Reflexão sobre o eixo x

def reflect_origin(v):
    return -v  # Reflexão sobre a origem

def reflect_y_equals_x(v):
    return np.array([[v[1, 0]], [v[0, 0]]])  # Reflexão sobre a reta y = x

# Alterando o ângulo da rotação para 75 graus (π/2.4)
def rotate_clockwise(v, phi):
    rotation_matrix = np.array([[np.cos(phi), np.sin(phi)],
                                [-np.sin(phi), np.cos(phi)]])
    return rotation_matrix @ v  # Rotação horária

# Definindo o ângulo para a rotação (75 graus)
phi = np.pi / 2.4  # Ângulo de 75 graus

# Lista de transformações e suas descrições
transformations = [
    (expand_u, "Expansão ao longo de u"),
    (contract_u, "Contração ao longo de u"),
    (expand_x, "Expansão na direção x"),
    (contract_x, "Contração na direção x"),
    (reflect_x, "Reflexão sobre o eixo x"),
    (reflect_origin, "Reflexão sobre a origem"),
    (reflect_y_equals_x, "Reflexão sobre a reta y = x"),
    (lambda v: rotate_clockwise(v, phi), "Rotação horária de 75 graus")
]

# Criando o gráfico 
fig, axs = plt.subplots(3, 3, figsize=(14, 9))

# Repetindo sobre as transformações e suas descrições
for ax, (transformation, description) in zip(axs.flatten()[:len(transformations)], transformations):
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.axhline(0, color='black', lw=1)
    ax.axvline(0, color='black', lw=1)
    ax.grid(True, linestyle='--', color='lightgray')
    
    # Aplicando a transformação
    transformed_vector = transformation(v)
    
    # DEsenhando o vetor original
    plot_vector(ax, v, color='blue', label='Vetor original')
    
    # Desenhando o vetor transformado
    plot_vector(ax, transformed_vector, color='orange', label='Vetor transformado')
    
    ax.set_title(description, fontsize=12, color='darkred')
    ax.set_aspect('equal')
    ax.legend()

# Ajustando o layout
plt.tight_layout()
plt.show()
