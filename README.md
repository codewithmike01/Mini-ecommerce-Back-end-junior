# Mini E-commerce Flask API

This is a mini ecommerce website, to perform CRUD operations on products. The Flask app that will be used for this project consists of a simple API with three endpoints:

- `GET '/products'`: This gets all products.
- `POST '/products'`: This post a new product .
- `DELETE '/products'`: This sends an array with ids of products to be deleted

## Front-end repo

```bash
  git clone https://github.com/Ginohmk/Sandiweb-Accessment-Front-end-junior.git
```

## Prerequisites

- Python version between 3.7 and 3.9. Check the current version using:

```bash
#  Mac/Linux/Windows
python --version
```

You can download a specific release version from <a href="https://www.python.org/downloads/" target="_blank">here</a>.

- Python package manager - PIP 19.x or higher. PIP is already installed in Python 3 >=3.4 downloaded from python.org . However, you can upgrade to a specific version, say 20.2.3, using the command:

```bash
#  Mac/Linux/Windows Check the current version
pip --version
# Mac/Linux
pip install --upgrade pip==20.2.3
# Windows
python -m pip install --upgrade pip==20.2.3
```

- Terminal
  - Mac/Linux users can use the default terminal.

```bash
pip install -r requirements.txt
```

## Initial setup

1. Locally clone your forked version to begin working on the project.

```bash
git clone https://github.com/Ginohmk/Sandiweb-Accessment-Back-end-junior.git
cd Sandiweb-Accessment-Back-end-junior/
```

1. These are the files relevant for the current project:

```bash
.
├── src
  ├── database
    ├── models.py
  ├── migration
  ├── app.py
  ├── README.md
  ├── requirements.txt
  ├── test_app.py

```
