document.getElementById("submit_login").onclick = function() {
    axios({
        method: "POST",
        url: "http://localhost:3000/posts",
        data: {
            title: "axios学习",
            author: "Yehaocong"
        }
    }).then(response => {
        console.log(response);
    })
};