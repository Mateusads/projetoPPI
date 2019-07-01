$(document).ready(function () {

    $('#buttondesc').click(function () {
        alert("Item Adicionado ao Carrinho com Sucesso");
    });

    $('.card-js').click(function () {
        $('.card-body').css('background', 'gray');
    });


    $("#searchLivro").submit(function(e){
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),

            success: function(json){
                console.log.json
            }
        })


    })

});

