'use strict';

/**
 * @ngdoc function
 * @name todoApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the todoApp
 */
angular.module('todoApp')
    .controller('NavCtrl', function ($scope, Storage) {
        var nav = this;
        nav.foo = 'bar';

        nav.isLoggedIn = function() {
            var storage_token = Storage.get('token');
            if (storage_token) {
                //$scope.accessToken = storage_token.access_token;
                if (storage_token.access_token) {
                    return true;
                }
            }
            return false;
        }
    });
