from setuptools import setup, find_packages

setup(
    name='django-campaignmonitor',
    version=__import__('campaignmonitor').__version__,
    description='Newsletter campaign management app for Django',
    #long_description=open('docs/overview.txt').read(),
    author='Philipp Bosch',
    author_email='hello@pb.io',
    url='http://github.com/philippbosch/django-campaignmonitor',
    packages=find_packages(),
    zip_safe=False,
    package_data = {
        'robots': [
            'locale/*/LC_MESSAGES/*',
            'templates/campaignmonitor/*.html',
        ],
    },
    classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Web Environment',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Framework :: Django',
    ]
)
