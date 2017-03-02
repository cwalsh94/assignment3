from setuptools import setup
setup(name="solve_led",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
    
      author="Claire Walsh",
      author_email="claire.walsh2@ucdconnect.ie",
      licence="GPL3",
      packages=['Claire'],
      entry_points={
          'console_scripts':['solve_led=Claire.main:main']
          }
      )
  