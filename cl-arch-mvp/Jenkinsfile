pipeline {
    agent any

    environment {
        // En Jenkins vamos a crear una credencial con este ID
        OPENAI_API_KEY = credentials('OPENAI_API_KEY')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Architecture Review') {
            steps {
                sh 'python tools/arch_check_demo.py'
            }
        }
    }
}
