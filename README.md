# map-bot

CECI N'EST PAS UN README.

Projet de bac 2021-2022, Alain THIRION

Code à diviser en plusieurs modules : docs user, python basic (API), puis code secondaire

Division en strates : 

0. robot physique (Meccano, ...) déplaçable dans l'espace par télécommande bluetooth (BlueDot + gpiozero) +++++ modulable !!!
  - choix de l'interface : carte I2C, channel PWM avec 16 servo OKOKOK
 - liste des composants nécessaires : 
    - servo stepper (ou précis) pour rotation capteur HC-SR04 ########
    - deux continuous servos pour mouvement général ; + puissant ou pas ? ----> https://www.gotronic.fr/art-servomoteur-fs5103r-25839.htm (torque 3.0 kg.cm-1)
    - bras 1 (recharge / mouvement possible) : 2 servo à rotation, puissance 
    - 
    - rotating servo puissant : TowerPro SG-5010 - 5010 (torque 5.5)

capteur plus précis ? (LIDAR, tester précision du HC SR04)
utilisation de la centrale inertielle ? (intégrer le mouvement)


I. déplacement dans l'espace, utilisant un capteur de distance
  - repérage dans l'espace grâce à un système de balises radios
  --> reconnaissance d'un signal, fréquence
  - deplacement anarchique sans collision
  - cartographie de l'espace avec capteur
  - exportation des cartes dans des fichiers / images vectorielles ( + conversion matricielle pour garantir la portabilité ?)
  - cartes annotables
  - rapidité / efficacité / portabilité du transfert de cartes sur un autre support
  - micro-logiciel de visualisation des cartes
  - aller d'un point A à un point B en utilisant la carte + Dijkstra
  
II. Amélioration des fonctions du robot
  - interface de visualisation des calculs pendant le fonctionnement (matrice LEDs, écran)

  
  
  
  ----- DOCS NEEDED ------
Bibliothèques python nécessaires : images vectorielles, tkinter (micro logiciel local pour la réception (SSH ?)), IA

Modélisation 3D : freeCAD, LeoCAD, Blender 
Localisation / mapping :
https://www.cs.cmu.edu/~motionplanning/lecture/Chap8-Kalman-Mapping_howie.pdf

---->> chercher en français ??? .. 

  ----- MATERIEL --------

rotary encoder
chenilles toujours d'actu pour faciliter le travail  

------- AGENDA ACTUEL -------

achat des composants principaux (+ tests perf) : avant vacances de la Toussaint, + coder premiers morceaux nécessaires (mouvement esclave notamment)
vacances Toussaint : construction, repérer pièces manquantes, liste
après Toussaint : tests de fonctionnement de base, continuer le code, choisir les algos secondaires et les commencer, fabrication 3D des pièces
vacances de Noël : fabrication matérielle des pièces nécessaires, finir le robot physique
après vacances de Noël : finir de coder les modules secondaires, tests finaux
vacances février : phase domotique optionelle

------ VARIANTES ---------
créer un hexapode pour mieux s'adapter aux terrains accidentés ?



  
