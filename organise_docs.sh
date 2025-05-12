# Se placer dans le dossier docs (le créer s'il n'existe pas)
mkdir -p ~/MesProjets/Projet3_Interventions_Francophones/docs
cd ~/MesProjets/Projet3_Interventions_Francophones/docs

# Créer la structure de dossiers
mkdir -p assets/visualisations assets/raw_data analysis

# Aller dans le dossier parent pour chercher les fichiers
cd ..

# Déplacer les fichiers .png s'ils existent
for f in *.png; do
  [ -e "$f" ] && mv "$f" docs/assets/visualisations/
done

# Déplacer banner.png s’il existe
[ -f banner.png ] && mv banner.png docs/assets/visualisations/

# Renommer le fichier principal de visualisation s’il existe
[ -f docs/assets/visualisations/interventions_visualisation_pro.png ] && mv docs/assets/visualisations/interventions_visualisation_pro.png docs/assets/visualisations/interventions.png

# Supprimer les doublons s’ils existent
rm -f docs/interventions_pro.png docs/interventions_visualisation.png

# Créer le fichier README dans le dossier docs
cat > docs/README_DOCS.md << 'EOF'
# Documentation du Projet

## Structure des fichiers

- `assets/visualisations/` : Contient tous les graphiques générés
- `analysis/` : Analyses détaillées au format Markdown
- `assets/raw_data/` : Données brutes utilisées pour les analyses

## Mise à jour

1. Générer les nouvelles visualisations
2. Placer les fichiers dans les dossiers appropriés
3. Mettre à jour ce document si la structure change
EOF
