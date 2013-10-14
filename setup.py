from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(name='buildout.autoapplyplonehotfixes',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Buildout :: Extension",
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='zc.buildout Plone autoapply hotfix',
      author='Alexander Loechel',
      author_email='Alexander.Loechel@lmu.de',
      url='https://github.com/collective/buildout.autoapplyplonehotfixes',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['buildout'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.break_core',
      ],
      entry_points={
        'zc.buildout.extension': ['ext = buildout.autoapplyplonehotfixes:main'],
      },
      )
