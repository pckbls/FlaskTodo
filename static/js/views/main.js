var MainView = Backbone.View.extend({
    el: ".container",

    events: {
        "click .btn-add-todo": "addTodo"
    },

    initialize: function() {
        this.todo_list_view = new TodoListView({ model: this.model });
        this.todo_editor_view = new TodoEditorView();
    },

    addTodo: function(e) {
        e.preventDefault();
        page.todo_editor_view.show();
    }
});
