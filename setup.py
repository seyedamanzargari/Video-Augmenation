from setuptools import setup, find_packages

setup(
    name='VideoAug',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/seyedamanzargari/VidAug',
    license='MIT',
    author='SeyedAman Zargari',
    author_email='seyedamanzargari@gmail.com',
    description='Toolbox for Video Augmentation',
    install_requires=['albumentations', 'opencv-python', 'tqdm']
)
