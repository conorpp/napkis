var Settings = {
    host:'http://napkis.com',
    message_port:10705, //production - 10705
    redis_port:14177,//production - 14177
    hostIP:'184.173.103.51'
}

try {
    module.exports = Settings;
} catch(e) {
}