pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Requirements') {
            steps {
                bat 'pip install --user -r requirements.txt'
            }
        }

        stage('Groovy'){
            steps {
                script {
                    groove = load 'main.groovy'
                    groove.func('prod')
                }
            }
        }
    }
}
