pipeline {
    agent { label 'master' }
    stages {
        stage('Print pipeline info') {
            steps {
                echo "--- Pipeline to deploy Apache Web Server in server 192.168.120.202"
            }
        }//end stage Print pipeline info
        stage('Deploy Apache Web Server'){
            steps{
                echo "--- Deploying Apache Web Server"
                ansiblePlaybook(
                    playbook: './apache.yml',
                    inventory: './hosts',
                    credentialsId: 'root_ssh_key',
                    disableHostKeyChecking: true,
                    colorized: true
                )
            }
        }//end stage Deploy Apache Web Server
        stage('Testing'){
            steps{
                echo "--- Testing"
                sh 'execute_test.sh'
                junit 'test_apache.xml' //record test result
            }
        }//end stage Testing
        stage('Finish'){
            steps{
                echo "--- Deployment finished"
            }
        }// end stage Finish
    }
}
