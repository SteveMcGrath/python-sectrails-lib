from setuptools import setup, find_packages


with open('sectrails/version.py', 'r') as vfile:
    exec(vfile.read())


setup(
    name='sectrails',
    version=version,  # noqa: F821
    description='SecurityTrails API Library',
    author='Steve McGrath',
    author_email='steve@chigeek.com',
    url='https://github.com/stevemcgrath/sectrails',
    licesne='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='securitytrails security-trails api restfly',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'restfly>=1.4.0',
        'arrow>=1.0.2',
    ]
)
