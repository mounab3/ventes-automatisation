# 🛒 Automatisation des Ventes — Projet de Fin d'Année

> **Matière : Logiciels** | Script Python d'analyse automatique de données e-commerce

---

## 📋 Description

Ce projet automatise l'analyse des ventes d'une entreprise e-commerce.
Il lit un fichier CSV, effectue des calculs financiers (CA Brut, CA Net, TVA)
et génère un rapport + des graphiques.

---

## 🗂️ Structure du projet

```
ventes_project/
│
├── analyse_ventes.py       ← Script principal (à lancer)
├── requirements.txt        ← Dépendances Python
├── README.md               ← Ce fichier
│
├── ventes.csv              ← Généré automatiquement au lancement
├── resultats_final.csv     ← Exporté après analyse
└── graphiques_ventes.png   ← Graphiques (si matplotlib installé)
```

---

## ⚙️ Installation & Lancement

### 1. Cloner le dépôt
```bash
git clone https://github.com/TON_USERNAME/ventes-automatisation.git
cd ventes-automatisation
```

### 2. Installer les dépendances (optionnel — pour les graphiques)
```bash
pip install -r requirements.txt
```

### 3. Lancer le script
```bash
python analyse_ventes.py
```

---

## 📊 Fonctionnalités

| # | Étape | Description |
|---|-------|-------------|
| 1 | Génération | Crée `ventes.csv` avec 10 produits |
| 2 | CA Brut | Prix × Quantité |
| 3 | CA Net | CA Brut × (1 − Remise%) |
| 4 | TVA | CA Net × 20% |
| 5 | Rapport | Affiche le CA total dans le terminal |
| 6 | Champion | Identifie le produit le plus rentable |
| 7 | Export | Génère `resultats_final.csv` |
| ⭐ | Bonus | 3 graphiques Matplotlib |

---

## 🧮 Formules utilisées

```
CA Brut  = Prix × Quantité
CA Net   = CA Brut × (1 − Remise / 100)
TVA      = CA Net × 0.20
CA TTC   = CA Net + TVA
```

---

## 💡 Exemple de sortie terminal

```
🛒 🛒 🛒 🛒 🛒 🛒 🛒 🛒 🛒 🛒
   DÉMARRAGE — Analyse automatique des ventes

✅ Fichier 'ventes.csv' généré avec 10 produits.

════════════════════════════════════════
  📊  RAPPORT DE VENTES
════════════════════════════════════════
  ID   Prix  Qté  Remise   CA Brut    CA Net     TVA    CA TTC
────────────────────────────────────────
  101  15.00    3     10%    45.00     40.50    8.10    48.60
  ...
════════════════════════════════════════
  💰 CA Total (HT) : 1025.60 €
  🏦 TVA collectée : 205.12 €
  🧾 CA Total (TTC): 1230.72 €

  🏆 Meilleur produit : ID 107 → CA Net = 216.00 €
```

---

*Projet réalisé dans le cadre du cours Logiciels — 2025*