pipeline {
    agent any

    stages {
        stage('Construir imagen Docker') {
            steps {
                sh 'docker build -t dataops-comisiones .'
            }
        }

        stage('Ejecutar contenedor') {
            steps {
                sh 'docker run --rm -v $(pwd):/app dataops-comisiones'
            }
        }

        stage('Verificar Excel generado') {
            steps {
                sh 'ls -la'
                sh 'ls -la comisiones.xlsx'
            }
        }
    }
}
