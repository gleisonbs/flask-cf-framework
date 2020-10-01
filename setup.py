import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask-cf-framework", # Replace with your own username
    version="0.0.2",
    author="Gleison Batista",
    # author_email="author@example.com",
    description="A route handler for Google Cloud Functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gleisonbs/flask-cf-framework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)