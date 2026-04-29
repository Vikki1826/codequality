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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo '📦 Installing project dependencies...'
                sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Flake8 Linting') {
            steps {
                echo '🔍 Running Flake8 linter...'
                sh '''
                    . venv/bin/activate
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "         FLAKE8 LINT RESULTS           "
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    flake8 src/ tests/ --count --statistics --show-source
                    echo "✅ Flake8 passed - No linting errors found"
                '''
            }
        }
        
        stage('Pylint Analysis') {
            steps {
                echo '📊 Running Pylint code analysis...'
                script {
                    def pylintOutput = sh(
                        script: '''
                            . venv/bin/activate
                            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                            echo "         PYLINT ANALYSIS RESULTS        "
                            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                            pylint src/ --output-format=colorized 2>&1 | tee pylint-report.txt
                            exit ${PIPESTATUS[0]}
                        ''',
                        returnStatus: true
                    )
                    
                    // Extract score from pylint report
                    def scoreMatch = sh(
                        script: '''
                            grep -oP "Your code has been rated at \\K[0-9.]+" pylint-report.txt || echo "0"
                        ''',
                        returnStdout: true
                    ).trim()
                    
                    def score = scoreMatch.toFloat()
                    def threshold = env.PYLINT_THRESHOLD.toFloat()
                    
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "Pylint Score: ${score}/10"
                    echo "Required Threshold: ${threshold}/10"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    
                    if (score < threshold) {
                        error "❌ Pylint score ${score} is below threshold ${threshold}"
                    } else {
                        echo "✅ Pylint passed - Score meets quality threshold"
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'pylint-report.txt', allowEmptyArchive: true
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                echo '🧪 Running pytest unit tests...'
                sh '''
                    . venv/bin/activate
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "           PYTEST RESULTS               "
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    pytest tests/ -v --tb=short --cov=src --cov-report=term-missing --cov-report=html
                '''
            }
            post {
                always {
                    echo '📁 Archiving test coverage report...'
                    archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
                }
            }
        }
        
        stage('Quality Gate Summary') {
            steps {
                echo '''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         🎉 ALL QUALITY GATES PASSED! 🎉
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Flake8 Linting    - PASSED
✅ Pylint Analysis   - PASSED  
✅ Unit Tests        - PASSED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                '''
            }
        }
    }
    
    post {
        success {
            echo '🎊 Pipeline completed successfully!'
        }
        failure {
            echo '💥 Pipeline failed. Check the logs above for details.'
        }
        cleanup {
            echo '🧹 Cleaning up workspace...'
            sh 'rm -rf venv || true'
        }
    }
}
