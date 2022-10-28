pipeline {
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

        stage('Docker-Compose Build and Run') {
            steps {
                sh "/bin/bash -c 'docker stop \$(docker ps -a -q)'"
                sh "/bin/bash -c 'docker rm \$(docker ps -a -q)'"
                sh "/bin/bash -c 'docker rmi \$(docker images -a -q)'"
                sh "docker-compose up -d"
            }
        }

    }
}
