from setuptools import setup

setup(name='KBE',
      version='1.0',
      description='Utilizing ParaPy to Frontload Preliminary UAV Design',
      url='https://github.com/skilkis/KBE',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['KBE'],
      install_requires=[
          'numpy',
          'parapy',
          'xlrd',
          'xlwt',
          'math',
          'json',
          'matplotlib',
      ],
      zip_safe=False)