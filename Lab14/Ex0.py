import importlib

packages = ["scipy", "statsmodels", "matplotlib"]

for package in packages:
    try:
        importlib.import_module(package)
        print(f"{package} is installed")
    except ImportError:
        print(f"{package} is NOT installed")