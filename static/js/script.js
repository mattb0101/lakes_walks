$(document).ready(function(){
    let loadScreenWidth = $(document).width();
    if (loadScreenWidth < 600 ) {
        $(".walk-header").removeClass("horizontal")
    }

    $('.sidenav').sidenav();
    $('.dropdown-trigger').dropdown({hover: false});
    $('.collapsible').collapsible();
    $('.fixed-action-btn').floatingActionButton({direction: 'left', hoverEnabled: false});
    // Resize comment and texzt area when typed in
    $('#user_comment').val();
    M.textareaAutoResize($('#user_comment'));
    $('.materialboxed').materialbox();
    $('.modal').modal();
    $('select').formSelect();


    // Adding this in as mobile screens dont want the horizontal class and 
    $(window).resize(function() {
        let screenWidth = $(window).width();
        if (screenWidth < 600) {
            $(".walk-header").removeClass("horizontal")
        } else {
            $(".walk-header").addClass("horizontal")
        }
    })
});

