// Generated by CoffeeScript 1.10.0
(function() {
  'use strict';
  var TodoService,
    bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  TodoService = (function() {
    function TodoService($http, $location, Storage, AccessToken, EndpointConfigService) {
      this.$http = $http;
      this.$location = $location;
      this.Storage = Storage;
      this.AccessToken = AccessToken;
      this.EndpointConfigService = EndpointConfigService;
      this.headers = bind(this.headers, this);
      this.getRemaining = bind(this.getRemaining, this);
      this.todos = [];
      this.access_token = void 0;
      this.storage_token = this.Storage.get('token');
      if (this.storage_token) {
        this.access_token = this.storage_token.access_token;
      }
    }

    TodoService.prototype.all = function() {
      var promise;
      console.log('todos.all()');
      console.log({
        headers: this.headers()
      });
      promise = this.$http.get(this.EndpointConfigService.getUrl('/todos'), {
        headers: this.headers()
      });
      promise.success((function(_this) {
        return function(response) {
          return _this.todos = response.todos;
        };
      })(this));
      return promise;
    };

    TodoService.prototype.create = function(obj) {
      var promise;
      promise = this.$http.post(this.EndpointConfigService.getUrl('/todos'), obj, {
        headers: this.headers()
      });
      promise.success((function(_this) {
        return function(response) {
          return _this.todos = response.todos;
        };
      })(this));
      return promise;
    };

    TodoService.prototype.getRemaining = function() {
      var count;
      count = 0;
      angular.forEach(this.todos, function(todo) {
        if (todo.is_completed) {
          return count++;
        }
      });
      return count;
    };

    TodoService.prototype.remove = function(obj) {
      var promise;
      promise = this.$http["delete"](this.EndpointConfigService.getUrl("/todo/" + obj.id), {
        headers: this.headers()
      });
      promise.success((function(_this) {
        return function(response) {
          return _this.todos = response.todos;
        };
      })(this));
      return promise;
    };

    TodoService.prototype.archive = function() {
      angular.forEach(this.todos, (function(_this) {
        return function(todo) {
          if (todo.is_completed) {
            return _this.remove(todo);
          }
        };
      })(this));
      return this.all();
    };

    TodoService.prototype.update = function(obj) {
      var data, promise;
      data = {
        'title': obj['title'],
        'priority': obj['priority'],
        'is_completed': obj['is_completed']
      };
      promise = this.$http.put(this.EndpointConfigService.getUrl("/todo/" + obj.id), data, {
        headers: this.headers()
      });
      return promise;
    };

    TodoService.prototype.headers = function() {
      console.log('todos.headers()');
      console.log(this.access_token);
      if (this.access_token) {
        return {
          Authorization: "Bearer " + this.access_token
        };
      } else {
        return {};
      }
    };

    return TodoService;

  })();

  TodoService.$inject = ['$http', '$location', 'Storage', 'AccessToken', 'EndpointConfigService'];

  angular.module('todoApp').service('TodoService', TodoService);

}).call(this);

//# sourceMappingURL=todoService.js.map
