var Todo = Backbone.Model.extend({
    idAttribute: "id"
});

var TodoCollection = Backbone.Collection.extend({
    model: Todo,

    url: "/api/todo/"
});
