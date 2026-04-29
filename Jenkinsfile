pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out source code...'
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo '🔧 Creating virtual environment...'
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installing dependencies...'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Flake8 Linting') {
            steps {
                echo '🔍 Running Flake8...'
                bat 'venv\\Scripts\\flake8 src tests'
            }
        }

        stage('Pylint Analysis') {
            steps {
                echo '📊 Running Pylint...'
                bat 'venv\\Scripts\\pylint src > pylint-report.txt'
                bat 'type pylint-report.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests...'
                bat 'venv\\Scripts\\pytest tests'
            }
        }

        stage('Done') {
            steps {
                echo '✅ Pipeline completed successfully!'
            }
        }
    }

    post {
        success {
            echo '🎉 SUCCESS'
        }
        failure {
            echo '❌ FAILED'
        }
        always {
            archiveArtifacts artifacts: 'pylint-report.txt', allowEmptyArchive: true
        }
    }
}
