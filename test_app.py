import pytest
import builtins
from unittest.mock import patch
from problema_cliente import ingresardatos, modificardatos

#Testeo a la funcion ingresar datos#

@patch('builtins.input', side_effect=[
    "12345678-9",     # RUN
    "Juan",           # NOMBRE
    "Perez",          # APELLIDO
    "DIRECCIÓN 123",  # DIRECCIÓN
    "987654321",      # TELÉFONO
    "juan@gmail.com",  # CORREO
    "101",            # CÓDIGO DEL TIPO DE CLIENTE
    "100000"          # MONTO CRÉDITO
])
def test_ingresardatos(mock_input):
    result = ingresardatos()
    assert result is None 

#Testeo a la funcion modificar datos#


@patch('builtins.input', side_effect=[
    "1",  # RUN del cliente a modificar
    "NuevoNombre",  # nuevo nombre
    "NuevoApellido",  # nuevo apellido
    "Nueva Dirección",  # nueva dirección
    "987654321",  # nuevo teléfono
    "nuevo@email.com",  # nuevo correo
    "102",  # nuevo tipo de cliente
    "200000",  # nuevo monto
    "SI", #Respuesta a si se desea modificar
    "999"  # este es un tipo de cliente que NO existe (lo usamos para ver si el programa detecta errores)
    
])
def test_modificardatos(mock_input):
    result = modificardatos()
    assert result == "Modificacion exitosa"
