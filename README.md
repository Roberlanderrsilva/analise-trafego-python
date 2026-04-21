
import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados
caminho_log = '/var/log/apache2/access.log'
df = pd.read_csv(caminho_log, sep=' ', header=None, usecols=[0], names=['IP'])

# 2. Pegar os top 10 IPs (agora teremos vários!)
top_ips = df['IP'].value_counts().head(10)

# 3. Criar o Visual Profissional
plt.figure(figsize=(10, 6))
# Usando cores variadas para ficar bonitão
cores = ['#2ecc71', '#3498db', '#9b59b6', '#f1c40f', '#e67e22', '#e74c3c', '#1abc9c', '#34495e', '#d35400', '#c0392b']
top_ips.plot(kind='bar', color=cores)

# Customização de Elite
plt.title('DASHBOARD DE TRÁFEGO - SERVIDOR LUBUNTU (ROBERLANDE)', fontsize=14, fontweight='bold')
plt.xlabel('Endereço IP do Visitante', fontsize=12)
plt.ylabel('Total de Requisições', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

# Salvar e mostrar
plt.savefig('dashboard_final.png')
print("\n🔥 SUCESSO! O Dashboard 'dashboard_final.png' foi gerado com volume de dados!")
plt.show()
