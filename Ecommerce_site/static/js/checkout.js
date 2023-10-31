$(document).ready(function(){
    $('.payWithRazorpay').click(function (e) {
        e.preventDefault();

        var fname = $("[name='fname']").val();
        var lname = $("[name='lname']").val();
        var email = $("[name='fname']").val();
        var phone = $("[name='fname']").val();
        var address = $("[name='address']").val();
        var city  = $("[name='city']").val();
        var state = $("[name='state']").val();
        var country = $("[name='country']").val();
        var pincode = $("[name='pincode']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();

        if(fname == "" || lname == "" || email == "" || phone == "" || address == "" || city == "" || state == "" || country == "" || pincode ==""){
             
            swal("Alert!","All field are mendatory", "error");
            return false;
        }
        else{
            $.ajax({
                method: "GET",
                url: "/proceed-to-pay",  // URL must match the one defined in your Django URLs
                
                success: function(response) {
                    //  console.log(response);
                    var options = {
                        "key": "rzp_test_pPnsEaruqWjT1D", // Enter the Key ID generated from the Dashboard
                        // "amount": response.total_price*100,
                        "amount": 1*100,  // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Prince Code",
                        "description": "Thank for buying with us.",
                        "image": "https://example.com/your_logo",
                        // "order_id": "order_IluGWxBm9U8zJ8", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (responseb){
                            alert(responseb.razorpay_payment_id);
                            // alert(response.razorpay_order_id);
                            // alert(response.razorpay_signature)
                            data = {
                              "fname" : fname,
                              "lname" : lname,  
                              "email" : email,
                              "phone" : phone,
                              "address" : address,
                              "city" : city,
                              "state" : state,
                              "country" :country,
                              "pincode" : pincode,
                              "payment_mode" : "Paid by Razorpay",
                              "payment_id" : responseb.razorpay_payment_id,
                               csrfmiddlewaretoken : token

                            }
                            $.ajax({
                                method: "POST",
                                url: "/place-order",  // URL must match the one defined in your Django URLs
                                data: data,
                                success: function(responsec) {
                                    // alertify.success(response.status);
                                    swal("Congratulation!",responsec.status, "success") ;
                                    
                                },
                            });
                        },
                        
                        "prefill": {
                            "name": fname+" "+lname,
                            "email": email,
                            "contact":  phone,
                        },
                        
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    
                    rzp1.open();
        
                }
            });

        }


    });
});