import matplotlib.pyplot as plt
import pandas as pd

# QUERY 1:
threads_q1_no_error = [1, 2, 5, 10, 20, 30, 50, 75, 100, 150]
latencia_q1_no_error = [43079, 56071, 60786, 83317, 166889, 284856, 440328, 696942, 876011, 1245423]

# QUERY 1:
requisicoes_q1_error = [1, 2, 40, 60]
latencia_q1_error = [31686, 31041, 30613, 30916]

# QUERY 2
usuarios_q2_leve = [1, 2, 5, 10, 20, 50, 75, 100, 150, 200, 300, 400, 500]
latencia_q2_leve_usuarios = [220, 227, 250, 286, 443, 1325, 2336, 3285, 4714, 6289, 8978, 13252, 8768]

# QUERY 2:
requisicoes_q2_leve = [1, 2, 5, 10, 20, 50, 75, 100, 150, 200, 300, 400, 500, 750, 1000, 2000, 5000]
latencia_q2_leve_requisicoes = [225, 220, 180, 172, 163, 156, 153, 146, 148, 145, 149, 148, 150, 148, 148, 151, 159]

fig, axs = plt.subplots(2, 2, figsize=(18, 14))
fig.suptitle('BD2 - Testes de Estresse de Banco', fontsize=20, y=1.02)

# Gráfico 1
axs[0, 0].plot(threads_q1_no_error, latencia_q1_no_error, marker='o', linestyle='-', color='blue')
axs[0, 0].set_xlabel('Threads', fontsize=12)
axs[0, 0].set_ylabel('Latência Média', fontsize=12)
axs[0, 0].set_title('Query Pesada: Latência vs. Threads', fontsize=14)
axs[0, 0].grid(True)
axs[0, 0].ticklabel_format(axis='y', style='plain')
axs[0, 0].annotate(f'{latencia_q1_no_error[-1]} ms', (threads_q1_no_error[-1], latencia_q1_no_error[-1]),
                   textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='green')


# Gráfico 2
axs[0, 1].plot(requisicoes_q1_error, latencia_q1_error, marker='o', linestyle='-', color='green')
axs[0, 1].set_xlabel('Número de Requisições', fontsize=12)
axs[0, 1].set_ylabel('Latência Média', fontsize=12)
axs[0, 1].set_title('Query Pesada: Latência vs. Requisições (Erro ou Latência Inaceitável)', fontsize=14)
axs[0, 1].grid(True)
axs[0, 1].ticklabel_format(axis='y', style='plain')
axs[0, 1].annotate('Mesmo com queries infinitas não resultaram erro', xy=(requisicoes_q1_error[-1], latencia_q1_error[-1]),
                   textcoords="offset points", xytext=(-50,20), ha='center', fontsize=10, color='green')


# Gráfico 3
axs[1, 0].plot(usuarios_q2_leve, latencia_q2_leve_usuarios, marker='o', linestyle='-', color='red')
axs[1, 0].set_xlabel('Threads', fontsize=12)
axs[1, 0].set_ylabel('Latência Média', fontsize=12)
axs[1, 0].set_title('Query Mais Leve: Latência vs. Threads', fontsize=14)
axs[1, 0].grid(True)
# Indicação
axs[1, 0].annotate('Erro em 44.80% das Queries', xy=(500, 8768), xytext=(450, 11000),
                   fontsize=10, color='red')

# Gráfico 4
axs[1, 1].plot(requisicoes_q2_leve, latencia_q2_leve_requisicoes, marker='o', linestyle='-', color='purple')
axs[1, 1].set_xlabel('Número de Requisições', fontsize=12)
axs[1, 1].set_ylabel('Latência Média', fontsize=12)
axs[1, 1].set_title('Query Mais Leve: Latência vs. Requisições', fontsize=14)
axs[1, 1].grid(True)
axs[1, 1].annotate(f'{latencia_q2_leve_requisicoes[-1]} ms em {requisicoes_q2_leve[-1]} requisições',
                   xy=(requisicoes_q2_leve[-1], latencia_q2_leve_requisicoes[-1]),
                   textcoords="offset points", xytext=(-50,10), ha='center', fontsize=10, color='green')

plt.subplots_adjust(hspace=0.5)
plt.tight_layout(rect=[0, 0.08, 1, 0.95])
plt.show()