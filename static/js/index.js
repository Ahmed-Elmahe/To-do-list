document.getElementById("joinNow")?.addEventListener("click", function () {
  window.location.href = "/signup";
});

// Move to Completed/Incomplete logic using event delegation
document.addEventListener("DOMContentLoaded", function () {
  const taskList = document.getElementById("taskList");
  if (taskList) {
    taskList.addEventListener("click", function (e) {
      if (e.target.classList.contains("move-completed-btn") || e.target.classList.contains("move-incomplete-btn")) {
        const taskItem = e.target.closest(".task-item");
        if (!taskItem) return;
        // Find the checkbox inside the .task-meta form
        const checkbox = taskItem.querySelector(".task-meta form .task-checkbox");
        if (checkbox) {
          checkbox.checked = !checkbox.checked;
          checkbox.form.submit();
        }
      }
    });
  }
});

// Add global showTasks function
window.showTasks = function(filter, btn) {
  const allTasksDiv = document.getElementById("allTasksDiv");
  const completedTasksDiv = document.getElementById("completedTasksDiv");
  const incompleteTasksDiv = document.getElementById("incompleteTasksDiv");
  // Show/hide divs
  if (filter === "all") {
    allTasksDiv.style.display = "";
    completedTasksDiv.style.display = "none";
    incompleteTasksDiv.style.display = "none";
  } else if (filter === "completed") {
    allTasksDiv.style.display = "none";
    completedTasksDiv.style.display = "";
    incompleteTasksDiv.style.display = "none";
  } else if (filter === "active") {
    allTasksDiv.style.display = "none";
    completedTasksDiv.style.display = "none";
    incompleteTasksDiv.style.display = "";
  }
  // Toggle active class
  document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
  btn.classList.add("active");
};

