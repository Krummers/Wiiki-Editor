# Wiiki Editor
This repository is a Python module that allows easy bot editing to the [Wiiki](https://wiki.tockdom.com/wiki/Main_Page).

## Requirements
* [Python](https://www.python.org/downloads/) with your preferred editor, of course.
* A bot account with password and API key on the Wiiki.
* [python-dotenv](https://pypi.org/project/python-dotenv/), a module that extracts sensitive information from files.
* [mwclient](https://pypi.org/project/mwclient/), a module that is a Python wrapper for the MediaWiki API.

## Contributing
To contribute to this editor, follow these steps:

1. Fork the repository and clone it to your device.
2. Make your desired changes and additions, test them thouroughly and commit.
3. Open a pull request on the main repository, describing your changes.

Once your pull request is submitted, it will be reviewed by the project's maintainers. They will provide feedback and work with you to ensure that your contribution aligns with the project's guidelines and quality standards.

## Building distribution and testing module
Follow these instructions to test a build. This requires [twine](https://pypi.org/project/twine/) to be installed.
1. Copy this repository to your device.
2. Make any changes to the code if you want to test them.
3. Run `build_install_release.py` to upload and install the new module. `build_release.py` and `install_release.py` can be activated seperately.
4. Use `import wiiki_editor` in a Python environment to test the build. Currently, it is best to use the repository as a reference.

## Bug reports and feature requests
If you notice any bugs in the code or want to request a feature, please do so in the [Issues section](https://github.com/Krummers/Wiiki-Editor/issues).
