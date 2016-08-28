crowdhub.controller('clientsCtrl', function($scope, API) {
    $scope.getClientsList = function(){
        API.ClientsList.list({}, function(data){
            $scope.ClientsList = data
        })
    }
    $scope.getClientsList();

    var TASK1_ID = 31;
    var CLICK_ITEM1_ID = "57bb6af794b68f10de6b054c";
    API.TaskItemsStats.detail({taskId:TASK1_ID, itemId:CLICK_ITEM1_ID}, function (data) {
        $scope.task1 = data;
    })

    var TASK2_ID = 30;
    var CLICK_ITEM2_ID = "57bb6b0694b68f10de6b054d";
    API.TaskItemsStats.detail({taskId:TASK2_ID, itemId:CLICK_ITEM2_ID}, function (data) {
        $scope.task2 = data;
    })
});
