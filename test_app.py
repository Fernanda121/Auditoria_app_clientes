import pytest
import builtins
from unittest.mock import patch
from problema_cliente import ingresardatos


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
