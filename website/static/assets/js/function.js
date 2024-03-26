console.log("working");

//дописать месяцы
const months = ["Jan", "Feb","March", "April", "May", "June", 
"July", "Aug", "Sept", "Oct", "Nov", "Dec"];

$("#commentForm").submit(function(e){
    e.preventDefault();

    let dt = new Date();
    let time = dt.getDay() + " " + months[dt.getUTCMonth()] + ", " + dt.getFullYear()

    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr("method"),
        url: $(this).attr("action"),
        dataType: "json",
        success: function(response){
            console.log("Review saved to Database");

            if(response.bool == true){
                $("#reviewFinal").html("Review added!")
                $(".hide-comment-form").hide()
                $(".add-review-here").hide()

                // расположить див с начала лупа до его конца(не включая луп)
                let _html = '<div>'
                    _html += '<a href = "#" class= "font-heading text-brand">' + response.context.user + '</a>'
                            
                    _html += '<div>'
                    _html += '<div>'
                    _html += '<span>' + time + '</span>'
                    _html += '</div>'

                    for(let i =1; i<=response.context.rating; i++){

                        _html += '<i class = "fas fa-star text-warning"></i>'
                    }

                    _html += '</div>'
                    _html += '<p>'+ response.context.review + '</p>'
                    $(".comment-list").prepend(_html)
            }
            // работа для comment-list
            

        }
    })
})

// filter function 

$(document).ready(function () {
    $(".filter-checkbox, #price-filter").on("click", function(){
        console.log("A checkbox have been clicked");
    
        let filter_object = {}

        let min_price = $('#max_price').attr("min")
        let max_price = $('#max_price').val()

        filter_object.min_price = min_price;
        filter_object.max_price = max_price;

        $(".filter-checkbox").each(function() {
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter") // vendor, category

            // console.log("Filter value is:", filter_value);
            // console.log("Filter key is:", filter_key);

            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter=' + filter_key + ']:checked')).map(function(element){
                return element.value
            })
        }) 
        console.log("Filter Object is: ", filter_object);
        $.ajax({
            url: '/filter-products',
            data: filter_object, 
            dataType: 'json',
            beforeSend: function() {
                console.log("Trying to filter product...");
            },
            success: function(response) {
                console.log(response);
                console.log("Data filtered successfully...");
            $("#filtered-product").html(response.data)
            }
        })
    })
    $("#max_price").on("blur", function(){
        let min_price = $(this).attr("min")
        let max_price = $(this).attr("max")
        let current_price = $(this).val()

        // console.log("Current Price is:", current_price);
        // console.log("Max Price is:", max_price);
        // console.log("Min Price is:", min_price);

        if(current_price < parseInt(min_price) || current_price > parseInt(max_price)){
            alert("Price must between " + min_price + 'tg and ' + max_price + 'tg')
            $(this).val(min_price)
            $('#range').val(min_price)

            $(this).focus()

            return false
        }
    })
})