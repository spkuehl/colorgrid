// A $( document ).ready() block.
$( document ).ready(function() {
  var counter = 0;
  $("td.random-color-cell").each(function() {
      $(this).attr("id", counter);
      counter++;

      // compare id to what you want
  });
  $( "#rotate" ).click(function() {
    colorList.unshift(colorList.pop());
    console.log(colorList);
    for (i = 0; i < colorList.length; i++) {
        var elem = document.getElementById(i);
        elem.style.backgroundColor = 'rgb(' + colorList[i] +')';
    }
  });
});
