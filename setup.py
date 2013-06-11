from setuptools import setup, find_packages

def long_desc():
    with open('README.md', 'rb') as f:
        return f.read()

if __name__ == "__main__":
    setup(name="django-nsa",
          version="0.1",
          url="https://github.com/lvm/django-nsa",
          license="MIT",
          author="Mauro",
          author_email="mauro@cacavoladora.org",
          description="An easy way for the NSA to see what's going on in our Django projects.",
          long_description=long_desc(),
          keywords="nsa django hype yay echelon".split(),
          packages=find_packages(),
          zip_safe=False,
          classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "Framework :: Django",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Topic :: Fun",
            ])
