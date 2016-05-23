// Generated by CoffeeScript 1.10.0
(function() {
  var EndpointConfigService;

  EndpointConfigService = (function() {
    function EndpointConfigService($rootScope, CURRENT_BACKEND) {
      var endpointMap;
      this.$rootScope = $rootScope;
      this.CURRENT_BACKEND = CURRENT_BACKEND;
      endpointMap = {
        firebase: {
          URI: '',
          root: 'clients/',
          format: '.json'
        },
        node: {
          URI: 'http://localhost:5000/',
          root: 'api/v1.0',
          format: ''
        }
      };
      this.currentEndpoint = endpointMap[this.CURRENT_BACKEND];
      this.userId = null;
      this.backend = this.CURRENT_BACKEND;
      this.$rootScope.$on('onCurrentUserId', (function(_this) {
        return function(event, id) {
          _this.userId = id;
        };
      })(this));
    }

    EndpointConfigService.prototype.getUrl = function(model) {
      return this.currentEndpoint.URI + this.currentEndpoint.root + model;
    };

    EndpointConfigService.prototype.getUrlForId = function(model, id) {
      return this.getUrl(model) + id + this.currentEndpoint.format;
    };

    EndpointConfigService.prototype.getCurrentBackend = function() {
      return this.backend;
    };

    EndpointConfigService.prototype.getCurrentFormat = function() {
      return this.currentEndpoint.format;
    };

    EndpointConfigService.prototype.getCurrentURI = function() {
      return this.currentEndpoint.URI;
    };

    return EndpointConfigService;

  })();

  EndpointConfigService.$inject = ['$rootScope', 'CURRENT_BACKEND'];

  angular.module('todoApp').constant('CURRENT_BACKEND', 'node').service('EndpointConfigService', EndpointConfigService);

}).call(this);

//# sourceMappingURL=EndpointConfigService.js.map