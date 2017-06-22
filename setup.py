from setuptools import setup
import os.path
import re

# reading package's version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__), 'apihero', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

setup(
    name='apihero',
    version=package_version,
    description='Restful API documentation generator tool with live unit test.',
    long_description=open('README.rst').read(),
    url='http://github.com/meyt/apihero',
    author='Mahdi Ghane.g',
    license='GPLv3',
    keywords='apihero api_documentation api document_generator raml_client_builder',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Documentation',
        'Topic :: Documentation',
        'Topic :: Software Development :: Build Tools'
    ],
    packages=['apihero'],
    install_requires=[
        'mako',
        'pyraml-parser'
    ],
    entry_points={
        'console_scripts': [
            'apihero = apihero:main'
        ]
    },
    include_package_data=True,
    zip_safe=False
)
