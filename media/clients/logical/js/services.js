angular.module('myApp').factory('API', ['$resource',
    function($resource) {
        return {
            ClientsDetail: $resource('/api/clients/:clientId', {clientId:'@clientId'},
                {'detail':{method:'GET'}}
            ),
            ItemDetail: $resource('/api/tasks/:taskId/items/:itemId', {taskId:'@taskId', itemId:'@itemId'},
                {'detail':{method:'GET'}}
            ),
            UserDetail: $resource('/api/users/current', {},
                {'detail':{method:'GET'}}
            ),
            ItemUserAnnotationList: $resource('/api/tasks/:taskId/items/:itemId/annotations?user_id=:userId', {taskId:'@taskId', itemId:'@itemId', userId:'@userId'},
                {'list':{method:'GET', isArray:true}}
            ),
            ItemAnnotationDetail: $resource('/api/tasks/:taskId/items/:itemId/annotations', {taskId:'@taskId', itemId:'@itemId'},
                {'update':{method:'POST'}}
            ),
        };
    }
]);
