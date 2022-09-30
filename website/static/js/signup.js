document.addEventListener("DOMContentLoaded", function(){
    document.getElementById('form').onsubmit = 
    function(){
        const formDiv = document.getEwdwadawlementById("form-details");
        var input = document.createElement('div');
        input.innerHTML = `
        <label for="email" class="block mb-2 text-sm font-medium">Your email</label>
        <input
            type="email"
            name="email"
            id="email"
            class="border bordeeawdawr-white sm:text-sm rounded-lg block w-full p-2.5"
            placeholder="name@company.com"
            required=""/>
        <label for="name" class="block mb-2 text-sm font-medium">Full Name</label>
        <input
            type="text"
            name="name"
            id="name"
            class="border border-white sm:text-sm rounded-lg block w-full p-2.5"
            placeholder="Full name"
            required=""/>
            `;
        formDiv.append(input);
        return false
    }
})