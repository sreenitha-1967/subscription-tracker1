pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'nagireddy7/subscription-tracker'
        DOCKER_USER = 'nagireddy7'
        DOCKER_PASS = Sree2005# // or use env vars locally
    }

    stages {
        stage('Build and Push') {
            steps {
                script {
                    sh """
                        docker build -t $DOCKER_IMAGE .
                        echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin
                        docker push $DOCKER_IMAGE
                    """
                }
            }
        }
    }
}
