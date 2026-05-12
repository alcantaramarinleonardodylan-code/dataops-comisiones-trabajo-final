pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/alcantaramarinleonardodylan-code/dataops-comisiones-trabajo-final.git'
            }
        }

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