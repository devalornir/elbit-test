

pipeline {

    agent {
        docker { image 'node:16.13.1-alpine' }
    }
    
    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub-ornir')
    }

    stages {

        stage('SCM Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-devalore', url: 'https://github.com/devalornir/elbit-test']]])
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

}


