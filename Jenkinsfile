pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'spe_calculator'
        GITHUB_REPO_URL = 'https://github.com/substobeme/SPEMINIPROJ.git'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
                }
            }
        }
        
        
        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest test_cal.py'
            }
        }
        stage('Build Docker Image') {
            steps {
            sh "docker build -t ${DOCKER_IMAGE_NAME} ."
              }
                }

        
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'mydocker') {
                        sh 'docker tag scientific_calculator substobeme/spe_calculator:latest'
                        sh 'docker push substobeme/spe_calculator:latest'
                    }
                }
            }
        }
        
        stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory.ini'
                    )
                }
            }
        }
    }
}
