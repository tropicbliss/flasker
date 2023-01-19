# flasker

Bootstrap a Flask and SQLAlchemy project. Get autocomplete out of the box with Visual Studio Code.

## Install instructions

1. Install Poetry by following its [installation instructions](https://python-poetry.org/docs/). Make sure that the system path to Poetry is specified in your environment variables.
2. Clone this repo.
3. Run the following commands:

```sh
poetry install
```

If you are on Windows, run the following commands in Powershell as an administrator to enable running Powershell scripts from Poetry:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

4. From Visual Studio Code, switch your default python interpreter to that of this project.
5. Run the web server by running the following commands:

```bash
poetry run python index.py
```
