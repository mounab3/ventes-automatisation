"""
╔══════════════════════════════════════════════════════════════╗
║          🛒 AUTOMATISATION DES VENTES — E-COMMERCE          ║
║              Projet de Fin d'Année — Logiciels               ║
╚══════════════════════════════════════════════════════════════╝
 
Ce script Python automatise l'analyse des données de ventes
d'une entreprise e-commerce. Il lit un fichier CSV, effectue
des calculs financiers, génère un rapport et des graphiques.
 
Auteur : Mouna Belhiba, Mariem Saffar, Chawk Mejri
Date   : 2025
"""
 
# ─────────────────────────────────────────────
#  📦 IMPORTATION DES BIBLIOTHÈQUES
# ─────────────────────────────────────────────
import csv          # Pour lire et écrire des fichiers CSV
import os           # Pour gérer les fichiers et dossiers
import sys          # Pour quitter le programme proprement
import random       # Pour générer des données aléatoires
import pandas as pd # Pour créer et manipuler les données CSV

# Matplotlib est optionnel — pour les graphiques (Bonus)
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("⚠️  matplotlib non installé — graphiques désactivés.")
    print("   Pour l'installer : pip install matplotlib\n")
 
# ─────────────────────────────────────────────
#  ⚙️  CONSTANTES GLOBALES
# ─────────────────────────────────────────────
TAUX_TVA = 0.20          # TVA française = 20%
FICHIER_ENTREE  = "ventes.csv"
FICHIER_SORTIE  = "resultats_final.csv"
 
 
# ══════════════════════════════════════════════
#  ÉTAPE 1 — Générer le fichier ventes.csv
# ══════════════════════════════════════════════
def generer_ventes_csv(chemin: str = FICHIER_ENTREE) -> None:
    """
    Crée le fichier ventes.csv avec 3000 lignes aléatoires.

    Chaque ligne représente une vente :
      - ID       : identifiant unique du produit (commence à 1001)
      - Prix     : prix unitaire aléatoire entre 5.0 et 500.0 €
      - Quantite : quantité aléatoire entre 1 et 50
      - Remise   : remise choisie parmi [0, 5, 10, 15, 20, 25, 30] %
    
    Utilise pandas pour créer le fichier CSV proprement.
    """

    # ── Génération de 3000 lignes aléatoires ────────────
    lignes = []
    for i in range(1, 5):
        lignes.append({
            'ID'      : 1000 + i,                              # ID unique
            'Prix'    : round(random.uniform(5.0, 500.0), 2),  # Prix aléatoire
            'Quantite': random.randint(1, 50),                  # Quantité aléatoire
            'Remise'  : random.choice([0, 5, 10, 15, 20, 25, 30])  # Remise aléatoire
        })

    # ── Création du fichier CSV avec pandas ─────────────
    df = pd.DataFrame(lignes)   # Convertit la liste en tableau pandas
    df.to_csv(chemin, index=False)  # Sauvegarde en CSV sans numéro de ligne

    print(f"✅ Fichier '{chemin}' généré avec {len(lignes)} produits aléatoires.\n")
 
 
# ══════════════════════════════════════════════
#  ÉTAPE 2 & 3 & 4 — Lire et calculer
# ══════════════════════════════════════════════
def calculer_resultats(chemin: str = FICHIER_ENTREE) -> list[dict]:
    """
    Lit ventes.csv et calcule pour chaque ligne :
      - CA Brut  = Prix × Quantité
      - CA Net   = CA Brut × (1 − Remise/100)
      - TVA      = CA Net × 20%
      - CA TTC   = CA Net + TVA
 
    Retourne une liste de dictionnaires (une entrée par produit).
    """
    if not os.path.exists(chemin):
        print(f"❌ Erreur : le fichier '{chemin}' est introuvable.")
        sys.exit(1)
 
    resultats = []
 
    with open(chemin, mode="r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f)   # Lecture avec en-tête comme clés
 
        for ligne in lecteur:
            # ── Lecture des valeurs brutes ──────────────────────
            id_produit = int(ligne["ID"])
            prix       = float(ligne["Prix"])
            quantite   = int(ligne["Quantite"])
            remise     = float(ligne["Remise"])   # en %
 
            # ── Calculs financiers ──────────────────────────────
            ca_brut = prix * quantite                          # Étape 2
            ca_net  = ca_brut * (1 - remise / 100)            # Étape 3
            tva     = ca_net * TAUX_TVA                       # Étape 4
            ca_ttc  = ca_net + tva                            # Total TTC
 
            # ── Stockage du résultat ────────────────────────────
            resultats.append({
                "ID"       : id_produit,
                "Prix"     : prix,
                "Quantite" : quantite,
                "Remise"   : remise,
                "CA_Brut"  : round(ca_brut, 2),
                "CA_Net"   : round(ca_net,  2),
                "TVA"      : round(tva,     2),
                "CA_TTC"   : round(ca_ttc,  2),
            })
 
    return resultats
 
 
# ══════════════════════════════════════════════
#  ÉTAPE 5 — Afficher le CA Total
# ══════════════════════════════════════════════
def afficher_rapport(resultats: list[dict]) -> None:
    """
    Affiche un tableau récapitulatif dans le terminal,
    avec le chiffre d'affaires total de l'entreprise.
    """
    largeur = 72
    ligne_sep = "─" * largeur
 
    print("\n" + "═" * largeur)
    print("  📊  RAPPORT DE VENTES — CHIFFRE D'AFFAIRES".center(largeur))
    print("═" * largeur)
 
    # En-tête du tableau
    print(f"  {'ID':>4}  {'Prix':>7}  {'Qté':>4}  {'Remise':>6}  "
          f"{'CA Brut':>9}  {'CA Net':>9}  {'TVA':>7}  {'CA TTC':>9}")
    print(ligne_sep)
 
    # Lignes de données
    for r in resultats:
        print(f"  {r['ID']:>4}  {r['Prix']:>7.2f}  {r['Quantite']:>4}  "
              f"{r['Remise']:>5.0f}%  {r['CA_Brut']:>9.2f}  "
              f"{r['CA_Net']:>9.2f}  {r['TVA']:>7.2f}  {r['CA_TTC']:>9.2f}")
 
    print(ligne_sep)
 
    # ── Totaux ──────────────────────────────────────────────
    total_brut = sum(r["CA_Brut"] for r in resultats)
    total_net  = sum(r["CA_Net"]  for r in resultats)
    total_tva  = sum(r["TVA"]     for r in resultats)
    total_ttc  = sum(r["CA_TTC"]  for r in resultats)
 
    print(f"  {'TOTAL':<17}{'':>13}  {total_brut:>9.2f}  "
          f"{total_net:>9.2f}  {total_tva:>7.2f}  {total_ttc:>9.2f}")
    print("═" * largeur)
 
    # ── Message de résumé ───────────────────────────────────
    print(f"\n  💰  CA Total (HT) : {total_net:.2f} €")
    print(f"  🏦  TVA collectée : {total_tva:.2f} €")
    print(f"  🧾  CA Total (TTC): {total_ttc:.2f} €\n")
 
 
# ══════════════════════════════════════════════
#  ÉTAPE 6 — Meilleur produit
# ══════════════════════════════════════════════
def meilleur_produit(resultats: list[dict]) -> dict:
    """
    Identifie le produit ayant généré le CA Net le plus élevé.
    Utilise la fonction max() avec une clé de tri sur CA_Net.
    """
    champion = max(resultats, key=lambda r: r["CA_Net"])
    print(f"  🏆  Meilleur produit : ID {champion['ID']} "
          f"→ CA Net = {champion['CA_Net']:.2f} €")
    print()
    return champion
 
 
# ══════════════════════════════════════════════
#  ÉTAPE 7 — Exporter resultats_final.csv
# ══════════════════════════════════════════════
def exporter_resultats(resultats: list[dict],
                       chemin: str = FICHIER_SORTIE) -> None:
    """
    Exporte toutes les colonnes (originales + calculées)
    dans un nouveau fichier CSV : resultats_final.csv
    """
    colonnes = ["ID", "Prix", "Quantite", "Remise",
                "CA_Brut", "CA_Net", "TVA", "CA_TTC"]
 
    with open(chemin, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=colonnes)
        writer.writeheader()       # Écrit l'en-tête
        writer.writerows(resultats)
 
    print(f"✅ Résultats exportés dans '{chemin}'.\n")
 
 
# ══════════════════════════════════════════════
#  BONUS — Graphiques Matplotlib
# ══════════════════════════════════════════════
def afficher_graphiques(resultats: list[dict]) -> None:
    """
    [BONUS] Génère 3 graphiques avec Matplotlib :
      1. Barres : CA Net par produit
      2. Camembert : répartition des CA
      3. Barres empilées : CA Net vs TVA
    Sauvegarde les graphiques dans 'graphiques_ventes.png'.
    """
    if not MATPLOTLIB_AVAILABLE:
        print("⚠️  Graphiques ignorés (matplotlib absent).\n")
        return
 
    ids    = [str(r["ID"])    for r in resultats]
    ca_net = [r["CA_Net"]     for r in resultats]
    tva    = [r["TVA"]        for r in resultats]
 
    # Palette de couleurs personnalisée
    couleurs = ["#2ecc71", "#3498db", "#e74c3c", "#f39c12", "#9b59b6",
                "#1abc9c", "#e67e22", "#34495e", "#e91e63", "#00bcd4"]
 
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle("📊 Tableau de Bord des Ventes — E-Commerce",
                 fontsize=16, fontweight="bold", color="#2c3e50")
    fig.patch.set_facecolor("#f8f9fa")
 
    # ── Graphique 1 : CA Net par produit ────────────────────
    ax1 = axes[0]
    barres = ax1.bar(ids, ca_net, color=couleurs, edgecolor="white",
                     linewidth=1.5, zorder=3)
    ax1.set_title("CA Net par Produit (€)", fontweight="bold")
    ax1.set_xlabel("ID Produit")
    ax1.set_ylabel("Euros (€)")
    ax1.grid(axis="y", linestyle="--", alpha=0.5, zorder=0)
    ax1.set_facecolor("#ecf0f1")
    # Étiquettes au-dessus des barres
    for b, val in zip(barres, ca_net):
        ax1.text(b.get_x() + b.get_width() / 2, b.get_height() + 1,
                 f"{val:.0f}€", ha="center", va="bottom", fontsize=8)
 
    # ── Graphique 2 : Répartition en camembert ───────────────
    ax2 = axes[1]
    wedges, texts, autotexts = ax2.pie(
        ca_net, labels=ids, colors=couleurs,
        autopct="%1.1f%%", startangle=140,
        wedgeprops={"edgecolor": "white", "linewidth": 2}
    )
    for t in autotexts:
        t.set_fontsize(8)
    ax2.set_title("Répartition du CA Net (%)", fontweight="bold")
 
    # ── Graphique 3 : CA Net vs TVA (barres empilées) ────────
    ax3 = axes[2]
    x = range(len(ids))
    ax3.bar(x, ca_net, label="CA Net (HT)", color="#3498db",
            edgecolor="white", linewidth=1.2)
    ax3.bar(x, tva, bottom=ca_net, label="TVA (20%)", color="#e74c3c",
            edgecolor="white", linewidth=1.2, alpha=0.85)
    ax3.set_xticks(x)
    ax3.set_xticklabels(ids)
    ax3.set_title("CA Net + TVA par Produit", fontweight="bold")
    ax3.set_xlabel("ID Produit")
    ax3.set_ylabel("Euros (€)")
    ax3.legend()
    ax3.set_facecolor("#ecf0f1")
    ax3.grid(axis="y", linestyle="--", alpha=0.5)
 
    plt.tight_layout()
    nom_fichier = "graphiques_ventes.png"
    plt.savefig(nom_fichier, dpi=150, bbox_inches="tight")
    print(f"✅ Graphiques sauvegardés dans '{nom_fichier}'.\n")
    plt.show()
 
 
# ══════════════════════════════════════════════
#  🚀  PROGRAMME PRINCIPAL
# ══════════════════════════════════════════════
def main():
    """
    Point d'entrée du script.
    Exécute toutes les étapes dans l'ordre logique.
    """
    print("\n" + "🛒 " * 20)
    print("   DÉMARRAGE — Analyse automatique des ventes")
    print("🛒 " * 20 + "\n")
 
    # ── Étape 1 : Générer les données ───────────────────────
    generer_ventes_csv()
 
    # ── Étapes 2-4 : Lire et calculer ──────────────────────
    resultats = calculer_resultats()
 
    # ── Étape 5 : Afficher le rapport ──────────────────────
    afficher_rapport(resultats)
 
    # ── Étape 6 : Meilleur produit ──────────────────────────
    meilleur_produit(resultats)
 
    # ── Étape 7 : Exporter le CSV final ────────────────────
    exporter_resultats(resultats)
 
    # ── Bonus : Graphiques ──────────────────────────────────
    afficher_graphiques(resultats)
 
    print("✨ Analyse terminée avec succès !\n")
 
 
# Ce bloc s'assure que main() ne s'exécute que si on lance
# ce fichier directement (pas si on l'importe dans un autre script)
if __name__ == "__main__":
    main()
 