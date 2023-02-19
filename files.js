const setItems=(files)=>{
    for (let i = 0; i < files.length; i++) {
        let li = document.createElement('li');
        li.innerHTML = files[i];
        document.getElementById('items').appendChild(li);
}}
class Files extends React.Component {

    constructor(props) {
        super(props);
        this.files=[];
        this.getFiles();
    }
    getFiles(){
        // return fetch('https://142.198.226.37:6010', {
        //     method: 'GET',
        //     headers: {
        //         'Content-Type': 'application/json',
        //         'command':'list'
        //     }
        // })
        //     .then(response => response.json())
        //     .then(data => {
        //         this.files = data;
        //         console.log(this.files);
        //     })
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'https://142.198.226.37:6010', true);
        xhr.setRequestHeader('command', 'list');
        xhr.onload = function () {
            if (this.status === 200) {
                this.files = JSON.parse(this.responseText);
                console.log(this.files);
                document.addEventListener('DOMContentLoaded', ()=>{setItems(this.files)});
            }
        }
        xhr.onerror = function () {
            alert('smth happened, better check the console')
        }
        xhr.send()
    }
    render(){
        return (
            <div>
                <h3>Items</h3>
                <ul id={'items'}></ul>
            </div>
        );
    }
}

const domContainer = document.querySelector('#react-domain-beta');
const root = ReactDOM.createRoot(domContainer);
root.render(React.createElement(Files));
