import setuptools

setuptools.setup(
    name="ifes-elections",
    version="0.0.0",
    description="IFES Elections Data Visualization",
    url="https://github.com/DataKind-DC/ifes-elections",
    author="DataKind",
    packages=["src"],
    install_requires=[
        "python-dotenv>=0.15.0",
        "requests>=2.25.1",
    ],
    zip_safe=False,
)
