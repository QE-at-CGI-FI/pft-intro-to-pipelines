# pft-intro-to-pipelines
Setting up GitHub actions pipeline for running of tests.

## Allure Reporting

The tests use Allure, an open source test reporting framework. To be able to display the reports locally, you need to install allure command line interface. 

You will need to install Java (open jdk) to be able to use allure cli. If you don't have Java installed, you can install it like this:

1. Windows: https://scoop-docs.vercel.app/docs/guides/Java.html
    - if you don't have `scoop` installed, run the following in a Powershell instance:` iwr -useb get.scoop.sh | iex`
2. Linux: `sudo apt-get install openjdk-8-jdk` or `brew install openjdk`

To install Allure command line: https://docs.qameta.io/allure/#_installing_a_commandline 

Then, use the following commands:
- to display the report: `allure serve test-results`
- to save the report: `allure generate test-results`

@allure.title("")
@allure.step("")