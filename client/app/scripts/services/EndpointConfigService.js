angular.module('todoApp')
    .constant('CURRENT_BACKEND', 'node')
    //.constant('CURRENT_BACKEND', 'firebase')
    .service('EndpointConfigService', function($rootScope, CURRENT_BACKEND) {
        var service = this,
            endpointMap = {
                firebase: {
                    URI: '',
                    root: 'clients/',
                    format: '.json' },
                node: {
                    URI: 'http://localhost:5000/',
                    root: 'api/v1.0',
                    format: ''}
            },
            currentEndpoint = endpointMap[CURRENT_BACKEND],
            userId = null,
            backend = CURRENT_BACKEND;

        service.getUrl = function(model) {
            return currentEndpoint.URI + currentEndpoint.root + model;
        };

        service.getUrlForId = function(model, id) {
            return service.getUrl(model) + id + currentEndpoint.format;
        };

        service.getCurrentBackend = function() {
            return backend;
        };

        service.getCurrentFormat = function() {
            return currentEndpoint.format;
        };

        service.getCurrentURI = function() {
            return currentEndpoint.URI;
        };

        $rootScope.$on('onCurrentUserId', function(event, id){
            userId = id;
        });
    });
