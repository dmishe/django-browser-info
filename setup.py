from distutils.core import setup
 
setup(
    name='django-browser-info',
    version='0.9',
    description='Django middleware and view decorator to add browser info to the request object',
    long_description = open("readme.md").read(),
    author='Chris Drackett',
    url = "https://github.com/chrisdrackett/django-browser-info",
    packages = [
        "browser_info",
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
