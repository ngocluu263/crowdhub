app.controller('myCtrl', function($scope, API) {
    var CLIENT_ID = 5;
    var TASK_ID = 30;
    var CLICK_ITEM_ID = "57bb6b0694b68f10de6b054d";

    $scope.ClientData = API.ClientsDetail.detail({clientId:CLIENT_ID});
    $scope.item = API.ItemDetail.detail({taskId:TASK_ID, itemId:CLICK_ITEM_ID});
    $scope.loadUser = function () {
        API.UserDetail.detail(function (data) {
            $scope.userId = data.id;
            $scope.getAnnotations();
        });
    }

    $scope.clicks = 0;
    $scope.getAnnotations = function() {
        API.ItemUserAnnotationList.list({taskId:TASK_ID, itemId:CLICK_ITEM_ID, userId:$scope.userId}, function (data) {
            $scope.clicks = data.length;
        });
    }
    $scope.loadUser();

    $scope.onClick = function() {
        API.ItemAnnotationDetail.update({taskId:TASK_ID, itemId:CLICK_ITEM_ID}, "{\"data\":{}}")
        $scope.getAnnotations();
    }
})
