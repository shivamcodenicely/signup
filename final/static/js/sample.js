/**
 * Created by sony on 12/3/18.
 */


function sign()
{

   var fname = document.getElementById('fname').value;
   var lname = document.getElementById('lname').value;
   var uname = document.getElementById('uname').value;

   // var pwd = document.getElementById('pwd').value;
   var email = document.getElementById('email').value;
   var contact=document.getElementById('contact').value;
   alert(fname);
   alert(lname);
   alert(uname);
   alert(contact);
   //alert(pwd);
   alert(email);

   $.ajax({
        url: '/signup/ajax/validate_username/',
        type: 'POST',
        data: {
          'email': email
        },
        dataType: 'json',
        success: function (sign) {
          if (sign.is_taken) {
            alert("A user with this username already exists.");
          }

        }
      });

// JSON.stringify(fname);
// JSON.stringify(lname);
// JSON.stringify(uname);
// JSON.stringify(pwd);
// JSON.stringify(email);
// JSON.stringify(contact);

// callFacebook();
// $.ajax({
//     url: '/login/login',
//     type: 'POST', // This is the default though, you don't actually need to always mention it
//     data:{ "fname":fname,"lname":lname,"uname":uname,"pwd":pwd,"email":email,"contact":contact},
//     success: function (data) {
//         alert("success")
//     }
//
// });
// function js(){
//     alert("eryi");
//   $.ajax({
//         url: '/signup/ajax/validate_username/',
//         type: 'POST',
//         data: {
//           'email': email
//         },
//         dataType: 'json',
//         success: function (sign) {
//           if (sign.is_taken) {
//             alert("A user with this username already exists.");
//           }
//
//         }
//       });

}


