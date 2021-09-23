# map-bot

CECI N'EST PAS UN README.

Projet de bac 2021-2022, Alain THIRION

Code à diviser en plusieurs modules : docs user, python basic (API), puis code secondaire

Division en strates : 

0. robot physique (Meccano, ...) déplaçable dans l'espace par télécommande bluetooth (BlueDot + gpiozero) +++++ modulable !!!
  - choix de l'interface : carte I2C, channel PWM avec 16 servos
  --> https://www.kubii.fr/cartes-extension-cameras-raspberry-pi/2750-servo-driver-hat-kubii-614961955844.html?search_query=16+channel+PWM+servo+driver&results=124
 - liste des composants nécessaires : 
    - servo stepper (ou précis) pour rotation capteur HC-SR04 ########
    - deux continuous servos pour mouvement général ; + puissant ou pas ? ----> https://www.gotronic.fr/art-servomoteur-fs5103r-25839.htm (torque 3.0 kg.cm-1)
    - bras 1 (recharge / mouvement possible) : 2 servo à rotation, puissance 
    - 
    - rotating servo puissant : TowerPro SG-5010 - 5010 (torque 5.5)


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
  (bras articulé pour reproduire les mouvements : Rotary Encoder... compliqué en 3D, autre mvt + simple ?)
  - ajout d'un bras / stockage protégé du cable de chargement sur secteur 
  - automatisation des tâches de réglage système (en headless)
  - ajout d'une caméra + centre secondaire de traitement si nécessaire...
  A. Phase IA
    - reconnaissance d'images, utilisation de la caméra
    - reconnaissance de prises secteur, entraînement de l'image
    - utilisation complémentaire du capteur de distance pour repérer la prise dans l'espace 
  
III. Phase domotique (optionnel +++)
  - interaction avec l'environnement... + ?
  
  
  
  ----- DOCS NEEDED ------
Réception des ondes radios --> enveloppe hilbert scipy, matériel... + Fourier
Bibliothèques python nécessaires : images vectorielles, tkinter (micro logiciel), IA

Modélisaition 3D : freeCAD, LeoCAD, Blender 

  ----- MATERIEL --------
chercher codes promos Kubii +  articles le +  sur kubii

rotary encoder
balises radios
servos (bien choisir !!!!!) + dénombrer
chenilles     
interface SPI pour PWM ?      OK


chenilles : 
https://fr.banggood.com/Small-Hammer-Plastic-Tracks-Crawler-Belt-Kit-For-DIY-RC-Robot-Car-Tank-p-1574899.html?rmmds=detail-topright-recommendation&cur_warehouse=CN

------- AGENDA ACTUEL -------

achat des composants principaux (+ tests perf) : avant vacances de la Toussaint, + coder premiers morceaux nécessaires (mouvement esclave notamment)
vacances Toussaint : construction, repérer pièces manquantes, liste
après Toussaint : tests de fonctionnement de base, continuer le code, choisir les algos secondaires et les commencer, fabrication 3D des pièces
vacances de Noël : fabrication matérielle des pièces nécessaires, finir le robot physique
après vacances de Noël : finir de coder les modules secondaires, tests finaux
vacances février : phase domotique optionelle

------ VARIANTES ---------
créer un hexapode pour mieux s'adapter aux terrains accidentés ?



  
