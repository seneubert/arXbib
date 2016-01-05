from setuptools import setup

setup(name='arxbib',
      version='0.1',
      description='Generating bibtex entries from arXiv IDs',
      url='https://github.com/seneubert/arXbib',
      author='Sebastian Neubert',
      author_email='se.neubert@gmail.com',
      license='',
      packages=['arxbib'],
      install_requires=['beautifulsoup4'],
      scripts=['bin/arXbib.py'],
      classifiers=[
          'Development Status :: 0 - PreAlpha',
          'Programming Language :: Python :: 3.4',
      ],
      zip_safe=False)
