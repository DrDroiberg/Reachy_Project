#commenter
#mes from a moi car pyzo fait chier
from os import path
import sys
sys.path.append(path.abspath('C:/Users/maxbu/Desktop/Projet_2A/progMax_4')) #changer le path
#----------

import time
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
from Prog_cinematic_movement_max4 import Full_matrice_Rota
from conversion_px_cm_max4 import coeff_px_to_cm
from z_coordinate_max4 import get_depth_l
from z_coordinate_max4 import get_depth_r
import numpy as np
from posi_elbow_max4 import posi_elbow_r, posi_elbow_l
import random


path = 'C:/Users/maxbu/dossPython/liste_Reachy/recognised_images' #changer la path
coeff = coeff_px_to_cm()

reachy = ReachySDK(host='localhost')
#reachy = ReachySDK(host='10.117.68.17')

#permet de creer les fichiers
final_position_r_data = []
final_position_l_data = []

#cette fonction détermine tout les angle moteurs et les met dans un fichier pour qu'ensuite le robot bouge. Cette fonction de fait pas bouger le robot
#gama, beta, alpha sont les rotation de la main pour "Full_matrice_Rota"
def inverse_kinematic(gamma, beta, alpha, right_wrist_coords,left_wrist_coords,compteur_image):

    ancient_mouvement_r = [0,0,0,0,0,0,0]   #arbitraire mais correspondrait a la position  des bras
    ancient_mouvement_l = [0,0,0,0,0,0,0]
    compteur = 0
    compteur2 = 0

    #permet d'instancier mouvement2 qui correspond a l'ancien mouvement
    mouvement2_r = Full_matrice_Rota(gamma, beta, alpha, 0.2, -0.3, -0.3)
    mouvement2_l = Full_matrice_Rota(gamma, beta, alpha, 0.2, 0.3, -0.3)

    #boucle qui détermine la cinematique inverse pour chaque position filmee
    for i in range(0, compteur_image):
        wrist_r_z = get_depth_r(i)
        wrist_r_x = right_wrist_coords[i][0] * coeff
        wrist_r_y = right_wrist_coords[i][1] * coeff

        #limite de securitees
        if wrist_r_z < 0:   #profondeur
            wrist_r_z = 0

        if wrist_r_x > -0.08:   #corps du robot
            wrist_r_x = -0.08

        if wrist_r_y < -0.3:    #table
            wrist_r_y = -0.3


        mouvement = Full_matrice_Rota(gamma, beta, alpha, wrist_r_z, wrist_r_x, wrist_r_y)
        final_position = reachy.r_arm.inverse_kinematics(mouvement,q0 = ancient_mouvement_r)
        shoulder_pitch_à_verifier = posi_elbow_r(i)

        #on met la priorite sur la position de la main et non la position du coude si la main est tendu vers l'avant
        if wrist_r_z < 0.35:
            #boucle qui met des valleurs aleatoire afin d'obtenir un calcul de cinematique inverse où le coude correspond a plus ou moins 10 degree a ce qui est mesurer sur l'image
             while ((shoulder_pitch_à_verifier+10  < final_position [1]) or (final_position [1] < shoulder_pitch_à_verifier-10)) and (compteur < 200):
                r1 = random.random()
                r2 = random.random()
                r3 = random.random()
                r4 = random.random()
                r5 = random.random()
                r6 = random.random()
                r7 = random.random()
                gammmmma = random.randrange(-180, 180, 1)
                beeeeeeta = random.randrange(-180, 180, 1)
                aaaaaalpha = random.randrange(-180, 180, 1)
                if compteur < 130:
                    mouvement = Full_matrice_Rota(gammmmma, beeeeeeta, aaaaaalpha, wrist_r_z, wrist_r_x, wrist_r_y)
                else:   #au bout de 130 iterations, on fixe la profondeur
                    mouvement = Full_matrice_Rota(gammmmma, beeeeeeta, aaaaaalpha, 0.15, wrist_r_x, wrist_r_y)
                final_position_test = reachy.r_arm.inverse_kinematics(mouvement,q0 = [r1*100, r2*100, r3*100, r4*100, r5*100, r6*100, r7*100])

                compteur += 1

        #fin boucle while et if





        #pour le secu en cinematique forward
        pos_a_securite = reachy.r_arm.forward_kinematics(joints_position = [final_position[0], final_position[1], final_position[2], final_position[3],0,0,0])
        if pos_a_securite[2][3] < -0.3:
            print("ooooo nON")
            final_position[3] = -110 #on reduit l'angle en degree de 20 degree





        compteur = 0
        mouvement2_r = mouvement
        print("picture ",i," right is done")
        ancient_mouvement_r = final_position

        #ici, on met les valleurs des angle dans un fichier pour le mouvement plus tard
        final_position_r_data.append(final_position)
        np.savetxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/final_position_r_data.txt',            final_position_r_data,delimiter=", ", fmt='%s')


############################

#meme programme mais pour le bras gauche
        wrist_l_z = get_depth_l(i)
        wrist_l_x = left_wrist_coords[i][0] * coeff
        wrist_l_y = left_wrist_coords[i][1] * coeff

        if wrist_l_z < 0:
            wrist_l_z = 0

        if wrist_l_x < 0.08:
            wrist_l_x = 0.08

        if wrist_l_y < -0.3:
            wrist_l_y = -0.3

        mouvement = Full_matrice_Rota(gamma, beta, alpha, wrist_l_z, wrist_l_x, wrist_l_y)
        final_position = reachy.l_arm.inverse_kinematics(mouvement,q0 = ancient_mouvement_l)
        shoulder_pitch_à_verifier = posi_elbow_l(i)


        if wrist_l_z < 0.35:
            #boucle qui met des valleurs aleatoire afin d'obtenir un calcul de cinematique inverse où le coude correspond a plus ou moins 10 degree a ce qui est mesurer sur l'image
            while ((shoulder_pitch_à_verifier+10  < final_position [1]) or (final_position [1] < shoulder_pitch_à_verifier-10)) and (compteur2 < 200):
                r1 = random.random()
                r2 = random.random()
                r3 = random.random()
                r4 = random.random()
                r5 = random.random()
                r6 = random.random()
                r7 = random.random()
                gammmmma = random.randrange(-180, 180, 1)
                beeeeeeta = random.randrange(-180, 180, 1)
                aaaaaalpha = random.randrange(-180, 180, 1)
                if compteur2 < 130:
                    mouvement = Full_matrice_Rota(gammmmma, beeeeeeta, aaaaaalpha, wrist_l_z, wrist_l_x, wrist_l_y)
                else:   #au bout de 130 iterations, on fixe la profondeur
                    mouvement = Full_matrice_Rota(gammmmma, beeeeeeta, aaaaaalpha, 0.15, wrist_l_x, wrist_l_y)
                final_position = reachy.l_arm.inverse_kinematics(mouvement,q0 = [r1*100, r2*100, r3*100, r4*100, r5*100, r6*100, r7*100])

                compteur2 += 1

        #fin boucle while et if
        if 199 > compteur2 > 129:
            print("small bad picture left")
        if compteur2 > 199:  # si on trouve pas, on prend la position precedente
            print("\nbad picture left\n")
            final_position = reachy.l_arm.inverse_kinematics(mouvement2_l,q0 = ancient_mouvement_l)

        #pour le secu en cinematique forward
        pos_a_securite = reachy.l_arm.forward_kinematics(joints_position = [final_position[0], final_position[1], final_position[2], final_position[3],0,0,0])
        if pos_a_securite[2][3] < -0.3:
            print("ooooo nON")
            final_position[3] = -110 #on reduit l'angle en degree de 20 degree



        compteur2 = 0
        mouvement2_l = mouvement
        print("picture ",i," left is done")

        ancient_mouvement_l = final_position

        final_position_l_data.append(final_position)
        np.savetxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/final_position_l_data.txt', final_position_l_data,delimiter=", ", fmt='%s')


#Fin






#ce programme fait bouger le robot avec les angle définit precedement
def mouvement_reachy (compteur_image):
    final_position_r = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/final_position_r_data.txt',
                    delimiter=',')

    final_position_l = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/final_position_l_data.txt',
                    delimiter=',')


    for i in range (0,compteur_image):
        left_arm_final_position = {
            reachy.l_arm.l_shoulder_pitch: final_position_l[i][0],
            reachy.l_arm.l_shoulder_roll: final_position_l[i][1],
            reachy.l_arm.l_arm_yaw: final_position_l[i][2],
            reachy.l_arm.l_elbow_pitch: final_position_l[i][3],
            reachy.l_arm.l_forearm_yaw: 0,#final_position_l[i][4],  #on fixe ces positions car peut utile
            reachy.l_arm.l_wrist_pitch: 0,#final_position_l[i][5],
            reachy.l_arm.l_wrist_roll: 0,#final_position_l[i][6],
        }

        right_arm_final_position = {

            reachy.r_arm.r_shoulder_pitch: final_position_r[i][0],
            reachy.r_arm.r_shoulder_roll: final_position_r[i][1],
            reachy.r_arm.r_arm_yaw: final_position_r[i][2],
            reachy.r_arm.r_elbow_pitch: final_position_r[i][3],
            reachy.r_arm.r_forearm_yaw:0,#final_position_r[i][4],   #on fixe ces positions car peut utile
            reachy.r_arm.r_wrist_pitch: 0, #final_position_r[i][5],
            reachy.r_arm.r_wrist_roll: 0, #final_position_r[i][6],
        }

      #en gros, notre final position est la liste des moteurs et leurs valleurs.
      #Il faut prendre le goto qui utilise la liste des moteurs et bien les appeler

        #goto({joint: pos for joint, pos in zip(reachy.r_arm.joints.values(), final_position)}, duration=1.0)

        goto(
            goal_positions=right_arm_final_position,
            duration=0.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
        time.sleep(0.2)
        goto(
            goal_positions=left_arm_final_position,
            duration=0.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
