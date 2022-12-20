properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/sergeyka23/DevOps3006.git"
    }
    stage("show files"){
        bat "dir"
    }
}
