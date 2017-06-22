from setuptools import setup

setup(
    name='apihero',
    version='0.1.3',
    description='Restful API documentation generator tool with live unit test.',
    long_description=open('README.rst').read(),
    url='http://github.com/meyt/apihero',
    author='Mahdi Ghane.g',
    license='GPLv3',
    keywords='apihero api_documentation api document_generator',
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
    scripts=['bin/apihero'],
    install_requires=[
        'mako',
        'mistune',
    ],
    include_package_data=True,
    zip_safe=False
)
