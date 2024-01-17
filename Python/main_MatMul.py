from Matrix_Multiplier_FPGA import MatrixMultiplier
import glob
import numpy as np
import time
import pynq
import psutil

import os

# Obtener la ruta del directorio actual del script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Unirlo con el nombre del archivo Mat_HLS_2B.xclbin
overlay_path = os.path.join(script_directory, 'Mat_HLS_2B.xclbin')

print("Ruta completa al archivo Mat_HLS_2B.xclbin:", overlay_path)

platform = glob.glob("/opt/xilinx/platforms/*/*.xpfm")[0]

size = 8
# Datos de entrada
in1 = np.random.randint(low=0, high=100, size=(size, size), dtype='u4')
in2 = np.random.randint(low=0, high=100, size=(size, size), dtype='u4')
overlay_path = '../bin_HLS/Mat_HLS_2B.xclbin'

matrix_multiplier = MatrixMultiplier(overlay_path, size, in1, in2)

# Run hardware version
result_hw, exec_time_hw = matrix_multiplier.run_hw()
print(f"In1: {in1}")
print(f"In2: {in2}")
print(f"Resultado HW: {result_hw}")
print(f"Tiempo de ejecución HW: {exec_time_hw} segundos")

