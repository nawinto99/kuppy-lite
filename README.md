# Kuppy Lite
The Kubernetes-Ready Python Web Application Template is a comprehensive solution designed to simplify the deployment of Python web applications on Kubernetes.

This repository provides a ready-to-use Python Flask boilerplate template for deploying Flask applications on Kubernetes. It includes all the necessary files and configurations to automate the deployment process using GitHub Actions.

## Features

- Flask application template with basic routes and error handling.
- Dockerfile for containerizing the Flask application.
- Kubernetes deployment and service files for easy deployment on Kubernetes clusters.
- GitHub Actions workflow for automating the deployment process.
- Pre-configured code formatters and linters for maintaining code quality.
- Unit testing setup using pytest for ensuring the correctness of the application.

## Getting Started

To get started with this Flask boilerplate template and deploy it on Kubernetes, follow these steps:

1. Make sure you have Python installed on your system. You can install Cookiecutter by running the following command in your terminal or command prompt:
   ```
   pip install cookiecutter
   ```
2. In your terminal or command prompt, navigate to the directory where you want to create your project. Run the following command
   ```
   cookiecutter https://github.com/nawinto99/kuppy-lite.git
   ```
3. Cookiecutter will prompt you for input based on the template's configuration. This could include things like project name, author name, etc. Fill in the requested information and press Enter after each input.
4. Project Generation: After you've provided all the required input, Cookiecutter will generate the project using the template. It will create the project structure and populate it with the necessary files and folders.
5. Install poetry and dependencies
     ```
     pip install poetry
     poetry install
     ```
6. Customize the Flask application code in the `app.py` file to meet your project requirements.
7. Update the Dockerfile to include any additional dependencies or configurations.
8. Modify the Kubernetes deployment and service files (`deployment.yaml` and `service.yaml`) to match your application's specifications.
9. Set up the necessary secrets and environment variables in your GitHub repository settings. This includes Docker Hub credentials, Kubernetes cluster credentials, and any other required environment variables.
10. Customize the GitHub Actions workflow (`deploy.yaml`) to match your deployment needs and configure the necessary environment variables and secrets.
11. Commit your changes and push them to the `main` branch of your GitHub repository.
12. GitHub Actions will automatically trigger the deployment workflow, building a Docker image, pushing it to a container registry, and deploying the application on your Kubernetes cluster.

## Testing and Code Quality

This template includes pre-configured code formatters (flake8, black), a security linter (bandit), and a unit testing framework (pytest). To ensure code quality and correctness, follow these guidelines:

- Run the code formatters before committing any changes. Use the command `poetry run pre-commit run --all-files` to automatically format the code according to the defined rules.
- Run the security linter using `poetry run bandit -r .` to identify potential security issues in your code.
- Write unit tests for your Flask application in the `tests` directory and run them using `poetry run pytest`.

## Contributing

Contributions to this Flask boilerplate template are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use it as a starting point for your own Flask projects.

Happy coding!
