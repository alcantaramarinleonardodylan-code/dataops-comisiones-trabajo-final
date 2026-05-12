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
                sh '''
                docker rm -f contenedor-comisiones || true
                docker create --name contenedor-comisiones dataops-comisiones
                docker start -a contenedor-comisiones
                docker cp contenedor-comisiones:/app/comisiones.xlsx ./comisiones.xlsx
                docker rm contenedor-comisiones
                '''
            }
        }

        stage('Verificar Excel generado') {
            steps {
                sh 'ls -la'
                sh 'ls -la comisiones.xlsx'
                archiveArtifacts artifacts: 'comisiones.xlsx', fingerprint: true
            }
        }
    }
}
