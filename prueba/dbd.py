import mysql.connector
from Clases import *
from typing import List

class DAO:

    def __init__(self) -> None:
        self.cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='Evaluacion_N3')
        


    def AddCars(self,vehiculo:vehiculo) -> None:
        cursor = self.cnx.cursor()
        query = ("INSERT INTO tblvehiculos (Patente,Marca,Modelo,Color,NumeroMotor) VALUES (%s,%s,%s,%s,%s)")
        data = (vehiculo.getPatente(),vehiculo.getMarca(),vehiculo.getModelo(),vehiculo.getColor(),vehiculo.getNumeroMotor())
        cursor.execute(query, data)
        self.cnx.commit()
        
    def DeleteCars(self,patente) -> None:
        cursor = self.cnx.cursor()
        query = ("DELETE INTO tblvehiculos (Patente,Marca,Modelo,Color,NumeroMotor) VALUES (%s,%s,%s,%s,%s)")
        data = (patente,)
        cursor.execute(query, data)
        self.cnx.commit()