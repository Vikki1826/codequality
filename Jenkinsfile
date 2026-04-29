pipeline {
    agent any

    environment {
        PYLINT_THRESHOLD = '8.0'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out source code...'
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo '🔧 Setting up Python virtual environment...'
                bat '''
                python -m venv venv
                venv\\Scripts\\activate
                python -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installing dependencies...'
                bat '''
                venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Flake8 Linting') {
            steps {
                echo '🔍 Running Flake8...'
                bat '''
                venv\\Scripts\\activate
                flake8 src tests
                '''
            }
        }

        stage('Pylint Analysis') {
            steps {
                echo '📊 Running Pylint...'
                bat '''
                venv\\Scripts\\activate
                pylint src > pylint-report.txt
                '''
                bat 'type pylint-report.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests...'
                bat '''
                venv\\Scripts\\activate
                pytest tests
                '''
            }
        }

        stage('Quality Gate Summary') {
            steps {
                echo '✅ All stages executed successfully!'
            }
        }
    }

    post {
        success {
            echo '🎉 Pipeline SUCCESS'
        }
        failure {
            echo '❌ Pipeline FAILED'
        }
        always {
            archiveArtifacts artifacts: 'pylint-report.txt', allowEmptyArchive: true
        }
    }
}
