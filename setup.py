from setuptools import setup, find_packages

setup(name='statphys_bot',
		version='0.1',
		description='Telegram bot for statphys_lab',
		author='Junghoon Jung',
		author_email='jh.jung@uos.ac.kr',
		packages=find_packages(),
		setup_requires=['python-telegram-bot'],
        scripts=['bin/talert-test']
	 )
