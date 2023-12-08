from dbd import DAO
from Clases import *
import os
dao = DAO()

input("Agregar Nuevo Vehiculo")
newpatente = input("Ingresa La Patente del Vehiculo: ")
newmarca = input("Ingresa la Marca del vehiculo: ")
newmodelo = input ("Ingresa el Modelo del vehiculo: ")
newcolor = input("Ingresa el Color del vehiculo: ")
newnmotor = input("Ingresa el Numero de Motor del vehiculo: ")
newcar = vehiculo(newpatente,newmarca,newmodelo,newcolor,newnmotor)
dao.AddCars(newcar)
input("Nuevo Vehiculo Agregado! ")