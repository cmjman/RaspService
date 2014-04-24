import distutils.core

try:
	import setuptools
except ImportError:
	pass

packages=['tornado','sqlalchemy','apscheduler','tornado-rest-handler']

distutils.core.setup(
	name='RaspService',
	version = '0.0.1',
	packages=['handlers','model','scheduler','sensors','test'],
	author='ShiningChan',
	author_email='stone@shiningio.com',
	install_requires=packages
)
