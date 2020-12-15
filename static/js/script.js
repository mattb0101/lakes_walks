$(document).ready(function(){
    let loadScreenWidth = $(document).width();
    if (loadScreenWidth < 600 ) {
        $(".walk-header").removeClass("horizontal");
    }

    $('.sidenav').sidenav();
    $('.dropdown-trigger').dropdown({hover: false});
    $('.collapsible').collapsible();
    $('.fixed-action-btn').floatingActionButton({direction: 'left', hoverEnabled: false});
    $('.materialboxed').materialbox();
    $('.modal').modal();
    $('select').formSelect();

    // Resize comment and text area when typed in - Split this off from the standard as it was throwing an error that there was no textarea to change.
    if (window.location.pathname == '/walk.html') {
        $('#user_comment').val();
        M.textareaAutoResize($('#user_comment'));
    }


    // Adding this in as mobile screens dont want the horizontal class on the image and header image for the walk. 
    $(window).resize(function() {
        let screenWidth = $(window).width();
        if (screenWidth < 600) {
            $(".walk-header").removeClass("horizontal");
        } else {
            $(".walk-header").addClass("horizontal");
        }
    });
});

