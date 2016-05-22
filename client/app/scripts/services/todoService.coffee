'use strict';

class TodoService
  constructor: (@$http, @$location, @Storage, @AccessToken, @EndpointConfigService) ->
    @todos = []
    @access_token = undefined
    @storage_token = @Storage.get 'token'
    @access_token = @storage_token.access_token if @storage_token

  all: () ->
    console.log 'todos.all()'
    console.log headers: @headers()
    promise = @$http.get @EndpointConfigService.getUrl('/todos'), headers: @headers()
    promise.success (response) =>
      @todos = response.todos
    promise

  create: (obj) ->
    promise = @$http.post @EndpointConfigService.getUrl('/todos'), obj, headers: @headers()
    promise.success (response) =>
      @todos = response.todos
    promise

  getRemaining: () =>
    count = 0
    angular.forEach @todos, (todo) ->
      count++ if todo.is_completed
    count

  remove: (obj) ->
    promise = @$http.delete @EndpointConfigService.getUrl("/todo/#{ obj.id }"), headers: @headers()
    promise.success (response) =>
      @todos = response.todos
    promise

  archive: () ->
    angular.forEach @todos, (todo) =>
      @remove(todo) if todo.is_completed

    @.all()

  update: (obj) ->
    data =
      'title': obj['title']
      'priority': obj['priority']
      'is_completed': obj['is_completed']

    promise = @$http.put @EndpointConfigService.getUrl("/todo/#{ obj.id }"), data, headers: @headers()
    promise

  headers: () =>
    console.log 'todos.headers()'
    console.log @access_token
    if @access_token
      Authorization: "Bearer #{@access_token}"
    else
      {}


TodoService.$inject = ['$http', '$location', 'Storage', 'AccessToken', 'EndpointConfigService']

angular.module('todoApp')
  .service 'TodoService', TodoService
