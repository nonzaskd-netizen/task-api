pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/nonzaskd-netizen/task-api.git'
            }
        }

        stage('Setup') {
            steps {
                echo "Running on branch main"

                bat 'C:\\Python\\Python314\\python.exe -m venv venv'
            }
        }

        stage('Install') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pytest -v --junitxml=result.xml'
            }
        }
    }

    post {
        always {
            junit testResults: 'result.xml', allowEmptyResults: true
            echo "Pipeline finished."
        }

        success {
            echo "Pipeline SUCCESS - main"
        }

        failure {
            echo "Pipeline FAILED - main"
        }
    }
}