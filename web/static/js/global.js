$(document).ready(function () {

    $('#buttondesc').click(function () {
        alert("Item Adicionado ao Carrinho com Sucesso");
    });




    $("#searchLivro").submit(function (e) {
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),

            success: function (json) {
                console.log.json
            }
        })


    })

    


    $("input").one("click", function () {
        pk = $('#pk').attr('value');
        rating = $(this).attr('value');
        url = $(this).attr('href');

        $.get('http://127.0.0.1:8000/insrating/' + pk + "/" + rating, function (data) {
            if (data.rating) {
                $("#rating").html('Avaliações positivas '+ data.rating);


            }

        })


    });


});

