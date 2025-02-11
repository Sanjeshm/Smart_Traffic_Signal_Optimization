from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy
import os
import importlib.util

# Load version.py dynamically
spec = importlib.util.spec_from_file_location('version', os.path.join('.', 'darkflow', 'version.py'))
version_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version_module)
VERSION = version_module.__version__

if os.name == 'nt':
    ext_modules = [
        Extension("darkflow.cython_utils.nms",
                  sources=["darkflow/cython_utils/nms.pyx"],
                  include_dirs=[numpy.get_include(),"darkflow/cython_utils"]
                  ),
        Extension("darkflow.cython_utils.cy_yolo2_findboxes",
                  sources=["darkflow/cython_utils/cy_yolo2_findboxes.pyx"],
                  include_dirs=[numpy.get_include(),"darkflow/cython_utils"]
                  ),
        Extension("darkflow.cython_utils.cy_yolo_findboxes",
                  sources=["darkflow/cython_utils/cy_yolo_findboxes.pyx"],
                  include_dirs=[numpy.get_include(),"darkflow/cython_utils"]
                  )
    ]

elif os.name == 'posix':
    ext_modules = [
        Extension("darkflow.cython_utils.nms",
                  sources=["darkflow/cython_utils/nms.pyx"],
                  libraries=["m"],
                  include_dirs=[numpy.get_include(),"darkflow/cython_utils"]
                  ),
        Extension("darkflow.cython_utils.cy_yolo2_findboxes",
                  sources=["darkflow/cython_utils/cy_yolo2_findboxes.pyx"],
                  libraries=["m"],
                  include_dirs=[numpy.get_include(),"darkflow/cython_utils"]
                  ),
        Extension("darkflow.cython_utils.cy_yolo_findboxes",
                  sources=["darkflow/cython_utils/cy_yolo_findboxes.pyx"],
                  libraries=["m"],
                  include_dirs=[numpy.get_include(),"darkflow/cython_utils"]
                  )
    ]

else:
    ext_modules = [
        Extension("darkflow.cython_utils.nms",
                  sources=["darkflow/cython_utils/nms.pyx"],
                  libraries=["m"],
                  include_dirs=[numpy.get_include(),"darkflow/cython_utils"]
                  ),
        Extension("darkflow.cython_utils.cy_yolo2_findboxes",
                  sources=["darkflow/cython_utils/cy_yolo2_findboxes.pyx"],
                  libraries=["m"],
                  include_dirs=[numpy.get_include(),"darkflow/cython_utils"]
                  ),
        Extension("darkflow.cython_utils.cy_yolo_findboxes",
                  sources=["darkflow/cython_utils/cy_yolo_findboxes.pyx"],
                  libraries=["m"],
                  include_dirs=[numpy.get_include(),"darkflow/cython_utils"]
                  )
    ]

setup(
    version=VERSION,
    name='darkflow',
    description='Darkflow',
    license='GPLv3',
    url='https://github.com/thtrieu/darkflow',
    packages=find_packages(),
    scripts=['flow'],
    ext_modules=cythonize(ext_modules)
)
