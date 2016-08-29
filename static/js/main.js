var todos;

var bootstrap = function(callback) {
    todos = new TodoCollection();
    todos.fetch({
        success: function() {
            callback();
        },
        error: function() {
            console.log("error occurred while bootstrapping...");
        }
    });
};

$(document).ready(function() {
    bootstrap(function() {
        page = new MainView({ model: todos });
    });
});
