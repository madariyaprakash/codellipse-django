<script>
var header = document.getElementById("pagination");
var btns = header.getElementsByClassName("page-item");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() 
  {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  }
  );
}
</script>