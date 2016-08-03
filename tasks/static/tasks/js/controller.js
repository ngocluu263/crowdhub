crowdhub.controller('tasksCtrl', function($scope, TasksList) {
    $scope.getTasksList = function(){
        TasksList.list({}, function(data){
            $scope.TasksList = data
        })
    }
    $scope.getTasksList();
});
