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