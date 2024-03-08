document.addEventListener('DOMContentLoaded', function () {
    loadTodos();

    document.getElementById('addBtn').addEventListener('click', function () {
        const todoInput = document.getElementById('todoInput');
        const todoText = todoInput.value.trim();

        if (todoText !== '') {
            addTodoToLocalStorage(todoText);
            todoInput.value = '';
            loadTodos();
        }
    });

    function loadTodos() {
        const todoList = document.getElementById('todo-list');
        todoList.innerHTML = '';

        const todos = getTodosFromLocalStorage();
        todos.forEach(function (todo, index) {
            const todoItem = document.createElement('div');
            todoItem.classList.add('row', 'custom-row', 'todo');

            const col9 = document.createElement('div');
            col9.classList.add('col-9', 'custom-col');
            if(todo.isUpdate){
                const editInput = document.createElement('input');
                editInput.id = 'editInput'; // Add an ID to distinguish it
                editInput.type = 'text';
                editInput.value = todo.text;
                editInput.classList.add('form-control', 'mt-1');
                editInput.style.padding = '10px';
                editInput.style.borderRadius = '20px';
                col9.appendChild(editInput);
                todoItem.appendChild(col9)

                const colButtons = document.createElement('div');
                colButtons.classList.add('col', 'custom-col');

                const updateButton = document.createElement('button');
                updateButton.classList.add('btn', 'btn-info', 'm-1');
                updateButton.textContent = 'Update';
                updateButton.addEventListener('click', function () {
                    updateTodo(index)
                });
                colButtons.appendChild(updateButton);

                const closeButton = document.createElement('button');
                closeButton.classList.add('btn', 'btn-danger');
                closeButton.textContent = 'Close';
                closeButton.addEventListener('click', function () {
                    closeTodo(index);
                });
                colButtons.appendChild(closeButton);

                todoItem.appendChild(colButtons);
            }else{
                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.classList.add('form-check-input', 'm-1');
                checkbox.checked = todo.isCompleted;
                checkbox.addEventListener('change', function () {
                    checkedTodo(index)
                });
                col9.appendChild(checkbox);

                const todoTextElement = document.createElement('span');
                if(todo.isCompleted){
                    todoTextElement.classList.add('strikethrough');
                }
                todoTextElement.textContent = todo.text;
                col9.appendChild(todoTextElement);

                todoItem.appendChild(col9);

                const colButtons = document.createElement('div');
                colButtons.classList.add('col', 'custom-col');

                const editButton = document.createElement('button');
                editButton.classList.add('btn', 'btn-warning', 'm-1');
                editButton.textContent = 'Edit';
                editButton.addEventListener('click', function () {
                    editTodo(index);
                });
                colButtons.appendChild(editButton);

                const deleteButton = document.createElement('button');
                deleteButton.classList.add('btn', 'btn-danger');
                deleteButton.textContent = 'Delete';
                deleteButton.addEventListener('click', function () {
                    deleteTodo(index);
                });
                colButtons.appendChild(deleteButton);

                todoItem.appendChild(colButtons);
            }
            todoList.appendChild(todoItem);
        });
    }

    function addTodoToLocalStorage(text) {
        const todos = getTodosFromLocalStorage();
        todos.push({
            text: text,
            isCompleted: false,
            isUpdate:false
        });
        localStorage.setItem('todos', JSON.stringify(todos));
    }

    function getTodosFromLocalStorage() {
        return JSON.parse(localStorage.getItem('todos')) || [];
    }

    function deleteTodo(index) {
        const todos = getTodosFromLocalStorage();
        todos.splice(index, 1);
        localStorage.setItem('todos', JSON.stringify(todos));
        loadTodos();
    }

    function editTodo(index) {
        const todos = getTodosFromLocalStorage();
        todos[index].isUpdate = !todos[index].isUpdate
        localStorage.setItem('todos', JSON.stringify(todos));
        loadTodos();
    }

    function closeTodo(index){
        const todos = getTodosFromLocalStorage();
        todos[index].isUpdate = !todos[index].isUpdate
        localStorage.setItem('todos', JSON.stringify(todos));
        loadTodos();
    }

    function updateTodo(index){
        const todoInput = document.getElementById('editInput');
        const todoText = todoInput.value.trim();

        if (todoText !== '') {
            const todos = getTodosFromLocalStorage();
            todos[index].text = todoText
            todos[index].isUpdate = !todos[index].isUpdate
            localStorage.setItem('todos', JSON.stringify(todos));
            loadTodos();
        }
    }

    function checkedTodo(index){
        const todos = getTodosFromLocalStorage();
        todos[index].isCompleted = !todos[index].isCompleted
        localStorage.setItem('todos', JSON.stringify(todos));
        loadTodos();
    }
});
