pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t dataops-comisiones .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm -v $(pwd):/app dataops-comisiones'
            }
        }
    }
}
