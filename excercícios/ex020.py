"""
6 - Faça um programa que abra e reproduza um áudio de um arquivo MP3.
"""

import pygame #Bibliteca muito usada na criação de games e muito usada para músicas
pygame.init()

pygame.mixer.music.load("OceanAlok.mp3")
pygame.mixer.music.play()
input("Música tocando... Aperte Enter para encerrar")