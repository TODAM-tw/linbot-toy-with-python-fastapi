# Line Bot Toy with Python FastAPI

## Developing Requirements

Python version `python3.11` or later.

### Build `venv` for **MacOS**
```shell
$ python3.11 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
$ rm -rf venv     # remove the venv
```

### Build `venv` for **Windows**
```shell
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ deactivate
$ rmdir /s venv     # remove the venv
```

### Run web app

Edit the `.env` file with your `YOUR_CHANNEL_ACCESS_TOKEN` and `YOUR_CHANNEL_SECRET`

```shell
$ cp .env.example .env2
```

```shell
$ python main.py

$ ngrok http http://localhost:8080
```

