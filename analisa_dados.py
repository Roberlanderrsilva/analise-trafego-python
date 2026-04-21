import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados do Apache
caminho_log = '/var/log/apache2/access.log'
colunas = ['IP', 'Ident', 'User', 'Data', 'Fuso', 'Metodo', 'Status', 'Tamanho']
# Lendo o log (pegando apenas IP e Status)
df = pd.read_csv(caminho_log, sep=' ', header=None, usecols=[0, 8], names=['IP', 'Status'])

# 2. Processar: Contar quantos acessos cada IP fez
top_ips = df['IP'].value_counts().head(5)

# 3. Mostrar no Terminal (O Insight)
print("\n" + "="*30)
print(" RELATÓRIO DE TRÁFEGO ")
print("="*30)
print(top_ips)
print("="*30)

# 4. CRIAR O VISUAL (O Dashboard de Barras)
top_ips.plot(kind='bar', color='green')
plt.title('Top 5 IPs que mais acessaram o Servidor')
plt.xlabel('Endereço IP')
plt.ylabel('Quantidade de Acessos')
plt.tight_layout()

# Salvar o gráfico para você postar no LinkedIn
plt.savefig('meu_dashboard.png')
print("\n✅ Dashboard gerado e salvo como 'meu_dashboard.png'!")
plt.show() # Isso vai abrir uma janela com o gráfico na sua tela!
