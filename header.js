// 'use strict';

// const e = React.createElement;
class NavBar extends React.Component {
    constructor(props) {
        super(props);
    }
    render(){
        return (
            <div>
                <header style={{display:"flex"}}>
                    <div id="nav-menu-button" style={{zIndex:0}}
                    onClick={()=>{let [menu_icon,menu]=[document.getElementById('nav-menu-button'),document.getElementById('nav-menu-content')];(menu.style.display==="none")?(menu.style.display="block"):(menu.style.display="none");menu_icon.style.zIndex="1";}}>
                        <svg viewBox="0 0 100 80" width="40" height="40" style={{transform:'scale(75%)'}}>
                            <rect width="100" height="20" rx="10"></rect>
                            <rect y="30" width="100" height="20" rx="10"></rect>
                            <rect y="60" width="100" height="20" rx="10"></rect>
                        </svg>
                    </div>
                    <div id="nav-menu-content" style={{position:'absolute',display:'none'}}>
                        <div id="nav-menu-content-inner">
                            <a href="home.html" className="underline">Home</a>
                            <a href="index.html" className="underline">A</a>
                            <a href="files.html" className="underline">Files</a>
                            <a href="https://kkevin.me/vigilant-telegram" className="underline">vigilant-telegram</a>
                            <a href="https://rickrollredirect.github.io" className="underline">glowing-pancake</a>
                        </div>
                    </div>
                    <h1 style={{margin:'auto',cursor:'pointer'}} id="nav-header" onClick={()=>{window.location.href='index.html'}}>
                        K
                    </h1>
                </header>
            </div>
        );
    }
}

const domContainer = document.querySelector('#react-domain-alpha');
const root = ReactDOM.createRoot(domContainer);
root.render(React.createElement(NavBar));