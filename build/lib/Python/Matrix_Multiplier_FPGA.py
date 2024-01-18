import pynq
import numpy as np
import time

class MatrixMultiplier:
    overlay_path = None  # Variable de clase para almacenar overlay_path

    @classmethod
    def set_overlay_path(cls, path):
        cls.overlay_path = path

    def __init__(self, size, in1_data, in2_data):
        if not MatrixMultiplier.overlay_path:
            raise ValueError("overlay_path no ha sido configurado. Use set_overlay_path antes de crear una instancia de MatrixMultiplier.")
        
        self.overlay = pynq.Overlay(MatrixMultiplier.overlay_path)
        self.mmult = self.overlay.mmult_1
        self.size = size

        self.in1 = pynq.allocate((size, size), 'u4', target=self.overlay.bank0)
        self.in2 = pynq.allocate((size, size), 'u4', target=self.overlay.bank1)
        self.out_hw = pynq.allocate((size, size), 'u4', target=self.overlay.bank2)

        # Copia los datos de entrada a los buffers asignados
        self.in1[:] = in1_data
        self.in2[:] = in2_data

    def run_hw(self):
        self.in1.sync_to_device()
        self.in2.sync_to_device()

        start_time = time.time()
        self.mmult.call(self.in1, self.in2, self.out_hw, self.size)
        end_time = time.time()

        self.out_hw.sync_from_device()

        execution_time = end_time - start_time
        return self.out_hw, execution_time

    
