from setuptools import setup

if __name__ == "__main__":
    setup(name="django-nsa",
          version="0.1",
          url="https://github.com/lvm/django_nsa",
          license="MIT",
          author="Mauro",
          author_email="mauro@cacavoladora.org",
          description="An easy way for the NSA to see what's going on in our Django projects.",
          long_description=open('README.md').read(),
          keywords="nsa django hype yay echelon".split(),
	  include_package_data=True,
          packages=['nsa'],
          zip_safe=False,
          install_requires=[
            "Django >= 1.4.3",
            ],
          classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "Framework :: Django",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Topic :: Communications",
            "Topic :: Internet",
            "Topic :: Security",
            ])
