pipeline {
    agent any

    stages {
        stage('Compilacion') {
            steps {
                echo 'Paso 1'
            }
        }
        stage('Test') {
            steps {
                echo 'Paso 2'
            }
        }
        stage('Final') {
            steps {
                echo 'Paso 3'
                exit 1
            }
        }
    }
}
