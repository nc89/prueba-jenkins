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
            post{
                always{
                // Notificar que el estado es "Pending"
                step([$class: 'GitHubCommitStatusSetter',
                      contextSource: [$class: 'ManuallyEnteredCommitContextSource', context: 'Setup'],
                      statusResultSource: [$class: 'ConditionalStatusResultSource', results: [
                          [$class: 'AnyBuildResult', state: 'SUCCESS', message: 'Setup finish.'],
                          [$class: 'AnyBuildResult', state: 'FAILURE', message: 'Some setup failed.']
                      ]]
                ]) 
                }
                
            }
        }
        stage('Run Selenium Tests') {
            steps {
                script{
                    bat '''
                    exit 1
                    pytest tests/                    
                    '''
                }                
            }
            post{
                always {
                    // Notificar éxito o fallo de los tests
                    step([$class: 'GitHubCommitStatusSetter',
                          contextSource: [$class: 'ManuallyEnteredCommitContextSource', context: 'Tests'],
                          statusResultSource: [$class: 'ConditionalStatusResultSource', results: [
                              [$class: 'AnyBuildResult', state: 'SUCCESS', message: 'Tests passed.'],
                              [$class: 'AnyBuildResult', state: 'FAILURE', message: 'Some tests failed.']
                          ]]
                    ])
                }
            }
        }
    }
    post {
        failure {
            step([$class: 'GitHubCommitStatusSetter',
                  contextSource: [$class: 'ManuallyEnteredCommitContextSource', context: 'Pipeline'],
                  statusResultSource: [$class: 'ConditionalStatusResultSource', results: [
                      [$class: 'AnyBuildResult', state: 'FAILURE', message: 'Pipeline failed.']
                  ]]
            ])
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
            step([$class: 'GitHubCommitStatusSetter',
                  contextSource: [$class: 'ManuallyEnteredCommitContextSource', context: 'Pipeline'],
                  statusResultSource: [$class: 'ConditionalStatusResultSource', results: [
                      [$class: 'AnyBuildResult', state: 'SUCCESS', message: 'Pipeline succeeded.']
                  ]]
            ])
            echo 'Build succeeded!'
        }
    }
}
