crowdhub.controller('clientsCtrl', function($scope, API) {
    $scope.getClient = function(clientId){
        API.ClientsDetail.detail({clientId:clientId}, function(data){
            $scope.Client = data
        })
    }
    $scope.getClient(2);
});
