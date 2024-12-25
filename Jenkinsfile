pipeline {
    stages {
        stage('Setup') {
            steps {                
                script {
                    sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }                          
            }
        }
        stage('Run Unit Tests') {
            steps {                                                    
                pytest --junitxml=results.xml                                
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
        stage('Run Selenium Tests') {
            steps {
                pytest tests/
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
