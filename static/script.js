
// js script for dropdown effects
function toggleSection(id) {
    var section = document.getElementById(id);
    section.style.display = (section.style.display === 'none' || section.style.display === '') ? 'block' : 'none';
}


// immutable string in js
const letters = "01";
// script to make words effects on appear disappear with anything but I chose numbers idk
// snippet of when user hovers over the words on the website it will trigger an action, decalres the css code inside the query selector
document.querySelector(".club-subtitle").onmouseover = event =>{
    // making sure the letters dont change when not neccessary
    let iterations = 0;

    // this snippet of code will fetch the number of letter that you want to iterate
    const targetTextLength = event.target.dataset.value.length;


    // runner to make sure the letters changes on their own
    const interval = setInterval(() => {

    // split letters so each one is random uniquely
        event.target.innerText = event.target.innerText.split("")
            // event maker, randoom number between 0 and 26 and random letters from const letters string
                // maps to each letter in the total word
                .map((letter, index) => {
                    if(index < iterations) {
                        return event.target.dataset.value[index]
                    }
                    return letters[Math.floor(Math.random() * 2)]
                })
                .join("");

            // if iterations reach 9 then clear the interval and reset the counter
            if(iterations >= targetTextLength) clearInterval(interval);
            iterations +=1/3;
    }, 75)
}