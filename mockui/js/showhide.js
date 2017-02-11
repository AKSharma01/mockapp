$(document).ready(function(){
     // on click SignIn Button checks for valid email and all field should be filled
	 $("#login").click(function(){
		var email = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);

		if( $("#loginemail").val()=='' || $("#loginpassword").val()=='')
		{
		  alert("Please fill all fields...!!!!!!");
		}

		else if(!($("#loginemail").val()).match(email))
		{
			alert("Please enter valid Email...!!!!!!");
		}

		else
		{
		 
		 $("form")[0].reset();
		}

	 });

	 $("#register").click(function(){
		var email = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);

		if( $("#name").val()=='' || $("#registeremail").val()=='' || $("#registerpassword").val()=='' || $("#contact").val()=='')
		{
		  alert("Please fill all fields...!!!!!!");
		}

		else if(!($("#registeremail").val()).match(email))
		{
			alert("Please enter valid Email...!!!!!!");
		}

		else
		{

		 $("#form")[0].reset();
		 $("#second").slideUp("slow",function(){
	      $("#first").slideDown("slow");
	   });
		}

	 });


	 // on click signup It Hide Login Form and Display Registration Form
	 $("#signup").click(function(){
       $("#first").slideUp("slow", function(){
		  $("#second").slideDown("slow");
	   });
	 });

	 // on click signin It Hide Registration Form and Display Login Form
     $("#signin").click(function(){
       $("#second").slideUp("slow",function(){
	      $("#first").slideDown("slow");
	   });
	 });

});
