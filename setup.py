import setuptools

with open('README.md', 'r') as fp:
    long_description = fp.read()

setuptools.setup(
    name = 'pathtree',
    version = '0.1.0',
    author = 'skylerlee',
    author_email = 'skyler.ac.lee@gmail.com',
    description = 'Python command line tree printer',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/skylerlee/pathtree',
    packages = setuptools.find_packages(),
    classifiers = (
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    )
)
