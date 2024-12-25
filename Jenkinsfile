pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {                
                script {
                    bat '''
                    python -m pip install --upgrade pip &&
                    pip install -r requirements.txt
                    '''
                }                          
            }
        }
        stage('Run Unit Tests') {
            steps {     
                script{
                    bat '''
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
                <h3>El build <b>#${env.BUILD_NUMBER}</b> falló.</h3>
                <p>Revisa los detalles en Jenkins: ${env.BUILD_URL}</p>
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
