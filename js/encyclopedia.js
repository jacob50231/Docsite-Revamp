const hideDocList = () => {
  document.querySelectorAll(".doc-list").forEach((element) => {
    element.classList.add("hidden");
  });
};

window.addEventListener("load", hideDocList());

const btns = document.querySelectorAll(".term-button");
btns.forEach((btn) => {
  btn.addEventListener("click", () => {
    hideDocList();
    buttonValue = btn.getAttribute("value");
    buildId = buttonValue + "-list";
    console.log(buildId);
    post = document.querySelector(`#${buildId}`);
    document.querySelector(".encyclopedia-content").classList.add("hidden");
    post.classList.remove("hidden");
  });
});

// document
//   .getElementById("resetbtn")
//   .addEventListener("click", () => location.reload(true));
