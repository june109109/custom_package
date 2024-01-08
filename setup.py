from setuptools import setup, find_packages

setup(
    name='custompackage',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Register any console scripts here
        ],
    },
    author='hj',
    author_email='dbguswn109@gmail.com',
    description='Test',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3.9',
    ],
    project_urls={
        'Source Code': 'https://github.com/june109109/custom_package.git'
    },
)
