import setuptools

setuptools.setup(
    name="validatejson",
    version="0.1",
    author="deeppy",
    description="Validate JSON payload against the JSON schema",
    url="",
    packages=["validatejson"],
    install_requires=['jsonschema','typer'],
    entry_points={
        'console_scripts': ['validatejson=validatejson.validate:run_app']
    }
)