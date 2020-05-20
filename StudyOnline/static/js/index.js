/**
 * 
 * @authors jinbo (you@example.org)
 * @date    2019-12-18 19:42:10
 * @version $Id$
 */

function btnCloseLoginBox(){
	var bg=document.getElementsByClassName("hidenBox");
	bg[0].style.display="none";
	var loginWin=document.getElementsByClassName("topLogin-Box");
	loginWin[0].style.display="none"
}

function btnLoginAndRegisterClicked()
{
	var bg=document.getElementsByClassName("hidenBox");
	bg[0].style.display="block";
	var loginWin=document.getElementsByClassName("topLogin-Box");
	loginWin[0].style.display="block"
}
