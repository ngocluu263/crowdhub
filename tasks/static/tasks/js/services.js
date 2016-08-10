angular.module('crowdhub').factory('API', ['$resource',
    function($resource) {
        return {
            TasksList: $resource('/api/tasks', {},
                {'list':{method:'GET', isArray:true}}
            ),
        };
    }
]);
