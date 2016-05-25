class TodoCtrl
  constructor: (@$scope, @TodoService) ->
    @todos = []
    @getTodos()
    @$scope.todoSortable =
      containment: 'parent'
      cursor: 'move'
      tolerance: 'pointer'

  getTodos: () ->
    @TodoService.all()
      .then (result) =>
        @todos = result.data.todos

  addTodo: () ->
    @TodoService.create(
      "title": @todoText
      "done": false
    ).then (result) =>
      @todoText = ''
      @getTodos()

  remaining: () ->
    @TodoService.getRemaining()

  archive: () ->
    @todos = @TodoService.archive().then (result) =>
      @todos = result.data.todos

  updateTodo: (obj) ->
    @TodoService.update(obj).then (result) =>
      @getTodos()


TodoCtrl.$inject = ['$scope', 'TodoService']

angular.module('todoApp')
  .controller 'TodoCtrl', TodoCtrl

