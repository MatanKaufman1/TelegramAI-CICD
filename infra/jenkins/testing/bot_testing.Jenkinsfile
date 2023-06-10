pipeline {
    agent {
        docker {
            image '700935310038.dkr.ecr.us-west-2.amazonaws.com/matan-jenkinsagent-cicd:1'
            args '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        APP_REGISTRY_URL = '700935310038.dkr.ecr.us-west-2.amazonaws.com'
        APP_IMAGE_NAME = 'matan_test_bot_app'
        APP_IMAGE_TAG = '${BUILD_NUMBER}'

        TEST_REGISTRY_URL = '700935310038.dkr.ecr.us-west-2.amazonaws.com'
        TEST_IMAGE_NAME = 'matan_test_bot'
        TEST_IMAGE_TAG = '${BUILD_NUMBER}'
    }



    stages {
        stage('Build app') {
            steps {
                sh '''
                aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin $APP_REGISTRY_URL
                docker build -t $APP_IMAGE_NAME:$APP_IMAGE_TAG -f qa_bot/Dockerfile .
                docker tag $APP_IMAGE_NAME:$BUILD_NUMBER $APP_REGISTRY_URL/$APP_IMAGE_NAME:$BUILD_NUMBER
                docker push $APP_REGISTRY_URL/$APP_IMAGE_NAME:$BUILD_NUMBER
                '''
            }
        }

         stage('Build test ') {
            steps {
                sh '''
                aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin $TEST_REGISTRY_URL
                docker build -t $ TEST_IMAGE_NAME:$BUILD_NUMBER -f qa/bot/Dockerfile .
                docker tag $TEST_IMAGE_NAME:$BUILD_NUMBER $TEST_REGISTRY_URL/$TEST_IMAGE_NAME:$BUILD_NUMBER
                docker push $TEST_REGISTRY_URL/$TEST_IMAGE_NAME:$BUILD_NUMBER
                '''
            }
        }

        stage('Run Containers') {
            steps {
                sh 'echo Start the application container'
                sh "docker run -d --name bot-app-container -e ENV=dev 700935310038.dkr.ecr.us-west-2.amazonaws.com/matan-dev-bot:104 "



                // Start the test code container and link it to the application container
                sh "docker run -d --name matan_test_bot --link  bot-app-container  $IMAGE_NAME:$BUILD_NUMBER"


            }
        }

        stage('Run Tests') {
            steps {
                sh 'echo Execute the tests inside the test code container'
                sh ' docker ps -a'
                sh "docker exec matan_test_bot pytest  700935310038.dkr.ecr.us-west-2.amazonaws.com/matan-dev-bot:104 "
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
            sh 'docker stop matan_test'
            sh 'docker rm matan_test'

        }
    }
}
