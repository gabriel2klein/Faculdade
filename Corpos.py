import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do movimento circular
raio = 5  # Raio da trajetória circular
velocidade_angular = 2  # Velocidade angular em radianos por segundo
tempo_total = 30  # Tempo total de simulação (em segundos)
n_pontos = 3000  # Número de pontos para resolução

# Vetor tempo
t = np.linspace(0, tempo_total, n_pontos)

# Cálculo das posições x e y ao longo do tempo
x = raio * np.cos(velocidade_angular * t)
y = raio * np.sin(velocidade_angular * t)

# Criando da figura
plt.figure(figsize=(8, 8))

# Desenhando a trajetória circular
plt.plot(x, y, color='purple', alpha=0.6, linewidth=1.5, label='Trajetória Circular')

# Adicionar pontos destacados na trajetória
n_pontos_marcados = 5  # Número de pontos destacados
indices_escolhidos = np.linspace(0, n_pontos - 1, n_pontos_marcados, dtype=int)

# Cores para os pontos destacados
cores_pontos = ['red', 'blue', 'green', 'orange', 'cyan']
for i, idx in enumerate(indices_escolhidos):
    plt.plot(x[idx], y[idx], 'o', color=cores_pontos[i], markersize=8, label=f'Corpo (t={t[idx]:.2f}s)')

# Configurações adicionais do gráfico
plt.title('Movimento Circular com Múltiplas Voltas e Pontos Destacados', fontsize=14)
plt.xlabel('Posição X', fontsize=12)
plt.ylabel('Posição Y', fontsize=12)
plt.xlim(-raio-1, raio+1)
plt.ylim(-raio-1, raio+1)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, linestyle='--', color='lightgray')

# Mostrar o gráfico
plt.show()

# Mostrar detalhes dos corpos nos pontos marcados
for i, idx in enumerate(indices_escolhidos):
    print(f"Detalhes do corpo no tempo t = {t[idx]:.2f}s:")
    print(f"  Posição X: {x[idx]:.2f} m")
    print(f"  Posição Y: {y[idx]:.2f} m")
    print(f"  Velocidade Angular: {velocidade_angular} rad/s")
    print("-" * 50)
