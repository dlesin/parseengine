$(window).scroll(function () {
    if ($(document).scrollTop() > 50) {
        $('.nav__link').css('padding', '12px 10px');
    } else {
        $('.nav__link').css('padding', '20px 10px');
    }
});

$("#get-video").on('click', function (e) {
    e.preventDefault();
    url = $("#video-quality").val();
    window.location.replace(url);
});


// $(".nav__searchbtn").click(function(){
//   $(this).toggleClass("bg-transparent");
//   //$(".fa").toggleClass("color-white");
//   $(".input").focus().toggleClass("active-width").val('');
// });

/*// cart scripts
$(document).ready(function () {
    $('.remove-from-cart').on('click', function (e) {
        e.preventDefault();
        product_slug = $(this).attr('data-slug');
        item_product_id = $(this).attr('data-id');
        data = {
            product_slug: product_slug
        };
        $.ajax({
            type: 'GET',
            url: '/remove_from_cart/',
            data: data,
            success: function (data) {
                $('#cart-count').html(data.cart_total);
                //$('.cart-item-' + item_product_id).css('display', 'none')
                $('.cart-item-' + item_product_id).remove();
                $('#cart-total-price').html('<strong>' + parseFloat(data.cart_total_price).toFixed(2) + ' руб.' + '</strong>');
                if (parseInt(data.cart_total) === 0) {
                    //$('.my-cart').css('display', 'none')
                    $('.my-cart').remove();
                    $('.cart-empty').html('<h3 class="text-center">Ваша корзина пуста</h3>')
                }
            }
        })
    })
});
$(document).ready(function () {
    $('#cart-item-qty').on('click', function (e) {
        qty = $(this).val();
        item_id = $(this).attr('data-id');
        data = {
            qty: qty,
            item_id: item_id
        };
        $.ajax({
            type: 'GET',
            url: '/change_item_qty/',
            data: data,
            success: function (data) {
                $('#cart-item-total-' + item_id).html('<strong>' + parseFloat(data.item_total).toFixed(2) + ' руб.' + '</strong>');
                $('#cart-total-price').html('<strong>' + parseFloat(data.cart_total_price).toFixed(2) + ' руб.' + '</strong>')
            }
        })
    })
});
$(document).ready(function () {
    $('#cart-item-qty').on('input keyup', function (e) {
        e.preventDefault();
        qty = $(this).val();
        if (qty <= 5 && qty != '') {        
            item_id = $(this).attr('data-id');
            data = {
                qty: qty,
                item_id: item_id
            };
            $.ajax({
                type: 'GET',
                url: '/change_item_qty/',
                data: data,
                success: function (data) {
                    $('#cart-item-total-' + item_id).html('<strong>' + parseFloat(data.item_total).toFixed(2) + ' руб.' + '</strong>');
                    $('#cart-total-price').html('<strong>' + parseFloat(data.cart_total_price).toFixed(2) + ' руб.' + '</strong>')
                }
            })
        }
    })
});
// product scripts
$(document).ready(function () {
    $('.add-to-cart-product').on('click', function (e) {
        e.preventDefault();
        product_slug = $(this).attr('data-slug');
        data = {
            product_slug: product_slug
        };
        $.ajax({
            type: 'GET',
            url: '/add_to_cart/',
            data: data,
            success: function (data) {
                $('#cart-count').html(data.cart_total);
                $('.add-to-cart-product').remove();
                $('#button').html('<a href="/cart/" id="add-to-cart-order">' + '<button class="btn btn-success">' + 'Оформить' + '</button>' + '</a>')
            }
        })
    })
});
//home scripts
$(document).ready(function () {
    $('.add-to-cart-home').on('click', function (e) {
        e.preventDefault();
        product_slug = $(this).attr('data-slug');
        data = {
            product_slug: product_slug
        };
        $.ajax({
            type: 'GET',
            url: '/add_to_cart/',
            data: data,
            success: function (data) {
                $('#cart-count').html(data.cart_total);
                $('#add-to-cart-' + product_slug).remove();
                $('#button-' + product_slug).html('<a href="/cart/" id="add-to-cart-order">' + '<button class="btn btn-success">' + 'Оформить' + '</button>' + '</a>')
            }
        })
    })
});

// order scripts
$(document).ready(function () {
    //$('#div_id_address').css('display', 'none');
    $('#id_buying_type').on('click', function () {
        buying_type = $(this).val()
        if(buying_type === 'delivery') {
            $('#id_address').css('display', 'block');
        }else {
            $('#id_address').css('display', 'none');
        }
    })
});
*/