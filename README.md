# Vitrine

Showcase your brand. Built with [Python](https://www.python.org/)

## Code Style
All HTML files are [w3c validated](https://github.com/alx-tools/W3C-Validator).
* **Validating HTML files**
```bash
alias w3cvalidate='~/W3C-Validator/w3c_validator.py'
w3cvalidate *.html
```
Python files in this codebase follow [Pycodestyle](https://pypi.org/project/pycodestyle/).
* **Validating Python files**
```bash
pycodestyle .
```

## Tests
This project is tested with the unittest module.
* **Run Tests**
*Run database setup scripts first*
```
VIT_ENV=test VIT_MYSQL_USER=vit_test VIT_MYSQL_PWD=vit_test_pwd VIT_MYSQL_DB=vit_test_db VIT_MYSQL_HOST=localhost python3 -m unittest
```

## API
The API is built with [Flask](https://flask.palletsprojects.com), it integrates Cross-Origin Resource Sharing(CORS) with the help of [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/).
* **Run API**
*Run database setup scripts first*
```
VIT_ENV=dev VIT_MYSQL_USER=vit_dev VIT_MYSQL_PWD=vit_dev_pwd VIT_MYSQL_DB=vit_db VIT_MYSQL_HOST=localhost VIT_API_HOST=0.0.0.0 VIT_API_PORT=5000 python3 -m api.v1.app
```
