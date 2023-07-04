from setuptools import setup

setup(name='dyalog-jupyter-kernel',
      version='0.1.0',
      description='A Dyalog APL kernel for Jupyter',
      license='MIT',
      url="https://github.com/TomaSajt/dyalog-jupyter-kernel",
      install_requires=['notebook >= 4.0'],
      packages=['dyalog_kernel'],
)
