OAuth2HttpInterceptor = ($q, $location, $log, $rootScope, Storage) ->
  return {
    'request': (config) ->
      # do something on success
      config

    'requestError': (rejection) ->
      # do something on error
      $q.reject rejection

    'response': (response) ->
      # do something on success
      response

    'responseError': (rejection) ->
      if rejection.status is 401
        # TODO: try to get access_token using refresh_token
        try
          alert rejection.data.message
        catch err

        Storage.delete 'token'
        $rootScope.$broadcast 'oauth:expired'
        $location.path '/auth'

      $q.reject rejection
  }

angular.module('todoApp')
  .factory 'OAuth2HttpInterceptor', OAuth2HttpInterceptor
