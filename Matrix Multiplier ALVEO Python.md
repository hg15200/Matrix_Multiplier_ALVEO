# Matrix Multiplier ALVEO Python

## Introduction
This is a tutorial to show you how to use a matrix multiplier python function on ***ALVEO accelerator cards***.

### ALVEO U250
The [**AMD ALVEO U250**](https://www.xilinx.com/products/boards-and-kits/alveo/u250.html) Data Center accelerator card is PCIe Gen3x16 compliant featuring Xilinx Virtex UltraScale+ technology. These cards accelerate compute-intensive applications such as machine learning, data analytics and more applications.

Firstly, if you aren't configure the ALVEO yet, you must to following the next steps.
- [Installing the Deployment Software](https://docs.xilinx.com/r/en-US/ug1301-getting-started-guide-alveo-accelerator-cards/Installing-the-Deployment-Software). You install the Xilinx Runtime [(XRT)](https://www.xilinx.com/products/design-tools/vitis/xrt.html) to facilitate communication between the application code and the accelerated application (kernel) deployed on the reconfigurable portion of PCIe based on ALVEO accelerator cards, Zynq 7000, Zynq Ultrascale+ MPSoC or Versal ACAPs.
- [Card Installation Procedures](https://docs.xilinx.com/r/en-US/ug1301-getting-started-guide-alveo-accelerator-cards/Card-Installation-Procedures). When you install the XRT, the next step is installing the card following the steps in the above link.

### Local Computer
To use your own computer, install and setup Vitis and install the ALVEO card packages, in this case the ALVEO U250 packages.
#### Setup Vitis on your own computer 
To run or build this lab on your own computer, you have to install Vitis (these licenses are free). 
Download [Vitis 2022.2](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis/2022-2.html) and install the tools. This link contains the Vitis IDE and the Vitis HLS, make sure you install the 2022.2 version.
#### Setup the tools 
Add the following lines to your enviroment setup:
```tcl=
source /opt/xilinx/xrt/setup.sh
source /$XILLINX_VITIS_INSTALL_PATH/settings64.sh
```

### Code
This line use the library *glob* to search for files with the extension .xpfm in the path /opt/xilinx/platforms/*/*.xpfm". In this case, you will obtain the ALVEO platform.

```tcl=
platform = glob.glob("/opt/xilinx/platforms/*/*.xpfm")[0]
```

This line of code is used to define the path to the bitstream .xclbin binary file containing the hardware implementation of the HLS (High-Level Synthesis) design you are using in your project.
```tcl=
overlay_path = '../bin_HLS/Mat_HLS_2B.xclbin'
```
1. **'../bin_HLS/'** , This refers to the bin_HLS directory that is located in the parent directory of the current directory. Using .. means that you go up one level in the directory hierarchy from the current location.

2. **Mat_HLS_2B.xclbin** , This is the name of the bitstream .xclbin binary file containing the hardware logic generated from your HLS design.

This line of code creates an instance of the MatrixMultiplier class, which belongs to the implementation itself in the Python code.
```tcl=
matrix_multiplier = MatrixMultiplier(overlay_path, size, in1, in2)
```

- **'MatrixMultiplier'** : This is the name of the class you are instantiating.
- **'overlay_path'** :  This is the path to the binary bitstream file (.xclbin) containing the hardware implementation for matrix multiplication. This path is used to load the PYNQ overlay.
- **'size'** : This is the size of the matrices to be multiplied.
- **'in1 & in1'** : Input data for matrix multiplication. This data is stored in arrays and used as input to the hardware.

This line of code invokes the run_hw() method on the instance of the matrix_multiplier object.
```tcl=
result_hw, exec_time_hw = matrix_multiplier.run_hw()
```

- **'matrix_multiplier'** : This is the object containing the implementation of matrix multiplication and has been created from the MatrixMultiplier class.
- **'run_hw()'** : A method of the MatrixMultiplier class that performs matrix multiplication in hardware. This method performs data transfer to and from hardware, initiates the matrix multiplication operation and measures the execution time.
- **'result_hw'** : It is the result of matrix multiplication obtained from the hardware.
- **'exec_time_hw'** : The execution time of matrix multiplication in hardware.