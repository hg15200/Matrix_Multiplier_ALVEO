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
#in1 = 10
#in2 = 200
#in1_sw = np.full((size,size),10)
#in2_sw = np.full((size,size),200)
#out_sw = np.zeros((size, size), dtype='u4')
#overlay_path = '/home/hector/IFIC_ALVEO/MatMul_py/Mat_HLS_2B/Mat_HLS_2B/overlays/Mat_HLS_2B.xclbin'
overlay_path = '../bin_HLS/Mat_HLS_2B.xclbin'

matrix_multiplier = MatrixMultiplier(overlay_path, size, in1, in2)

# Software Version
# Measure execution time for software
#start_time_sw = time.time()
#out_sw = np.dot(in1_sw, in2_sw)
#end_time_sw = time.time()
#execution_time_sw = end_time_sw - start_time_sw


# Run hardware version
result_hw, exec_time_hw = matrix_multiplier.run_hw()
print(f"In1: {in1}")
print(f"In2: {in2}")
#print(f"Resultado SW: {out_sw}")
print(f"Resultado HW: {result_hw}")
print(f"Tiempo de ejecución HW: {exec_time_hw} segundos")
#print(f"Tiempo de ejecución SW: {execution_time_sw} segundos")

# Obtener estadísticas de memoria
mem_info = psutil.virtual_memory()
# Imprimir memoria libre
print(f"Memoria libre: {mem_info.available} bytes")


