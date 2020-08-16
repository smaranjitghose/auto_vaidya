//Play an animation back on second click
var preloader = document.getElementById("loading");
function myFunction(){

	preloader.style.display = 'none';
}



let iconMenu = document.querySelectorAll('.bodymovinanim');
var i = 2;
while (i--) {
	let animationMenu = bodymovin.loadAnimation({
		container: iconMenu[i],
		renderer: 'svg',
		loop: true,
		autoplay: false,
		path: 'assets/js/github.json'
	});

	var directionMenu = 1;
	iconMenu[i].addEventListener('mouseenter', (e) => {
		animationMenu.setDirection(directionMenu);
		animationMenu.play();
	});

	iconMenu[i].addEventListener('mouseleave', (e) => {
		animationMenu.stop();
	});
}
i = 2;
let iconMenu2 = document.querySelectorAll('.linkedin');
while (i--) {
	let animationMenu2 = bodymovin.loadAnimation({
		container: iconMenu2[i],
		renderer: 'svg',
		loop: true,
		autoplay: false,
		path: 'assets/js/linkedin.json'
	});

	var directionMenu2 = 1;
	iconMenu2[i].addEventListener('mouseenter', (e) => {
		animationMenu2.setDirection(directionMenu2);
		animationMenu2.play();
	});

	iconMenu2[i].addEventListener('mouseleave', (e) => {
		animationMenu2.stop();
	});
	//moved from html code.
    $(document).ready(function(){
		$('.sidenav').sidenav();
	});
	$(document).ready(function(){
    	$('.fixed-action-btn').floatingActionButton();
  	});
	
}

