crowdhub.controller('tasksCtrl', function($scope, API) {
    $scope.getTasksList = function(){
        API.TasksList.list({}, function(data){
            $scope.TasksList = data
        })
    }
    $scope.getTasksList();
});
