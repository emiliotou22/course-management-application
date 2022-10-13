# Python Client-Server
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
## Table of Contents
* [Background](#background)
* [Install](#install)
* [Usage](#usage)
* [Related Efforts](#related-efforts)
* [Maintainers](#maintainers)
* [Contributing](#contributing)
* [License](#license)
## Background
This program creates a simple, locally hosted client-server network with Python.

The local machine acts as the client and server (with separate directories). And the former sends a serialised Python dictionary or a file from its directory to the latter's directory.
## Install
This program requires [Python3](https://www.python.org/downloads/). Additionaly, ensure access to the following Python modules: [socket](https://docs.python.org/3/library/socket.html), [json](https://docs.python.org/3/library/json.html), [Fernet](https://cryptography.io/en/latest/fernet/), and [dicttoxml](https://pypi.org/project/dicttoxml/). (The former two are built-in.)
```bash
$ git clone https://github.com/adibhaider/Python-Client-Server.git
```
## Usage
Run the Python server first.
```bash
$ python3 server.py
```
Run the client after the server is running.
```bash
$ python3 client.py
```
## Related Efforts
[python-client-server](https://github.com/pricheal/python-client-server) - A basic example of a TCP client/server network using Python's socket and threading library.
## Maintainers
[@adibhaider](https://github.com/adibhaider)
[emiliotou22](https://github.com/emiliotou22)
## Contributing
Feel free to dive in! [Open an issue](https://github.com/adibhaider/Python-Client-Server/issues/new) or submit PRs.

Standard Readme follows the [Contributor Covenant](https://www.contributor-covenant.org/version/1/3/0/code-of-conduct/) Code of Conduct.
## License
[MIT](https://github.com/adibhaider/Python-Client-Server/blob/main/LICENSE)
