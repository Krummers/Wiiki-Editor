# Wiiki Editor
This repository contains various classes and functions that allow easy editing access to wiki.tockdom.com.

## Requirements
* [Python](https://www.python.org/downloads/)
* [mwclient](https://pypi.org/project/mwclient/)

## Contributing
To contribute to this editor, follow these steps:

1. Fork the repository and clone it to your device.
2. Make your desired changes and additions and commit them.
3. Open a pull request on the main repository, describing your changes.

Once your pull request is submitted, it will be reviewed by the project's maintainers. They will provide feedback and work with you to ensure that your contribution aligns with the project's guidelines and quality standards.

## Bug reports and feature requests
If you notice any bugs in the code or want to request a feature, please do so in the [Issues section](https://github.com/Krummers/Wiiki-Editor/issues).

## Building distribution and testing module
Follow these instructions to test a build. This requires [twine](https://pypi.org/project/twine/) to be installed.
1. Copy this repository to your device.
2. Make any changes to the code if you want to test them.
3. Edit the version number of `pyproject.toml` to one that has not been used before, preferably one bigger than the previous one.
4. Select your correct prefix for commands. In future steps, if `prefix` is used, use the correct prefix for your operating system. `py` for Windows, `python3` for Unix/macOS.
5. Create an account at [TestPyPi](https://test.pypi.org/account/register/) and verify it.
6. Execute the command `prefix -m build` in the root directory. This should create a `dist` folder with the module files.
7. Execute the command `prefix -m twine upload --repository testpypi dist/*`. This will upload the module to a test server. Use `__token__` as a username and the API token (found in `api_token.txt`) as a password. Note that copy-pasting something into the password prompt in a Windows command prompt is broken. Instead insert it under Edit > Paste.
8. Visit the "View at:" link and copy and run the command.
9. Use `import wiiki_editor` in a Python environment to test the build.
