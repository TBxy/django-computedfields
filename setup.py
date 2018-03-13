from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError, RuntimeError):
    long_description = ''

setup(
    name='django-computedfields',
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    version='0.0.5',
    license='MIT',
    description='autogenerated and autoupdated database fields for decorated model methods',
    long_description=long_description,
    author='netzkolchose',
    author_email='j.breitbart@netzkolchose.de',
    url='https://github.com/netzkolchose/django-computedfields',
    download_url='https://github.com/netzkolchose/django-computedfields/archive/0.0.5.tar.gz',
    keywords=['django', 'function', 'decorator', 'autoupdate', 'persistent', 'field'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
