document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("task-modal");
  const addTaskBtn = document.getElementById("add-task-btn");
  const closeModalBtn = document.querySelector(".modal__close");
  const taskForm = document.getElementById("task-form");
  const taskIdInput = document.getElementById("task-id");
  const taskTitleInput = document.getElementById("task-title");
  const taskDescriptionInput = document.getElementById("task-description");

  // Open modal for creating a new task
  addTaskBtn.addEventListener("click", () => {
    taskIdInput.value = "";
    taskTitleInput.value = "";
    taskDescriptionInput.value = "";
    modal.style.display = "flex";
  });

  // Close modal
  closeModalBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

  taskForm.addEventListener("submit", async function (e) {
    e.preventDefault();
    const id = document.getElementById("task-id").value;
    const title = document.getElementById("task-title").value;
    const description = document.getElementById("task-description").value;

    const formData = new FormData();
    formData.append("id", id);
    formData.append("title", title);
    formData.append("description", description);

    const response = await fetch("/save/", {
      method: "POST",
      body: formData,
      headers: { "X-CSRFToken": getCookie("csrftoken") },
    });

    const data = await response.json();
    console.log(data);
  });

  // Handle delete button
  document.querySelectorAll(".task-card__delete-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const taskId = btn.dataset.taskId;
      console.log("Deleting Task ID:", taskId);
      // Send delete request to the server

      fetch(`/tasks/${taskId}`, {
        method: "DELETE",
        body: JSON.stringify({ task_id: taskId }),
      })
        .then((response) => {
          if (response.ok) {
            const taskItem = btn.closest(".task-list__item");
            taskItem.remove();
            console.log("Task deleted successfully");
          } else {
            console.error("Failed to delete task");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  });
});
