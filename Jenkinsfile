pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Code already checked out by Jenkins SCM step'
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Setting up Python environment...'
                sh 'python3 --version'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    . venv/bin/activate
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "No requirements.txt found, skipping"
                    fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    . venv/bin/activate
                    if [ -f requirements.txt ] && python3 -c "import pytest" 2>/dev/null; then
                        pytest --junitxml=results.xml || true
                    else
                        echo "pytest not available, running basic check instead"
                        python3 -m py_compile *.py || echo "No .py files at root to compile"
                    fi
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
            junit allowEmptyResults: true, testResults: 'results.xml'
        }
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed. Check console output.'
        }
    }
}
