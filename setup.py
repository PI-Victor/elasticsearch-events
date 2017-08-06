from setuptools import setup, find_packages

VERSION='0.1'

long_description='A tool that stores AWS events from a resource to elastic search.'
packages=[
    'elasticevents',
]
install_requires=[
    'boto3',
    'click',
]
def main():
    setup_info = dict(
        name='Elasticevents',
        version=VERSION,
        author='Victor Palade',
        description='AWS Tools',
        long_description=long_description,
        license='Apache-2.0',
        packages=packages,
        install_requires=install_requires,
        zip_safe=False,
    )

    setup(**setup_info)

if __name__ == '__main__':
    main()
