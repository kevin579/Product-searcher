var min_slider = document.getElementById("min-price-range");
var min_price = document.getElementById("min-price");
var max_slider = document.getElementById("max-price-range");
var max_price = document.getElementById("max-price");
var min_value = min_slider.value;
var max_value = max_slider.value;
min_price.innerHTML = min_slider.value;
max_price.innerHTML = max_slider.value;


var price_order = document.getElementById("sort")
var text = document.getElementById("order")


min_slider.oninput = function(){
    
    min_value = Math.max(0.1,(Math.round(Math.pow(this.value,5)/10000000000000000*100)/100));
    if (min_value>=max_value){
        max_value = Math.min(10000,Math.round(min_value*1.1*100)/100);
        max_slider.value = Math.min(10000,Math.round(this.value*1.1*100)/100);
        max_price.innerHTML = max_value;
    }
    min_price.innerHTML = min_value;
    
}




max_slider.oninput = function(){
    max_value = Math.max(1,(Math.round(Math.pow(this.value,5)/10000000000000000*100)/100));
    if (min_value>=max_value){
        
        min_value = Math.max(0.1,Math.round(max_value*0.9*100)/100);
        if (min_value<=0.95){
            min_value=0.1;
            min_slider.value = 0.1;
        }
        else{
            min_slider.value = Math.max(0.1,Math.round(this.value*0.9*100)/100);
        }
        
        min_price.innerHTML = min_value;
    }
    
    max_price.innerHTML = max_value;
}

var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  /* For each element, create a new DIV that will act as the selected item: */
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  /* For each element, create a new DIV that will contain the option list: */
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    /* For each option in the original select element,
    create a new DIV that will act as an option item: */
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
        /* When an item is clicked, update the original select box,
        and the selected item: */
        var y, i, k, s, h, sl, yl;
        s = this.parentNode.parentNode.getElementsByTagName("select")[0];
        sl = s.length;
        h = this.parentNode.previousSibling;
        for (i = 0; i < sl; i++) {
          if (s.options[i].innerHTML == this.innerHTML) {
            s.selectedIndex = i;
            h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }
        h.click();
    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    /* When the select box is clicked, close any other select boxes,
    and open/close the current select box: */
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  /* A function that will close all select boxes in the document,
  except the current select box: */
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

/* If the user clicks anywhere outside the select box,
then close all select boxes: */
document.addEventListener("click", closeAllSelect);