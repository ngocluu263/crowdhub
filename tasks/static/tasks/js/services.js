angular.module('crowdhub').factory('TasksList', function($resource) {
    return $resource('/api/tasks/tasks',{},
        {'list':{method:'GET', isArray:true}}
    );
});
