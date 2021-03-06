angular.module('crowdhub').factory('API', ['$resource',
    function($resource) {
        return {
            ClientsList: $resource('/api/clients', {},
                {'list':{method:'GET', isArray:true}}
            ),
            ClientsDetail: $resource('/api/clients/:clientId', {clientId:'@clientId'},
                {'detail':{method:'GET'}}
            ),
            TaskItemsStats: $resource('/api/tasks/:taskId/items/:itemId/stats', {taskId:"@taskId", itemId:"@itemID"},
                {'detail':{method:'GET'}}
            ),
        };
    }
]);
