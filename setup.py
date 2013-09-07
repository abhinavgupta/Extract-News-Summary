from setuptools import setup, find_packages

setup(name="ENS",
  version=1.0,
  license='BSD',
  author ='Abhinav Gupta',
  author_email='aag999in@gmail.com',
  packages = find_packages(),
  scripts = ["scripts/ENS_Soup", "scripts/ENS_lxml"]
  )
