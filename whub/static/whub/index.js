document.addEventListener('DOMContentLoaded', function() {

},
false);

function upvote(revid)
{
  var id = 'v'+revid;
  document.getElementById(id).innerHTML = parseInt(document.getElementById(id).innerHTML) + 1;

  var sid = 's'+revid;
  document.getElementById(sid).innerHTML = parseInt(document.getElementById(sid).innerHTML) + 1;
  $.ajax({
    type:"GET",
    url: "upvote",
    data:{ revid: revid},
    error: function(){
      alert('failure upvote');
    }
  });
}

function downvote(revid)
{
  var id = 'v'+revid;
  document.getElementById(id).innerHTML = parseInt(document.getElementById(id).innerHTML) - 1;

  var sid = 's'+revid;
  document.getElementById(sid).innerHTML = parseInt(document.getElementById(sid).innerHTML) - 1;

  $.ajax({
    type:"GET",
    url: "downvote",
    data:{ revid: revid},
    error: function(){
      alert('failure downvote');
    }
  });
}

function search()
{
  var key = document.getElementById("search-input").value;
  $.ajax({
    type:"get",
    url: "search",
    data:{ key: key},
    error: function(){
      alert('failure search');
    },
    success: function(data){
      document.getElementsByTagName("BODY")[0].innerHTML = "";
      document.write("<div>"+ data +"</div>")

    }
  });
}

function send(rid)
{
  var text = "";
  if(document.getElementById(rid).value != "")
  {
    text = document.getElementById(rid).value;
    document.getElementById(rid).value = "";
  }

  else {
    var sid = 't'+rid;
    text = document.getElementById(sid).value;
    document.getElementById(sid).value = "";
  }

  $.ajax({
    type:"get",
    url: "comment",
    data:{ rid: rid, text:text},
    error: function(){
      alert('failure comment');
    },
    success: function(){
      location = location;
      return false;
    }
  });
}


function searchinp(e)
{
  if (e.keyCode == 13) {
    var key = document.getElementById("search-input").value;
    $.ajax({
      type:"get",
      url: "search",
      data:{ key: key},
      error: function(){
        alert('failure search');
      },
      success: function(data){
        document.getElementsByTagName("BODY")[0].innerHTML = "";
        document.write("<div>"+ data +"</div>")

      }
    });
  }
}

function sendcmt(e, rid)
{
  if (e.keyCode == 13) {

    var text = "";
    if(document.getElementById(rid).value != "")
    {
      text = document.getElementById(rid).value;
      document.getElementById(rid).value = "";
    }

    else {
      var sid = 't'+rid;
      text = document.getElementById(sid).value;
      document.getElementById(sid).value = "";
    }


    $.ajax({
      type:"get",
      url: "comment",
      data:{ rid: rid, text:text},
      error: function(){
        alert('failure comment');
      },
      success: function(){
        location = location;
        return false;
      }
    });
  }
}
