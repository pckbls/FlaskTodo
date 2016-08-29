var TodoListView = Backbone.View.extend({
    el: "#todo-list",

    initialize: function() {
        _.bindAll(this, "add");
        this.listenTo(this.model, "add", this.add);
        this.reset();
    },

    add: function(todo) {
        var v = new TodoListItemView({ model: todo });
        this.$el.append(v.render().$el);
    },

    reset: function() {
        this.$el.html("");
        this.model.forEach(this.add);
    }
});

var TodoListItemView = Backbone.View.extend({
    tagName: "button",
    className: "list-group-item",
    template: _.template($(".todo-list-item-template").html()),

    events: {
        "click .btn-edit": "editTodo",
        "click .btn-delete": "deleteTodo",
        "click": "toggleChecked"
    },

    initialize: function() {
        this.listenTo(this.model, "change", this.renderText);
        this.listenTo(this.model, "destroy", this.remove);
    },

    render: function() {
        this.$el.html(this.template());
        this.renderText();
        this.renderCheckedState();
        return this;
    },

    renderText: function() {
        this.$el.find(".list-group-item-heading").html(this.model.get("title"));
        this.$el.find(".list-group-item-text").html(this.model.get("text"));
    },

    renderCheckedState: function() {
        this.$el.toggleClass("checked", this.model.get("checked"));
    },

    toggleChecked: function(e) {
        // TODO: ugly hack
        if ($(e.target).hasClass("glyphicon"))
            return;

        this.model.set("checked", !this.model.get("checked"));
        this.model.save();
        this.renderCheckedState();
    },

    editTodo: function() {
        page.todo_editor_view.show(this.model);
    },

    deleteTodo: function() {
        this.model.destroy({ wait: true });
    }
});

var TodoEditorView = Backbone.View.extend({
    el: "#add-todo-modal",

    events: {
        "show.bs.modal": "onShow",
        "click .btn-save": "save"
    },

    initialize: function() {
        _.bindAll(this, "show", "hide");
    },

    show: function(model) {
        this.model = model;
        this.$el.modal("show");
    },

    hide: function() {
        this.$el.modal("hide");
    },

    onShow: function() {
        this.$(".input-title").val(this.model ? this.model.get("title") : "");
        this.$(".input-text").val(this.model ? this.model.get("text") : "");
    },

    save: function() {
        var attrs = {
            title: this.$(".input-title").val(),
            text: this.$(".input-text").val()
        };

        var options = {
            wait: true,
            success: this.hide
        };

        if (this.model)
            this.model.save(attrs, options);
        else
            todos.create(attrs, options);
    }
});
