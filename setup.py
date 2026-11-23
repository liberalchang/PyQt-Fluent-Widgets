import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="PySide6-Fluent-Widgets",
    version="1.11.3-liber.1",
    keywords="pyside6 fluent widgets",
    author="liber",
    author_email="changxianglong@outlook.com",
    description="A fluent design widgets library based on PySide6",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="GPLv3",
    url="https://github.com/liberalchang/PyQt-Fluent-Widgets/tree/PySide6",
    packages=setuptools.find_packages(),
    install_requires=[
        "PySide6",
        "PySideSix-Frameless-Window>=0.8.0",
        "darkdetect",
    ],
    extras_require = {
        'full': ['scipy', 'pillow', 'colorthief', 'PySide6-Addons', 'vispy>=0.9.0', 'numpy>=1.20.0', 'PyOpenGL>=3.1.0']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    project_urls={
        'Documentation': 'https://qfluentwidgets.com/',
        'Source Code': 'https://github.com/liberalchang/PyQt-Fluent-Widgets/tree/PySide6',
        'Bug Tracker': 'https://github.com/liberalchang/PyQt-Fluent-Widgets/issues',
    }
)
