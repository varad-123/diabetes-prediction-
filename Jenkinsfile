pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/varad-123/diabetes-prediction-.git'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
    }

    post {
        success {
            echo 'Build Successful!'
        }

        failure {
            echo 'Build Failed!'
        }
    }
}
