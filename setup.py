import ArabicNames
from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name=ArabicNames.__title__,
    version=ArabicNames.__version__,
    author=ArabicNames.__author__,
    author_email=ArabicNames.__author_email__,
    url="https://github.com/AhmedMadbouly/ArabicNames",
    description="Generate random arabic names",
    long_description='\n\n'.join((
        readme,
    )),
    license=ArabicNames.__license__,
    packages=find_packages(),
    package_data={'ArabicNames': ['.*csv']},
    include_package_data=True,
    install_requires=['pandas',                    
        ],
    entry_points={
        'console_scripts': [
            'ArabicNames = ArabicNames.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
