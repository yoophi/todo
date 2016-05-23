'use strict';

class NavCtrl
  constructor: (@$scope, @Storage) ->
    @foo = "bar"

  isLoggedIn: () ->
    storage_token = @Storage.get 'token'
    if storage_token
      return true if storage_token.access_token
    else
      return false

NavCtrl.$inject = ['$scope', 'Storage']

angular.module('todoApp')
  .controller 'NavCtrl', NavCtrl
