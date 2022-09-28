## Before you start you need
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python 3.9](https://www.python.org/downloads/release/python-3913/)
* pip install --upgrade pip

## Add ssh-keys for you profile
You need add keys [here](https://gitlab.com/-/profile/keys) [instruction how to generate](https://coderlessons.com/tutorials/devops/vyuchit-gitlab/gitlab-nastroika-kliucha-ssh)

### Git clone 
`git@github.com:greatlaki/t-scrapy-articles.git`

### Install venv
`cd src` <br />
`python3.9 -m venv venv` <br />
`source ./venv/bin/activate`
### Verify python version
`python --version` <br />
`Python 3.9.12`

- Use command `python -m pip install -U pip` and `pip install -r requirements.txt` to install libraries.
- Go to the folder where `manage.py` is located and use command `python manage.py runserver` to run server.
- Open Postman (or other querying program) and send a POST request to `http://127.0.0.1:8000/products`. You must also attach the xlsx file with the articles to the request.