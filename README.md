# map-bot

Projet de bac 2021-2022, Alain THIRION

Division en strates : 

0. robot physique (Meccano, ...) déplaçable dans l'espace par télécommande bluetooth (BlueDot + gpiozero) +++++ modulable !!!

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


  ----- MATERIEL --------
rotary encoder
balises radios
servos (bien choisir !!!!!) + dénombrer

  
  
