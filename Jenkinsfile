

pipeline {

    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS=creddentials('9d7ba4fd-8e67-45fa-8a1a-db423ff172c2')
    }

    stages {
        stage('SCM Checkout') {
            steps {
                git 'https://github.com/devalornir/elbit-test.git'
            }
        }
        
        stage('Build docker image'){
            steps {
                sh "docker image build -t flask_docker:$BUILD_NUMBER ."
            }
        }
        stage('Test Docker image'){
            steps {
                sh 'node --version'
            }

        }
        stage('Login to the dockerhub') {
            steps {
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_SUR --password-stdin"

            }
        }
        stage('Push image') {
            steps {
                sh "docker push flask_docker:$BUILD_NUMBER"

            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }

}


