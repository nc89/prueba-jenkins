pipeline {
    agent any
    triggers {
        // Ejecutar el pipeline al hacer push a la rama develop
        pollSCM('H/5 * * * *')  // Revisa cambios cada 5 minutos
    }
    environment {
        VENV = 'venv'
    }
    stages {
        stage('Setup') {
            steps {
                script {
                    sh '''
                    python -m pip install --upgrade pip
                    python -m venv $VENV
                    source $VENV/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Unit Tests') {
            steps {
                script {
                    sh '''
                    source $VENV/bin/activate
                    pytest --junitxml=results.xml
                    '''
                }
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
        stage('Run Selenium Tests') {
            steps {
                script {
                    sh '''
                    source $VENV/bin/activate
                    pytest tests/
                    '''
                }
            }
        }
    }
    post {
        failure {
            mail to: 'cnicolasadolfo@gmail.com',
                 subject: 'Build Failed: ${env.JOB_NAME}',
                 body: "El build ${env.BUILD_NUMBER} falló. Revisa Jenkins para más detalles."
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
