// A $( document ).ready() block.
$( document ).ready(function() {
  $( "#rotate" ).click(function() {
    colorList.unshift(colorList.pop());
    console.log(colorList);
    for (i = 0; i < colorList.length; i++) {
      console.log(i);
      console.log(colorList[i]);
        var elem = document.getElementById(i);
        elem.style.backgroundColor = 'rgb(' + colorList[i] +')';
    }
  });
});
