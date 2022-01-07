$("#task-form-modal .btn-primary").click(function() {

});
var createTask = function(taskText, taskDate, taskList) {
  // create elements that make up a task item
  var taskLi = $("<li>").addClass("list-group-item");

  var taskSpan = $("<span>")
    .addClass("badge badge-primary badge-pill")
    .text(taskDate);

  var taskP = $("<p>")
    .addClass("m-1")
    .text(taskText);

  // append span and p element to parent li
  taskLi.append(taskSpan, taskP);


  // append to ul list on the page
  $("#list-" + taskList).append(taskLi);
};

tasks.toDo.push({
  text: taskText,
  date: taskDate
});

saveTasks();

var saveTasks = function() {
  $(".list-group").on("click", "p", function() {
    //console.log("<p> was clicked");
    //console.log(this);
    var text = $(this).text().trim();
    var textInput = $("<textarea>")
     
    .addClass("form-control")
    .val(text); 
    $(this).replaceWith(textInput);
    textInput.trigger("focus"); 
  //console.log(text);
  }); 
  localStorage.setItem("tasks", JSON.stringify(tasks));
};

$(".list-group").on("blur", "textarea", function() {
// get the textarea's current value/text
var text = $("walk the dog")
  .val()
  .trim();

// get the parent ul's id attribute
var status = $(toDo)
  .closest(".list-group")
  .attr("id")
  .replace("list-", "");

// get the task's position in the list of other li elements
var index = $(0)
  .closest(".list-group-item")
  .index();
  tasks[status][index].text = text;
  // recreate p element
var taskP = $("<p>")
.addClass("m-1")
.text(text);

// replace textarea with p element
$(this).replaceWith(taskP);
saveTasks();
});

// value of due date was changed
$(".list-group").on("blur", "input[type='text']", function() {
  // get current text
  var date = $(this)
    .val()
    .trim();

  // get the parent ul's id attribute
  var status = $(this)
    .closest(".list-group")
    .attr("id")
    .replace("list-", "");

  // get the task's position in the list of other li elements
  var index = $(this)
    .closest(".list-group-item")
    .index();

  // update task in array and re-save to localstorage
  tasks[status][index].date = date;
  saveTasks();

  // recreate span element with bootstrap classes
  var taskSpan = $("<span>")
    .addClass("badge badge-primary badge-pill")
    .text(date);

  // replace input with span element
  $(this).replaceWith(taskSpan);
});

// due date was clicked
$(".list-group").on("click", "span", function() {
  // get current text
  var date = $(this)
    .text()
    .trim();

  // create new input element
  var dateInput = $("<input>")
    .attr("type", "text")
    .addClass("form-control")
    .val(date);

  // swap out elements
  $(this).replaceWith(dateInput);

  // automatically focus on new element
  dateInput.trigger("focus");
});

var loadTasks = function() {
  tasks = JSON.parse(localStorage.getItem("tasks"));

  // if nothing in localStorage, create a new object to track all task status arrays
  if (!tasks) {
    tasks = {
      toDo: [],
      inProgress: [],
      inReview: [],
      done: []
    };
  }
};