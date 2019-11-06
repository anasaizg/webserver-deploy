pipeline {
    agent { label 'master' }
    stages {
        stage('Print pipeline info') {
            steps {
                echo "--- Deploying Apache Web Server in server 192.168.120.202"
            }
        }//end stage Print pipeline info
        stage('Deploy Apache Web Server'){
            steps{
                ansiblePlaybook(
                    playbook: './apache.yml',
                    inventory: './hosts',
                    credentialsId: 'root_ssh_key',
                    colorized: true
                )
            }
        }//end stage Deploy Apache Web Server
        stage('Finish'){
            steps{
                echo "--- Deployment finished"
            }
        }// end stage Finish
    }
}
