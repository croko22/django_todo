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
});
