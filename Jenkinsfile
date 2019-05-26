#!/usr/bin/env groovy

node ('slave') {
def GIT_COMMIT

    //check-out-code 
    stage('code-checkout') {
    // some block
deleteDir()

checkout([$class: 'GitSCM', 
    branches: [[name: '${BRANCH}']],
    doGenerateSubmoduleConfigurations: false,
    extensions: [[$class: 'SubmoduleOption',
                  disableSubmodules: false,
                  parentCredentials: true,
                  recursiveSubmodules: true,
                  reference: '',
                  trackingSubmodules: false]],
    submoduleCfg: [],
    userRemoteConfigs: [[credentialsId: 'Git Credentails', url: 'https://github.com/manoj8928/samplecode.git']]])
    }

stage('Build-Test') {
    // Build,Execute test cases & generate/publish report
    sh 'git name-rev --name-only HEAD > GIT_BRANCH'
    sh 'echo GIT_BRANCH'
    git_branch = readFile('GIT_BRANCH').trim()
    env.GIT_BRANCH = git_branch
    sh 'git rev-parse HEAD > GIT_COMMIT' 
    sh 'echo GIT_COMMIT'
    git_commit = readFile('GIT_COMMIT').trim()
    env.GIT_COMMIT = git_commit
    echo sh(script: 'env|sort', returnStdout: true)
    currentBuild.displayName = "#" + currentBuild.number + "." + env.GIT_BRANCH
    //build python
  sh '''#!/bin/bash -ex
  #make release-notes
RELEASE_MESSAGE=`git for-each-ref --count=1 --sort=-taggerdate --format '%(tag) %(contents:subject)'`'''

}


stage ('Deploy to Dev')
{
step([$class: 'AWSEBDeploymentBuilder',
    applicationName: "${params.AWS_EBS_APP_NAME}",
    awsRegion: "${params.AWS_REGION}",
    bucketName: "${params.AWS_BUCKET_NAME}",
    keyPrefix: 'sample-code/build/',
    checkHealth: true,
    credentialId: "${params.AWS_CREDENTIALS}",
    environmentName: "${params.AWS_EBS_ENV_NAME}",
    includes: '',
    excludes: '**/.git/**/*,**/.ebextensions/security-groups.config**,',
    maxAttempts: 3,
    rootObject: '.',
    sleepTime: 90,
    versionDescriptionFormat: '',
    versionLabelFormat: '${BUILD_TAG}',
    zeroDowntime: false])
}
stage ('Email/Slack Notify')
{
echo 'Pipeline Success. Sending slack notification.'
            slackSend channel: '#deployment', color: 'good', message: "Successfully Deployed ${env.JOB_NAME} ${env.GIT_BRANCH} ${env.BUILD_NUMBER} !(<${env.BUILD_URL}|Open>)", tokenCredentialId: 'Slack_Token'
            currentBuild.result = 'SUCCESS'

            echo 'Send email'
        stage ('Email Notification')
        emailext body: '$JOB_URL $GIT_BRANCH', subject: 'Successfully Deployed $JOB_BASE_NAME', to: '$EMAIL_ID'

}

}