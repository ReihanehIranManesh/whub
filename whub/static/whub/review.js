document.addEventListener('DOMContentLoaded', function() {

  $('.step').change(function() {
    var next_step = $(this).next('.step');
    var all_next_steps = $(this).nextAll('.step');
    // If the element *has* a value
    if ($(this).val()) {
      // Should also perform validation here
      next_step.attr('disabled', false);
    }
    // If the element doesn't have a value
    else {
      // Clear the value of all next steps and disable
      all_next_steps.val('');
      all_next_steps.attr('disabled', true);
    }
  });

  $('.step').keydown(function(event) {
    // If they pressed tab AND the input has a (valid) value
    if ($(this).val() && event.keyCode == 9) {
      $(this).next('.step').attr('disabled', false);
    }
  });

},
false);

function openmodal()
{
  $('.modal-body input:checkbox').prop('checked', false);
  $('.modal-body input:checkbox').prop('disabled', false);
  $('#myModal').modal('show');
  jQuery(function(){
    var max = 3;
    var checkboxes = jQuery('.modal-body input[type="checkbox"]');
    checkboxes.change(function(){
      var current = checkboxes.filter(':checked').length;
      checkboxes.filter(':not(:checked)').prop('disabled', current >= max);
    });
  });
}
function choose()
{
  var checkboxes = jQuery('.modal-body input[type="checkbox"]');
  var current = checkboxes.filter(':checked').length;
  if(current == 0)
  {
    alert('You should choose at least one category.');
  }
  else {
    $('#myModal').modal('toggle');
  }
}
function submit()
{
  var checkboxes = jQuery('.modal-body input[type="checkbox"]');
  var current = checkboxes.filter(':checked').length;
  if(current == 0)
  {
    alert('You should choose at least one category.');
  }
  else {
    if(document.getElementById('city').value)
    {
      if(document.getElementById('title').value)
      {
        if(tinyMCE.get('mytextarea').getContent({ format: "text" }).length == 1)
        {
          alert('You should write a brief review of your trip.');
        }
        else if(tinyMCE.get('mytextarea').getContent({ format: "text" }).length > 200)
        {
          alert("You have reached the maximum allowed words for your review.");
        }
        else
        {
          if(document.getElementById('dostep1').value && document.getElementById('dontstep1').value)
          {
            var values = ""
            for (i = 0; i < checkboxes.length; i ++)
            {
              if(checkboxes[i].checked)
              {
                values = values + checkboxes[i].value + ",";
              }
            }
            values = values.substr(0, values.length - 1);

            var content = tinyMCE.get('mytextarea').getContent({ format: "text" })
            var imge =  document.getElementById('img').value;
            var country =  document.getElementById('dls-input').value;
            $.ajax({
              type:"GET",
              url: "reviewcard",
              data:{ categories: values, title: document.getElementById('title').value, text: content, city : document.getElementById('city').value , country : country, image : imge, votes: 0},
              error: function(){
                alert('failure submit');
              }
            });

            var dos = document.getElementById("Dos").children;
            for (i = 0; i < dos.length; i++ )
            {
              if (dos[i].value)
              {
                $.ajax({
                  type:"GET",
                  url: "do",
                  data:{ text: dos[i].value},
                  error: function(){
                    alert('failure do');
                  }
                });
              }
            }

            var donts = document.getElementById("Don'ts").children;
            for (i = 0; i < donts.length; i++ )
            {
              if (donts[i].value)
              {
                $.ajax({
                  type:"GET",
                  url: "dont",
                  data:{ text: donts[i].value},
                  error: function(){
                    alert('failure dont');
                  }
                });
              }
            }

            alert("Thank you for your submission and sharing your valuable opinions to everyone.");
            location.href="/"

          }
          else {
            alert('You should at least give one tip.');
          }
        }
      }
      else {
        alert('You should fill in the title of your review.');
      }
    }
    else {
      alert('You should fill in the name of the city you visited.');
    }
  }
}
