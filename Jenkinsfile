pipeline {z
    agent any 
    stages {
        stage('Tests') {
            steps {
                dir('flask-app'){
                    sh "echo this is a test"
                    sh "chmod +x application/tests/test_app.py"
                    sh "bash test.sh"
                }
            }
        }

        stage('docker push') {
            environment {
                    DOCKER_CRED = credentials('DOCKER_CRED')   
                }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u ${DOCKER_CRED_USR} -p ${DOCKER_CRED_PSW}"
                sh "docker-compose push" 
            }
        }
        stage('docker swarm') { 
              steps {
                sh "docker stack deploy --compose-file docker-compose.yaml flask-app"    
              }
        }
    }
}
