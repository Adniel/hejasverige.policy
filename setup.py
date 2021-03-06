from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='hejasverige.policy',
      version=version,
      description="Heja Sverige Site Policy",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
      ],
      keywords='',
      author='Daniel Grindelid',
      author_email='daniel.grindelid@swedwise.se',
      url='http://www.swedwise.se/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['hejasverige'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
          'Plone',
          'collective.onlogin',
          'Products.PloneFormGen',
          'hejasverige.theme',
          'hejasverige.api',
          'hejasverige.content',
          'hejasverige.megabank',
          'hejasverige.invitation',
          #'hejasverige.ims'
          # -*- Extra requirements: -*-
      ],
      extras_require={
        'test': ['plone.app.testing',]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )
