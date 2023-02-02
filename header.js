// class ShoppingList extends React.Component {
//     render() {
//         return (
//             <div className="shopping-list">
//                 <h1>Shopping List for {this.props.name}</h1>
//                 <ul>
//                     <li>Instagram</li>
//                     <li>WhatsApp</li>
//                     <li>Oculus</li>
//                 </ul>
//             </div>
//         );
//     }
// }

// Example usage: <ShoppingList name="Mark" />
// 'use strict';

const e = React.createElement;
class NavBar extends React.Component {
    constructor(props) {
        super(props);
    }
    render(){
        return (
            <div>
                <h1>Header (hopefully this works)</h1>
                <h2>dasflkajdskfljdsaklfjdasklfjkldasjkfldsakfjadkslf</h2>
                <script type="text/javascript">alert("daklfjadsklfjdsaklfj")</script>
            </div>
        );
    }
}

alert("i dont like react nothings working THIS ISNT EVEN BEING CALLED")
const domContainer = document.querySelector('#react-domain-alpha');
const root = ReactDOM.createRoot(domContainer);
root.render(e(NavBar));
