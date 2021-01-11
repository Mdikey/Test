var phx = function (){
    let socket = new Socket("127.0.0.1:4000/socket", {params: {userToken: "123"}})
socket.connect()
let channel = socket.channel("room:123", {token: roomToken})
channel.on("new_msg", msg => console.log("Got message", msg) )
$input.onEnter( e => {
  channel.push("new_msg", {body: e.target.val}, 10000)
    .receive("ok", (msg) => console.log("created message", msg) )
    .receive("error", (reasons) => console.log("create failed", reasons) )
    .receive("timeout", () => console.log("Networking issue...") )
})

channel.join()
  .receive("ok", ({messages}) => console.log("catching up", messages) )
  .receive("error", ({reason}) => console.log("failed join", reason) )
  .receive("timeout", () => console.log("Networking issue. Still waiting..."))}
  var tst = function(){
console.log("tst")
  }

    var gql2 = function(){
var xd = document.getElementById('xdat');
// xd.innerHTML="";
xd.setAttribute("x-data","{}");

// Event.stopPropagation()
{/* <div @my-custom-event.stop="handleIt()"> */}
{/* <button x-data @click="$dispatch('hey-fetch-the-data')"></button> */}


    }

//     // Select the node that will be observed for mutations
// const targetNode = document.getElementById('some-id');

// // Options for the observer (which mutations to observe)
// const config = { attributes: true, childList: true, subtree: true };

// // Callback function to execute when mutations are observed
// const callback = function(mutationsList, observer) {
//     // Use traditional 'for loops' for IE 11
//     for(const mutation of mutationsList) {
//         if (mutation.type === 'childList') {
//             console.log('A child node has been added or removed.');
//         }
//         else if (mutation.type === 'attributes') {
//             console.log('The ' + mutation.attributeName + ' attribute was modified.');
//         }
//     }
// };

// // Create an observer instance linked to the callback function
// const observer = new MutationObserver(callback);

// // Start observing the target node for configured mutations
// observer.observe(targetNode, config);

// // Later, you can stop observing
// observer.disconnect();