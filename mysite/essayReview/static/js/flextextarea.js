function flexTextarea(el){
    const dummy=el.querySelector(".flexTextarea__dummy")
    el.querySelector(".flexTextarea__text").addEventListener('input', e=>{
        dummy.textContent=e.target.value+'\u200b'
    })
}
document.querySelectorAll(".flexTextarea").forEach(flexTextarea)