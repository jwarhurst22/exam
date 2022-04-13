pipeline {
    agent any
    parameters {
    booleanParam(defaultValue: false, description: 'Deploy the App', name: 'DEPLOY')
    }
    stages {
        stage('Build') {
            steps { 
                withSonarQubeEnv('SonarQube') { 
                    // sh 'mvn -B -DskipTests clean package sonar:sonar' 
                }
            } 
        }
        // stage("Quality Gate") {
        //     steps { 
        //         timeout(time: 1, unit: 'HOURS') { 
        //         waitForQualityGate abortPipeline: true 
        //         }
        //     } 
        // }
        stage('Test') { 
            steps { 
                sh 'mvn test'
            } 
            post { 
                always { 
                    junit 'target/surefire-reports/*.xml' 
                } 
            } 
         }
        stage('Deploy') { 
            steps { 
                sh 'mvn -B -DskipTests -s settings.xml clean deploy' 
            } 
        }
        stage('Package') {
            steps {
                withCredentials([string(credentialsId: 'DockerHub', variable: 'TOKEN')]) {
                    sh "docker login -u 'jawarhurst' -p '$TOKEN' docker.io"
                    sh "docker build -t myapp:latest --tag jawarhurst/samplejava:myapp ."
                    sh "docker push jawarhurst/samplejava:myapp"
                }
            }
        }
         stage('Deliver') { 
             when {
                    expression { params.DEPLOY }
                }
            steps {
                sh 'docker run myapp:latest'
            } 
         }
    }
}