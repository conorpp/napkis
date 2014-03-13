
$(document).ready(function(){
    $('#soon, #header, #sideBar').hide();
    var showHeader = 320;
    $('#header').show(showHeader);
    
    setInterval(function(){
        $('#soon').show(300);
    },showHeader);
    
    setInterval(function(){
        $('#sideBar').show(300);
    },showHeader);
    
    $('h1').mouseenter(function(){
        $(this).find('.glyphicon').css('color','#2c00ba');
    });
    $('h1').mouseleave(function(){
        $(this).find('.glyphicon').css('color','black');
    });
    
    $(document).scroll(function(){
        var top = $(document).scrollTop();
        console.log(top);
        if (top < 110) {
            var current = 110;
            var result = current - top;
            console.log('result ', result);
            $('#sideBar').css('top', result+'px');
        }else{
            $('#sideBar').css('top', '0px');
        }
    });
    
});

/*  Namespace and event listeners for node messaging  */


var Message = {
    /*
        connect to chat app, make web socket.
        connection issues UI.
    */
    connect: function(){
        try {
            
            this.socket = io.connect(Settings.host, {port: Settings.message_port});
            this.socket.on('connecting', function () {});
            this.socket.on('connect', function(){
            });
            this.socket.on('reconnecting', function(){

            });
            this.socket.on('reconnect_failed', function () {

            });
            this.socket.on('reconnect', function () {

            });
            this.socket.on('disconnect', function () {

            });
        } catch(e) {
            this.socket = $();
            console.log("Failed connecting to socket.  Chat.js probably isn't running. ", e);
        }

    },

    /*
        Send message to everyone in conversation Cpk
    */
    updateMenu: function(html){
 
    },

    
};
    
    Message.connect();

/*Message.socket.on('menuitem', function(data) {
    console.log('got data ', data);
    if ($('#menuitems').length) {
        $('#menuitems').append(data.html);
    }
});*/
Message.socket.on('menuitem', function(data) {
    console.log('got data ', data);
    if ($('#menuitems').length) {
      //  setTimeout(function(){
        $('#menuitems').append(data.html);
        $('#menuitem'+data.pk).hide();
        $('#menuitems').find('tbody').append( $('#menuitem'+data.pk) );
        $('#menuitem'+data.pk).show(420);
        $("html, body").animate({ scrollTop: "30000px" },250);
       // },3000);
    }
});

