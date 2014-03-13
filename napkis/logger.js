
//dependents for websockets with python:
//$ sudo apt-get install redis-server
//$ sudo pip install redis
//$ sudo apt-get install python-software-properties 
//$ sudo add-apt-repository ppa:chris-lea/node.js
//$ sudo apt-get update
//$ sudo apt-get install nodejs
//$ npm install socket.io
//$ npm install cookie
//$ npm install crypto


//production - 14177
//dev - 6379
var REDIS_PORT = 14177;
//var REDIS_PORT = 6379;
var Settings = require('./static_admin/settings/settings');
console.log('------------------------------------------------\n');
console.log('Starting up Node.  Here is the config : \n',Settings);
console.log('\n------------------------------------------------\n');

var http = require('http');
var server = http.createServer().listen(Settings.message_port, Settings.hostIP);

var io = require('socket.io').listen(server);
var redis = require('socket.io/node_modules/redis');
var gen = redis.createClient(Settings.redis_port);	//general functions redis. Channel 0 only.
gen.subscribe(0); 	
io.configure(function(){
    io.set('authorization', function(data, accept){
	return accept(null, true);
    });
    io.set('log level',1);
});
io.sockets.on('connection', function(socket){

    console.log('user connected');
    socket.on('disconnect', function(data){
        console.log('User disconnected.');
    });

    
}); // end io.sockets.on
//This is what sends data back to client
gen.on('message', General);			//channel 0 only.


function General(channel, data){
    if (channel != 0 ) return; 
    data = JSON.parse(data);
    //console.log('data', data);
    switch(data['TYPE']){

    
	case 'log':
	    console.log('LOG : ', data['log']);
	break;
    
	case 'menuitem':
	    console.log('sending menuitem update : ', data);
	    io.sockets.emit('menuitem', data);
	break;
    
	default:
	    console.log('None of cases were met for general publish. Nothing was done.');
    }
}


