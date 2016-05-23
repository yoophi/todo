'use strict';

class AboutCtrl
  constructor: () ->
    @awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ]

angular.module('todoApp')
  .controller 'AboutCtrl', AboutCtrl
