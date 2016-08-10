crowdhub.controller('clientsCtrl', function($scope, API) {
    $scope.getClientsList = function(){
        API.ClientsList.list({}, function(data){
            $scope.ClientsList = data
        })
    }
    $scope.getClientsList();
});
