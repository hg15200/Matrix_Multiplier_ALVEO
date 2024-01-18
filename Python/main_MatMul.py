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

size = 4
# Datos de entrada
in1 = np.random.randint(low=0, high=100, size=(size, size), dtype='u4')
in2 = np.random.randint(low=0, high=100, size=(size, size), dtype='u4')

in3 = 10
in4 =200

overlay_path = MatrixMultiplier.set_overlay_path('../bin_HLS/Mat_HLS_2B.xclbin') 

matrix_multiplier = MatrixMultiplier(size, in1, in2)

# Run hardware version
result_hw, exec_time_hw = matrix_multiplier.run_hw()
print(f"In1: {in1}")
print(f"In2: {in2}")
print(f"Resultado HW: {result_hw}")
print(f"Tiempo de ejecución HW: {exec_time_hw} segundos")

matrix_multiplier_B = MatrixMultiplier(size, in3, in4)
result_hw_B, exec_time_hw_B = matrix_multiplier_B.run_hw()

print(f"In1: {in3}")
print(f"In2: {in4}")
print(f"Resultado HW: {result_hw_B}")
print(f"Tiempo de ejecución HW: {exec_time_hw_B} segundos")

