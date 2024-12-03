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