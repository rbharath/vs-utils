from setuptools import setup, find_packages
import sys


def main():
    if 'develop' not in sys.argv:
        raise NotImplementedError("Use python setup.py develop.")
    setup(
        name="pande_gas",
        url='https://github.com/DeepMol/pande-gas',
        description='Pande Lab/GAS collaboration.',
        packages=find_packages(),
    )

if __name__ == '__main__':
    main()
