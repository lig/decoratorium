from setuptools import setup


setup(
    name='decoratorium',
    version='1.0',
    description='Decorator class implementation.',
    url='https://github.com/lig/decoratorium',
    author='Serge Matveenko',
    author_email='s@matveenko.ru',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='python decorator class klass',
    py_modules=['decoratorium'],
    extras_require={
        'test': ['pytest'],
    },
)
