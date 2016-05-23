class EndpointConfigService
  constructor: (@$rootScope, @CURRENT_BACKEND) ->
    endpointMap =
      firebase:
        URI: ''
        root: 'clients/'
        format: '.json'
      node:
        URI: 'http://localhost:5000/'
        root: 'api/v1.0'
        format: ''

    @currentEndpoint = endpointMap[@CURRENT_BACKEND]
    @userId = null
    @backend = @CURRENT_BACKEND

    @$rootScope.$on 'onCurrentUserId', (event, id) =>
      @userId = id
      return

  getUrl: (model) ->
    @currentEndpoint.URI + @currentEndpoint.root + model

  getUrlForId: (model, id) ->
    @getUrl(model) + id + @currentEndpoint.format

  getCurrentBackend: ->
    @backend

  getCurrentFormat: ->
    @currentEndpoint.format

  getCurrentURI: ->
    @currentEndpoint.URI


EndpointConfigService.$inject = ['$rootScope', 'CURRENT_BACKEND']

angular.module('todoApp')
  .constant('CURRENT_BACKEND', 'node')
  .service 'EndpointConfigService', EndpointConfigService

