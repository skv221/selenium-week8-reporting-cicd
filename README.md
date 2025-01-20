# Week 8: Advanced Automation with CI/CD and Detailed Reporting

This repository contains the final set of tasks for my Selenium learning journey. The focus for this week was on implementing advanced automation strategies, integrating CI/CD pipelines, and generating detailed test reports to enhance the overall testing process.

## Key Tasks and Highlights

### Task 1: CI/CD with GitHub Actions
- **Goal**: Automate test execution and reporting using GitHub Actions.
- **Steps**: Set up GitHub Actions for automating the test execution pipeline, including installing dependencies, running tests, and generating HTML reports.
- **Key Learnings**: Integration of GitHub Actions with Selenium test scripts for seamless automation.

### Task 2: Detailed Test Reporting with Allure
- **Goal**: Generate detailed, interactive test reports with Allure.
- **Steps**: Integrated Allure to produce comprehensive reports from pytest results, making test outcomes more understandable and actionable.
- **Key Learnings**: Enhanced test result visibility with interactive reports that provide better insights into test execution.

### Task 3: Cross-Browser Testing and Headless Execution
- **Goal**: Ensure the scripts work across multiple browsers and in headless mode.
- **Steps**: Implemented cross-browser testing using Chrome, Firefox, and Edge. Also configured headless mode for faster test execution in CI/CD environments.
- **Key Learnings**: Improved test reliability across browsers and reduced test execution time in CI/CD pipelines.

### Task 4: Integration with BrowserStack
- **Goal**: Run tests on cloud-based browsers using BrowserStack.
- **Steps**: Configured BrowserStack for running Selenium tests on different operating systems and browsers, providing broader coverage.
- **Key Learnings**: Enabled cross-platform and cross-browser testing using BrowserStack for more robust automation.

## Technologies Used
- **Selenium WebDriver**
- **Pytest**
- **GitHub Actions**
- **Allure Reporting**
- **BrowserStack**
- **VS Code**

## How to Run the Scripts

1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd <repository-directory>
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Allure**:
   - To install Allure on your local machine, follow these steps:
     - Download and install Allure from [Allure website](https://allure.qatools.ru/).
     - For macOS, use:
       ```bash
       brew install allure
       ```
     - For Windows, you can download the latest version from the [Allure GitHub releases page](https://github.com/allure-framework/allure2/releases).
     - Ensure Allure is added to your system's `PATH` variable.
   
4. Run the tests:
   ```bash
   pytest --alluredir=allure-results
   ```

5. To view the Allure report:
   ```bash
   allure serve allure-results
   ```

## Key Learnings
- Automated test execution with CI/CD using GitHub Actions.
- Generating detailed and interactive test reports using Allure.
- Cross-browser testing and headless execution to speed up testing.
- Integration with BrowserStack for broader test coverage.

## Future Enhancements
- Expand reporting features with more granular test details.
- Further integrate other cloud platforms for testing.
- Continue optimizing CI/CD pipelines for faster feedback loops.

