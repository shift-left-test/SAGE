pipeline {
  agent {
    docker {
      image "cart.lge.com/swte/yocto-dev:18.04"
    }
  }
  stages {
    stage("Test") {
      steps {
        sh "tox"
      }
    }
    stage("Report") {
      steps {
        junit 'result.xml'
        cobertura coberturaReportFile: 'coverage.xml'
      }
    }
  }
}
