#commenter
#mes from a moi car pyzo fait chier
from os import path
import sys
sys.path.append(path.abspath('C:/Users/maxbu/Desktop/Projet_2A/progMax_3'))
#----------



import numpy as np
from reachy_sdk.trajectory import InterpolationMode
from math import acos , pi
from picture_calculation_max4 import offset_distance





def posi_elbow_r(u):
    #Ici, on importe les membre nécéssaire
    #right :
    right_wrist = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_wrist_coords.txt', delimiter=',')

    right_elbow = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_elbow_coords.txt', delimiter=',')

    right_shoulder = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_shoulder_coords.txt', delimiter=',')

#left :
    left_shoulder = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_shoulder_coords.txt', delimiter=',')


#calcule le point central repere du reachy

    centre_x = left_shoulder[u][0] + (right_shoulder[u][0] - left_shoulder[u][0]) / 2

    centre_y = min(right_shoulder[u][1], left_shoulder[u][1]) + (abs(right_shoulder[u][1] - left_shoulder[u][1]) / 2)

#Ici, calcule des distance
    should_elbow= offset_distance(right_elbow[u][0], right_elbow[u][1], right_shoulder[u][0],             right_shoulder[u][1])

    elbow_centre= offset_distance(right_elbow[u][0], right_elbow[u][1], centre_x, centre_y)

    centre_should= offset_distance(centre_x, centre_y, right_shoulder[u][0],right_shoulder[u][1])


#Calcule de l'angle shoulder roll
    shoulder_roll = acos((should_elbow**2 +centre_should**2 - elbow_centre**2) / (2 * should_elbow * centre_should)) # c'est juste l'angle c en rad

    shoulder_roll = shoulder_roll * (180/pi) #I c'est juste l'angle c an degree

    limite = centre_y - right_elbow[u][1]
    if limite < 0:
        shoulder_roll = shoulder_roll - 270
    else :
        shoulder_roll = 90 - shoulder_roll # c'est bien le shiulder roll


    return shoulder_roll



def posi_elbow_l(u):
    #Ici, on importe les membre nécéssaire
    #right :
    right_wrist = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_wrist_coords.txt', delimiter=',')

    right_elbow = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_elbow_coords.txt', delimiter=',')

    right_shoulder = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_shoulder_coords.txt', delimiter=',')

#left :
    left_wrist = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_wrist_coords.txt', delimiter=',')

    left_elbow = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_elbow_coords.txt', delimiter=',')

    left_shoulder = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_shoulder_coords.txt', delimiter=',')


#calcule le point central repere du reachy

    centre_x = left_shoulder[u][0] + (right_shoulder[u][0] - left_shoulder[u][0]) / 2

    centre_y = min(right_shoulder[u][1], left_shoulder[u][1]) + (abs(right_shoulder[u][1] - left_shoulder[u][1]) / 2)

#Ici, calcule des distance
    should_elbow= offset_distance(left_elbow[u][0], left_elbow[u][1], left_shoulder[u][0],             left_shoulder[u][1])

    elbow_centre= offset_distance(left_elbow[u][0], left_elbow[u][1], centre_x, centre_y)

    centre_should= offset_distance(centre_x, centre_y, left_shoulder[u][0],left_shoulder[u][1])


#Calcule de l'angle shoulder roll
    shoulder_roll = acos((should_elbow**2 +centre_should**2 - elbow_centre**2) / (2 * should_elbow * centre_should)) # c'est juste l'angle c en rad

    shoulder_roll = shoulder_roll * (180/pi) #I c'est juste l'angle c an degree

    limite = centre_y - left_elbow[u][1]
    if limite < 0:
        shoulder_roll = 270 - shoulder_roll
    else :
        shoulder_roll =  shoulder_roll -90  # c'est bien le shiulder roll

    return shoulder_roll


posi_elbow_r(0)









