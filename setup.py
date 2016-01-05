from setuptools import setup

setup(name='arxbib',
      version='0.1',
      description='Generating bibtex entries from arXiv IDs',
      url='https://github.com/seneubert/arXbib',
      author='Sebastian Neubert',
      author_email='se.neubert@gmail.com',
      license='',
      packages=['arxbib'],
      scripts=['bin/arXbib.py'],
      zip_safe=False)
