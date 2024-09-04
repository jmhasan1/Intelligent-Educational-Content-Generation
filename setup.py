from setuptools import setup, find_packages

setup(
    name="intelligent_content_generation",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "nltk",
        "pandas",
        "transformers",
        "torch",
        "Flask",
        "scikit-learn",
        "requests",
        "kaggle",
    ],
    entry_points={
        "console_scripts": [
            "data_collection=src.data.data_collection:main",
            "data_preprocessing=src.data.data_preprocessing:main",
            "data_exploration=src.data.data_exploration:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
