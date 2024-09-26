1. 创建环境
conda create -n quantum python=3.11
1. 激活环境
conda activate D:\CS\python-studying\Qiskit\.conda
2. 退出环境
conda deactivate
3. 删除环境
conda env remove -n quantum



之后我们可以在terminal中通过输入如下的代码跳转到Jupyter Notebook的页面，Jupyter Notebook可能是结合编程、文本和图像的最佳方式：

jupyter notebook
在Jupyter Notebook创建一个新文件之后输入如下的代码我们便可以检验是否下载好并且是否下载了最新的版本：

import qiskit
qiskit.__qiskit_version__

在虚拟环境中
{'qiskit': '0.45.1', 'qiskit-aer': None, 'qiskit-ignis': None, 'qiskit-ibmq-provider': None, 'qiskit-nature': None, 'qiskit-finance': None, 'qiskit-optimization': None, 'qiskit-machine-learning': None}