'use strict';

class MainCtrl
  constructor: () ->
    @awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ]

angular.module('todoApp')
  .controller 'MainCtrl', MainCtrl
