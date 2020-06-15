import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="syd_ui",
    version="0.0.1",
    author="David Sarrut",
    author_email="david.sarrut@creatis.insa-lyon.fr",
    description="SYD - Dosimetry for Molecular Radiation Therapy - Minimalist User Interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.in2p3.fr/dsarrut/syd_ui",
    package_dir={ 'syd_ui': 'ui'},
    packages=['syd_ui'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    python_requires='>=3.6',
    install_requires=[
        'syd',
        #'pyside2'
      ],
    scripts=['syd_ui']
)
