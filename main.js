document.getElementById("ssubmit").addEventListener("click",(e)=>{
    e.preventDefault();
    let username = document.getElementById("text_username").value;
    let password = document.getElementById("text_password").value;
    document.getElementById("text_username").value = "";
    document.getElementById("text_password").value = "";
    var obj = {u : username, p: password};
    var myJSON = JSON.stringify(obj);
    $.ajax({
        url : './api',
        type : "POST",
        data : myJSON,
        contentType: "application/json; charset=utf-8",
        success : function(data){
          console.log(data)
          
          
        }
   
          });//ajax fetch data end
});