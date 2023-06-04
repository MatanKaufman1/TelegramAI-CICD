pipeline {
    agent any


    stages {
        stage('Install dependencies') {
            steps {
                script {
                    def nexusUrl = 'http://35.161.122.163:8081/repository/pypi-hosted/'
                    def nexusCredentialsId = 'matan_nexus'

                    withCredentials([usernamePassword(credentialsId: nexusCredentialsId, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh ''' cd 15_fantastic_ascii '''
                        sh "pip install --index-url=${nexusUrl} --trusted-host http://35.161.122.163 --user --upgrade pip"
                        sh "pip install --index-url=${nexusUrl} --trusted-host http://35.161.122.163 --user -r requirements.txt"
                    }
                }
            }
        }

        stage('Build') {
            steps {

                sh '''
                echo "Nexus Integration Build"
                cd 15_fantastic_ascii
                python3 -m build .
                '''
            }
        }
        stage('Publish') {
           steps {
                withCredentials([usernamePassword(credentialsId: 'matan_nexus', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')
              ]) {

                sh '''
                cd 15_fantastic_ascii
                echo $USERNAME
                echo $PASSWORD
                sed -i -e "s/<username>/$USERNAME/g" .pypirc
                sed -i -e "s/<password>/$PASSWORD/g" .pypirc
                python3 -m twine upload --config-file .pypirc --repository pypi-hosted dist/*
                '''
              }
            }
        }
    }
    post {
        cleanup {
            cleanWs()
        }
    }
}