from setuptools import setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name='file_sort',
    version='0.0.6',
    description='Sorts your media files in PATH://YYYY//MM/DD format based on file metadata or filename',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author='Nishant Ghanate',
    py_modules=['file_sort'],
    install_requires=['setuptools','ExifRead==3.0.0'],
    license_files=["LICENSE"],
    python_requires='>=3.8',
    entry_points = {
        'console_scripts': ['file_sort=file_sort:main'],
    },
)