# Karma configuration
# http://karma-runner.github.io/0.12/config/configuration-file.html
# Generated on 2016-05-15 using
# generator-karma 1.0.1

module.exports = (config) ->
  'use strict'
  config.set
    autoWatch: true
    basePath: '../'
    frameworks: [ 'jasmine' ]
    files: [
      'bower_components/jquery/dist/jquery.js'
      'bower_components/angular/angular.js'
      'bower_components/bootstrap-sass-official/assets/javascripts/bootstrap.js'
      'bower_components/angular-animate/angular-animate.js'
      'bower_components/angular-cookies/angular-cookies.js'
      'bower_components/angular-resource/angular-resource.js'
      'bower_components/angular-route/angular-route.js'
      'bower_components/angular-sanitize/angular-sanitize.js'
      'bower_components/angular-touch/angular-touch.js'
      'bower_components/ngstorage/ngStorage.js'
      'bower_components/jsrsasign/jsrsasign-latest-all-min.js'
      'bower_components/oauth-ng/dist/oauth-ng.js'
      'bower_components/angular-mocks/angular-mocks.js'
      'app/scripts/**/*.js'
      'test/mock/**/*.js'
      'test/spec/**/*.js'
    ]
    exclude: []
    port: 8080
    browsers: [ 'PhantomJS' ]
    plugins: [
      'karma-phantomjs-launcher'
      'karma-jasmine'
    ]
    singleRun: false
    colors: true
    logLevel: config.LOG_INFO
  return
