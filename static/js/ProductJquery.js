$(function(){
    var Quantity = +$("#values").val();
    var Price = +$("#price").text();

    $("#ProductPlus").on("click",function(){
        Quantity += 1 ;
        $("#values").val(Quantity);
        totalPrice = Price * Quantity;
        $("#price").html(totalPrice);
    });

    $("#ProductMinus").on("click",function(){
        Quantity -= 1 ;
        if(Quantity<=1){Quantity = 1 ;}
        $("#values").val(Quantity);
        totalPrice = Price * Quantity;
        $("#price").html(totalPrice);
    });
});