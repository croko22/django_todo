document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("task-modal");
  const addTaskBtn = document.getElementById("add-task-btn");
  const closeModalBtn = document.querySelector(".modal__close");
  const taskIdInput = document.getElementById("task-id");
  const taskTitleInput = document.getElementById("task-title");
  const taskDescriptionInput = document.getElementById("task-description");

  addTaskBtn.addEventListener("click", () => {
    taskIdInput.value = "";
    taskTitleInput.value = "";
    taskDescriptionInput.value = "";
    modal.style.display = "flex";
  });

  closeModalBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

  document.querySelectorAll(".task-card__edit-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      console.log("Edit button clicked");
      console.log("Task ID:", btn.dataset.taskId);
      console.log("Task Title:", btn.dataset.taskTitle);
      console.log("Task Description:", btn.dataset.taskDescription);

      const taskId = btn.dataset.taskId;
      const taskTitle = btn.dataset.taskTitle;
      const taskDescription = btn.dataset.taskDescription;

      taskIdInput.value = taskId || "";
      taskTitleInput.value = taskTitle || "";
      taskDescriptionInput.value = taskDescription || "";

      modal.style.display = "flex";
    });
  });
});
