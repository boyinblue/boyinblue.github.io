const link_info = document.getElementById('link_info');
document.addEventListener("mousemove", (e) => { // mousemove이벤트를 이용해 움
    // 마우스의 좌표는 clientX와 clientY를 이용해 알수 있다. -> 브라우저 window의 좌표값 위치를 전달한다.
    // pageX, pageY와는 다름.
    const mouseX = e.clientX;
    const mouseY = e.clientY;
    link_info.style.left = mouseX + 'px';
    link_info.style.top = mouseY + 'px';
    });

function show_page_info() {
    const page_info = document.getElementById('page_info');
    page_info.style.display = 'block';
}

function show_comment() {
    const comment_window = document.getElementById('disqus_window');
    comment_window.style.display = 'block';
}

// Hide Header on on scroll down
var didScroll;
var lastScrollTop = 0;
var delta = 5;

$(window).scroll(function(event){
    didScroll = true;
});

setInterval(function() {
    if (didScroll) {
        hasScrolled();
        didScroll = false;
    }
}, 250);

const header_window = document.getElementById('header_wrap');

function hasScrolled() {
    var st = $(this).scrollTop();
    
    // Make sure they scroll more than delta
    if(Math.abs(lastScrollTop - st) <= delta)
        return;
    
    // If they scrolled down and are past the navbar, add class .nav-up.
    // This is necessary so you never see what is "behind" the navbar.
    if (st > lastScrollTop && st > navbarHeight){
        // Scroll Down
        header_window.style.display = 'block';
    } else {
        // Scroll Up
        header_window.style.display = 'none';
    }
    
    lastScrollTop = st;
}