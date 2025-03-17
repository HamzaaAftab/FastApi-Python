document.getElementById("add-btn").addEventListener("click", function() {
    let title = document.getElementById("task-title").value;
    let desc = document.getElementById("task-desc").value;

    if (title.trim() === "" || desc.trim() === "") {
        alert("Enter task title and description!");
        return;
    }

    let taskList = document.getElementById("task-container");
    
    let taskItem = document.createElement("li");
    taskItem.innerHTML = `
        <div class="task-content">
            <div class="task-title">${title}</div>
            <div class="task-desc">${desc}</div>
        </div>
        <div class="task-buttons">
            <button class="update">Update</button>
            <button class="delete">Delete</button>
        </div>
    `;

    taskList.appendChild(taskItem);

    document.getElementById("task-title").value = "";
    document.getElementById("task-desc").value = "";
});

// 🗑️ Delete Task
document.addEventListener("click", function(event) {
    if (event.target.classList.contains("delete")) {
        event.target.closest("li").remove();
    }
});

// ✏️ Update Task
document.addEventListener("click", function(event) {
    if (event.target.classList.contains("update")) {
        let taskItem = event.target.closest("li");
        let titleElement = taskItem.querySelector(".task-title");
        let descElement = taskItem.querySelector(".task-desc");

        let newTitle = prompt("Enter new title:", titleElement.innerText);
        let newDesc = prompt("Enter new description:", descElement.innerText);

        if (newTitle !== null && newTitle.trim() !== "") {
            titleElement.innerText = newTitle;
        }
        if (newDesc !== null && newDesc.trim() !== "") {
            descElement.innerText = newDesc;
        }
    }
});
