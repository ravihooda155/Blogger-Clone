function enable_iframe()
{
    if(rich_test.document.designMode == "on")
        return
    else
        rich_test.document.designMode = "on";
}

function change(command)
{
    rich_test.document.execCommand(command,false,null);
}
function changewitharg(command,arg)
{
    rich_test.document.execCommand(command,false,arg);
}
function show(i)
{
//   var x = document.getElementsByName("rich_test");
  var y = (window.frames[0].document.body.innerHTML );
  title=document.getElementById('title').value;
//   alert(y);
  var formData = new FormData();
  formData.append('data', y);
  formData.append('title',title);
  formData.append('published',i);
  formData.append('theme',document.getElementById("theme_choice").value);
  alert(document.getElementById("theme_choice").value);
  url=window.location.href;
  temp=url.split('/');
  blog_id=temp[temp.length-1];
  console.log(blog_id);
  formData.append('blog_id',blog_id);

  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    document.getElementById("new_content").innerHTML = this.responseText;
    }
};
  xhr.open('POST', 'http://127.0.0.1:5000/addrec', true);
  xhr.send(formData);
//   document.getElementById('text_name').value=y;
   
  return y;
}
setTimeout(enable_iframe(),50)

function get_comment(blog_id)
{
    var formData = new FormData();
    formData.append('blog_id', blog_id);

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText)

            text =   '<hr/><form action="/add_comment" class="form-inline" method = "post">'+
            '<textarea name="blog_id" value="'+blog_id + '"hidden>'+blog_id+'</textarea>'+
            '<input type="text" class="form-control" name="plain_text" placeholder="Enter your comment here" style="width:80%;margin-right:1em;">'+
            '<button class="btn btn-default" onclick="submit">Submit</button></form>'
          
        
        document.getElementById("comment"+blog_id).innerHTML = this.responseText + text;
        }
    };
    xhr.open('POST', 'http://127.0.0.1:5000/comment', true);
    xhr.send(formData);
    //   document.getElementById('text_name').value=y;
    return y; 
}


function del_blog(blog_id)
{
    var formData = new FormData();
    formData.append('blog_id', blog_id);

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // console.log(this.responseText, typeof(this.responseText));
            if (this.responseText=='1')
                $("#blog"+blog_id).fadeOut('slow');
        
        // document.getElementById("delete"+blog_id).innerHTML = this.responseText + text;
        }
    };
    xhr.open('POST', 'http://127.0.0.1:5000/del_blog', true);
    xhr.send(formData);
    //   document.getElementById('text_name').value=y;
    // return y; 
    
}

function edit_blog(blog_id){
    // var formData = new FormData();
    // formData.append('blog_id', blog_id);

    // var xhr = new XMLHttpRequest();
    // xhr.onreadystatechange = function() {
    //     if (this.readyState == 4 && this.status == 200) {
    //         // console.log(this.responseText, typeof(this.responseText));
    //         if (this.responseText=='1')
    //             $("#blog"+blog_id).fadeOut('slow');
        
    //     // document.getElementById("delete"+blog_id).innerHTML = this.responseText + text;
    //     }
    // };
    // str = 'http://127.0.0.1:5000/editor/'+blog_id;
    // console.log(str);
    // xhr.open('POST', str, true);
    // xhr.send(formData);
    url = "/editor/"+blog_id;
    window.location = url;
}
