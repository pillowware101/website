function writeCookieusrname(username){
	var username2='username='+username+'; expires=Thu, 1 Jan 4040 12:00:00 UTC';
	document.cookie=username2;
}
function writeCookiepsswrd(psswrd){
	var psswrdcookie='password='+psswrd+'; expires=Thu, 1 Jan 4040 12:00:00 UTC';
	document.cookie=psswrdcookie;
}