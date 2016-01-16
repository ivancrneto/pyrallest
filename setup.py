import os
from setuptools import setup

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'README.rst')) as f:
    README = f.read()

    setup(
        name='pyrallest',
        version='0.1.0',
        author='Ivan Neto',
        author_email='ivan.cr.neto@gmail.com',
        description=('Easy Python tests parallelization'),
        long_description=README,
        license='MIT',
        keywords='python testing tests parallelization',
        url='https://github.com/ivancrneto/pyrallest',
        packages=['pyrallest'],
        install_requires=[],
        tests_require=['nose', 'coverage'],
        test_suite='tests',
        entry_points={
            'console_scripts': ['pyrallest=pyrallest:main']
        },
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Development Status :: 3 - Alpha',
            'Natural Language :: English',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Testing'
        ],
    )
