pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {                
                script {
                    bat '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }                          
            }
        }
        stage('Run Selenium Tests') {
            steps {
                script{
                    bat '''
                    pytest tests/
                    '''
                }
                
            }
        }
    }
    post {
        failure {
            emailext (
                subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                El build #${env.BUILD_NUMBER} falló.
                Revisa los detalles en Jenkins: ${env.BUILD_URL}
                NICOLAS ADOLFO CARDENAS PATIÑO
                """,
                to: "cnicolasadolfo@gmail.com",
                recipientProviders: [[$class: 'CulpritsRecipientProvider'], [$class: 'DevelopersRecipientProvider']]
            )
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
