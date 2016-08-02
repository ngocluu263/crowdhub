var crowdhub = angular.module('crowdhub', ['ngResource', 'ui.bootstrap']).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});
