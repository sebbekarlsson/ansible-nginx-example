node {
    stage('Preparation') { // for display purposes
        // Get some code from a GitHub repository
        git 'https://github.com/sebbekarlsson/ansible-nginx-example.git'
    }
    stage('Tests') {
        sh  './run_tests.sh'
    }
    stage('Deploy') {
        sh './run.sh'
    }
}