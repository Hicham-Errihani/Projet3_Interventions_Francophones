#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd

# Configuration manuelle du style (alternative à seaborn)
params = {
    'font.family': 'sans-serif',
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.figsize': (10, 6)
}
plt.rcParams.update(params)

# Données
data = {
    'Type': ['Communications scientifiques', 'Conférences internationales'],
    'Nombre': [352148, 125000]
}
df = pd.DataFrame(data)

# Création du graphique
fig, ax = plt.subplots()
bars = ax.bar(df['Type'], df['Nombre'], 
             color=['#1f77b4', '#ff7f0e'],  # Couleurs standard
             width=0.6)

# Personnalisation
ax.set_title('RÉPARTITION DES INTERVENTIONS FRANCOPHONES', 
            pad=20, fontweight='bold')
ax.set_xlabel('Type d\'intervention')
ax.set_ylabel('Nombre d\'occurrences')

# Format des nombres
ax.yaxis.set_major_formatter(lambda x, pos: f'{int(x):,}'.replace(',', ' '))

# Valeurs sur les barres
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 5000,
            f'{height:,}'.replace(',', ' '),
            ha='center', va='bottom')

plt.tight_layout()
plt.savefig('docs/interventions_pro.png', dpi=300)
print("Graphique généré avec succès dans docs/interventions_pro.png")
