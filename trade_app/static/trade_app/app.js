function getCookie(c_name){
    if (document.cookie.length > 0){
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1){
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}

$(function(){

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    $('.sch-watch-box').hide();
  
    $('.sch-watch').on('click', function(){
       $('.sch-watch-box').toggle();
    })

    $('.sch-watch-btn').on('click', function(){
        query = $('.sch-watch-input').val()
        
        if(query === ''){
            $('.sch-watch-input').focus()
        }
        else{
            var settings = {
                "async": true,
                "crossDomain": true,
                "url": `https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete?region=US&q=${query}`,
                "method": "GET",
                "headers": {
                    "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
                    "x-rapidapi-key": "3031e33fd9msh3c73fd1d3122a19p1a03abjsn0397c5598162"
                }
            }
            
            $.ajax(settings).done(function(response){
                console.log('request finished')
                var data = response.quotes; 
                symbol = data[0].symbol; 
                name = data[0].longname;
    
                if(name === 'undefined'){
                    console.log('There was an error with this request. This symbol does not exist.');
                    $('.sch-watch-input').val('');
                }
                else{
                    $.ajax({
                        url: '/portfolio/search/',
                        method: 'POST',
                        data: {
                            'symbol':symbol,
                            'name':name
                        },
                        success: function(){
                            location.reload();
                        }
                    })
                }
            })
        }
    })

    $('.trade-quantity').on('change', function(){
        quantity = $('.trade-quantity').val()
        price = $('.pricing').val()
        estimate = quantity * price
        $('#estimate').text(estimate.toFixed(2))
        $('.order-error').text('')  
    })

    $('.order-btn').on('click', function(){
        total = parseFloat($('#estimate').text())
        cash = parseFloat($('#usr-cash').text())
        action = $('.action').val();
        quantity = $('.trade-quantity').val();
        shares = parseInt($('#shares').text())
        if(action == 'Buy' && total > cash){
            $('.order-error').text('Your order exceeds the cash available for trading.')
        }
        else if(action == 'Sell' && quantity > shares){
            $('.order-error').text('Your order exceeds the number of shares you have available for trading.')
        }
        else{ 
            symbol = $('#h-sym').text(); 
            name = $('#h-name').text();
            $.ajax({
                url: '/checkout/',
                method: 'POST',
                data: {
                    'symbol':symbol,
                    'name':name,
                    'action':action,
                    'quantity':quantity,
                    'total':total
                },
                success: function(){
                    location.href = '/portfolio/'
                },
                error: function(data){
                    console.log('error: ' + data);
                }
            })
        }
    })
})
