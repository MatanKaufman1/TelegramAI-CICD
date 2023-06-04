pipeline {
    agent {
        docker {
            image '700935310038.dkr.ecr.us-west-2.amazonaws.com/matan-jenkinsagent-cicd:1'
            args '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        REGISTRY_URL = '700935310038.dkr.ecr.us-west-2.amazonaws.com'
        IMAGE_NAME = 'matan_test_bot'
        IMAGE_TAG = '${BUILD_NUMBER}'
    }



    stages {
        stage('Build') {
            steps {
                sh '''
                aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin $REGISTRY_URL
                docker build -t $IMAGE_NAME:$BUILD_NUMBER -f qa/Dockerfile .
                docker tag $IMAGE_NAME:$BUILD_NUMBER $REGISTRY_URL/$IMAGE_NAME:$BUILD_NUMBER
                docker push $REGISTRY_URL/$IMAGE_NAME:$BUILD_NUMBER
                '''
            }
        }

        stage('Run Containers') {
            steps {
                sh 'echo Start the application container'
                sh "docker run -d --name bot-app-container 700935310038.dkr.ecr.us-west-2.amazonaws.com/matan-dev-bot:104 "



                // Start the test code container and link it to the application container
                sh "docker run -d --name matan-test --link bot-app-container $IMAGE_NAME:$BUILD_NUMBER"
            }
        }

        stage('Run Tests') {
            steps {
                sh 'echo Execute the tests inside the test code container'
                sh "docker exec matan_test_bot pytest 700935310038.dkr.ecr.us-west-2.amazonaws.com/matan-dev-bot:104"
            }
        }

        stage('Collect Results') {
            steps {
                // Copy the test results from the test code container to the Jenkins workspace
                sh 'docker cp matan_test_bot:/path/to/tests/results.xml .'

                // Publish the test results in Jenkins
                junit 'results.xml'
            }
        }


    }

    post {
        always {
            sh 'docker image prune -a --filter "until=64" --force'
            sh 'docker stop bot-app-container'
            sh 'docker rm bot-app-container'
            sh 'docker stop matan_test_bot'
            sh 'docker rm matan_test_bot'

        }
    }
}
