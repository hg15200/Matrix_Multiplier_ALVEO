from setuptools import setup, find_packages

setup(
    name='Matrix_Multiplier_FPGA',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'pynq',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'Matrix_Multiplier_FPGA_script = Matrix_Multiplier_FPGA.Matrix_Multiplier_FPGA:main',
        ],
    },
)

