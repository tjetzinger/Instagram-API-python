from setuptools import setup

setup(name='instagram-api',
      version='0.1',
      description='Unofficial instagram API, give you access to ALL instagram features (like, follow, upload photo and video and etc)! Write on python.',
      url='https://github.com/moacirmoda/pygram',
      author='Lions Crayons',
      author_email='info@lionscrayons.com',
      license='GNU',
      packages=['instagram_api'],
      zip_safe=False,
      install_requires=[
          "requests==2.11.1",
          "requests-toolbelt==0.7.0",
      ])