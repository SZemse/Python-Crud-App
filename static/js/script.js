$(function () {
  $("#admin-link").click(function () {
    $("#login-box").hide();
    $("#admin-box").show();
  });
  $("#login-link").click(function () {
    $("#login-box").show();
    $("#admin-box").hide();
  });
  $("#forgot-link").click(function () {
    $("#login-box").hide();
    $("#forgot-box").show();
  });
  $("#back-link").click(function () {
    $("#login-box").show();
    $("#forgot-box").hide();
  });
});