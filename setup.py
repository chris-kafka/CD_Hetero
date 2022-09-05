from setuptools import setup, find_packages
setup(
    name='Hetero',
    version='0.1',
    packages=['Hetero*'],
    install_requires=['py3Dmol','absl-py','biopython',
                      'chex','dm-haiku','dm-tree',
                      'immutabledict','jax','ml-collections',
                      'numpy','pandas','scipy','tensorflow'],
)
