pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
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
                bat 'venv\\Scripts\\python.exe -m pytest tests -v --junitxml=result.xml'
            }
        }
    }

    post {
        always {
            junit 'result.xml'
        }
    }
}