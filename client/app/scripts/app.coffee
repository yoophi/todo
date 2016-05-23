'use strict'

###*
# @ngdoc overview
# @name todoApp
# @description
# # todoApp
#
# Main module of the application.
###

angular.module('todoApp', [
  'oauth'
  'ngAnimate'
  'ngCookies'
  'ngResource'
  'ngRoute'
  'ngSanitize'
  'ngTouch'
]).config ($routeProvider, $httpProvider) ->
  $routeProvider.when('/',
    templateUrl: 'views/main.html'
    controller: 'MainCtrl'
    controllerAs: 'main'
  ).when('/about',
    templateUrl: 'views/about.html'
    controller: 'AboutCtrl'
    controllerAs: 'about'
  ).when('/todo',
    templateUrl: 'views/todo.html'
    controller: 'TodoCtrl'
    controllerAs: 'todoList'
  ).when('/auth',
    templateUrl: 'views/auth.html'
    controller: 'AuthCtrl'
    controllerAs: 'auth'
  ).when('/access_token=:accessToken',
    template: ''
    controller: ($location, AccessToken) ->
      hash = $location.path().substr(1)
      AccessToken.setTokenFromString hash
      $location.path '/'
      $location.replace()
      return
  ).otherwise redirectTo: '/'

  $httpProvider.interceptors.push 'OAuth2HttpInterceptor'
  return
