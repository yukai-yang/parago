# setup.py
# by Yukai Yang

from setuptools import setup

setup(name='parago',
      version='1.0',
      description='implementing the Go routing and R apply like parallel computation',
      long_description='The package implements two different kinds of parallel computation. One immitates the Go routine like concurrent computation, and the other the R apply like parallel computation. They are featured in the way that the user of the package does not need to know how many cores are deployed and gets the jobs done.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Parallel computation :: Concurrency',
      ],
      keywords='parallel concurrency',
      url='https://github.com/yukai-yang/parago',
      author='Yukai Yang',
      author_email='yukai.yang@statistik.uu.se',
      license='MIT',
      packages=['parago'],
      zip_safe=False)
