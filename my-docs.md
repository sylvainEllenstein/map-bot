Docs pour l'aglo principal de localisation et mapping : 
algo coreSlam : https://www.instituts-carnot.eu/fr/coreslam-localisation-et-cartographie-simultan%C3%A9es-pour-robot-autonome (inutile maintenant)

---> chercher "algo de SLAM", filtre de kalman...
https://tel.archives-ouvertes.fr/tel-01781871
https://fr.wikipedia.org/wiki/Cartographie_et_localisation_simultan%C3%A9es
https://www.cs.cmu.edu/~motionplanning/lecture/Chap8-Kalman-Mapping_howie.pdf
idées https://www.innowtech.com/2019/05/16/les-algorithmes-slam/

essayer (kalman filter) : https://oatao.univ-toulouse.fr/2248/1/Alazard_2248.pdf

M.Garay : https://arxiv.org/pdf/1910.03558.pdf
![image](https://user-images.githubusercontent.com/76899255/135299148-925629dd-1f19-41b7-89cc-aaf6eda5a802.png)


For motor driver hat : 
https://www.youtube.com/watch?v=Omm6_QxtJ04
--> SSH connection + sudo pip3 install adafruit-circuitpython-motorkit
corriger les patchs dans la lib adafruit (voir vidéo)
pour voir exemples de fonctionnement : https://github.com/gallaugher/PiBot/blob/master/pibottest.py


NB : ne pas créer de classes supplémentaires, surchargerait trop la mem

Pour le mouvement dans l'espace, regarder : http://eavr.u-strasbg.fr/~bernard/education/3a_robmob/3a_robmob_slides.pdf

![image](https://user-images.githubusercontent.com/76899255/141144304-bc6e6c5c-03a3-40a1-a6f0-34f18095d7b2.png)

Pour robot mobile unicycle :
![image](https://user-images.githubusercontent.com/76899255/141146472-c975ab27-3e13-43b6-8705-c826ef2c023e.png)

Pour robot unicycle avec roue de commande d'orientation : 
![image](https://user-images.githubusercontent.com/76899255/141147202-309f3fbb-25e0-45a4-bc21-e9c2dd160533.png)
