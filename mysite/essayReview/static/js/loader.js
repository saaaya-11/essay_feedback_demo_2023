const form=document.forms.input_form;
const loader=form.querySelector(".loader");
const button=form.querySelector(".submit_button");
const loadStart= () => {
    button.addEventListener('click', (e)=>{
        loader.style.display="block";
    }, false);
};
loadStart();