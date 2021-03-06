// Generated by CoffeeScript 1.10.0
(function() {
  var OAuth2HttpInterceptor;

  OAuth2HttpInterceptor = function($q, $location, $log, $rootScope, Storage) {
    return {
      'request': function(config) {
        return config;
      },
      'requestError': function(rejection) {
        return $q.reject(rejection);
      },
      'response': function(response) {
        return response;
      },
      'responseError': function(rejection) {
        var err, error;
        if (rejection.status === 401) {
          try {
            alert(rejection.data.message);
          } catch (error) {
            err = error;
          }
          Storage["delete"]('token');
          $rootScope.$broadcast('oauth:expired');
          $location.path('/auth');
        }
        return $q.reject(rejection);
      }
    };
  };

  angular.module('todoApp').factory('OAuth2HttpInterceptor', ['$q', '$location', '$log', '$rootScope', 'Storage', OAuth2HttpInterceptor]);

}).call(this);

//# sourceMappingURL=OAuth2HttpInterceptor.js.map
