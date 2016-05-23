'use strict'

###*
# @ngdoc function
# @name todoApp.controller:AboutCtrl
# @description
# # AboutCtrl
# Controller of the todoApp
###
class AuthCtrl
  constructor: (@$scope, @$rootScope, @Storage, @$timeout,
                @$log, @AccessToken, @EndpointConfigService) ->
    @site = @EndpointConfigService.getUrl('')
    @profile_url = @EndpointConfigService.getUrl('/me')

    storage_token = @Storage.get('token')
    if storage_token
      @$scope.accessToken = storage_token.access_token

    @$scope.$on 'oauth:expired', (event) =>
      @$rootScope.accessToken = null
      @$scope.accessToken = null
      return

    @$scope.$on 'oauth:login', (event, token) =>
      @$rootScope.accessToken = token.access_token
      @$scope.accessToken = token.access_token
      return

    @$scope.$on 'oauth:logout', (event) =>
      @$rootScope.accessToken = null
      @$scope.accessToken = null
      return

AuthCtrl.$inject = [
  '$scope', '$rootScope', 'Storage', '$timeout',
  '$log', 'AccessToken', 'EndpointConfigService'
]

angular.module('todoApp')
  .controller 'AuthCtrl', AuthCtrl
