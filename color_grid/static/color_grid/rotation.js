// A $( document ).ready() block.
$( document ).ready(function() {
  var counter = 0;
  $("td.random-color-cell").each(function() {
    //Assign IDs to table cells.
    $(this).attr("id", idList[counter]);
    $(this).text(idList[counter]);
    counter++;
  });
  $( "#rotate" ).click(function() {
    colorList.unshift(colorList.pop()); //Move last color to first in array.
    for (i = 0; i < colorList.length; i++) {
      //Apply new colors to each cell.
      var elem = document.getElementById(i);
      elem.style.backgroundColor = 'rgb(' + colorList[i] +')';
    }
  });
});
