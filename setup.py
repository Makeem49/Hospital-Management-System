from setuptools import find_packages, setup

# setup(
#     name='HMS-CLI',
#     version='1.0',
#     packages=['cli', 'cli.commands'],
#     include_package_data=True,
#     install_requires=[
#         'click',
#     ],
#     entry_points="""
#         [console_scripts]
#         hms=cli.cli:cli
#     """,
# )

setup(
    name='HMS-CLI',
    version='1.0.0',
    packages=['cli', 'cli.commands'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click',
    ],
    entry_points="""
        [console_scripts]
        hms=cli.cli:cli
    """ 
)